
import numpy as np
import theano

import theano.tensor as tt


"""

Implements chains multidimensional of Catmull-Rom-splines in Theano

TODO:
	* There is an issue on OSX, running as a script, where constant-folding optimization causes an errer. No problem running in a notebook or under linux...
		[fix: import pymc3 or theano.config.gcc__cxxflags = "-Wno-c++11-narrowing"]

"""
	
def tj05_split(px1,px2,pv1,pv2,alpha=0.5):
	d = pv2-pv1
	dd = tt.dot(d,d)
	return tt.pow(dd+(px2-px1)*(px2-px1),alpha/2.)

def CentripetalCatmullRomSpline_splitControls(cpx,cpv,space):
	""" Control points are split in location cpx and values (can be multi-dim),
	separating what's 'constant' numpy arrays (cpx, space) from theano objects (cpv)"""
	# scaled space (fixed positions, no theano)
	space1 = (space-cpx[1])/(cpx[2]-cpx[1])
		
	t0 = tt.cast(0.,"float64")
	t1 = tj05_split(cpx[0],cpx[1],cpv[0],cpv[1]) + t0
	t2 = tj05_split(cpx[1],cpx[2],cpv[1],cpv[2]) + t1
	t3 = tj05_split(cpx[2],cpx[3],cpv[2],cpv[3]) + t2

	tspace = ( t1 + space1*(t2-t1) ).reshape((space.shape[0],1,))
	p = cpv.dimshuffle(0,'x',1)
	
	A1 = p[0] * (t1-tspace)/(t1) + p[1] * (tspace)/(t1)
	A2 = p[1] * (t2-tspace)/(t2-t1) + p[2] * (tspace-t1)/(t2-t1)
	A3 = p[2] * (t3-tspace)/(t3-t2) + p[3] * (tspace-t2)/(t3-t2)
	B1 = (t2-tspace)/(t2)*A1 + (tspace)/(t2)*A2
	B2 = (t3-tspace)/(t3-t1)*A2 + (tspace-t1)/(t3-t1)*A3
	C = (t2-tspace)/(t2-t1)*B1 + (tspace-t1)/(t2-t1)*B2
	return C

class Spline(object):
	def __init__(self,cpx,cpv):
		"""
			cpx : control point x value, numpy:array [points]
			cpy : control point y value(s) theano:tensor [dimension,points]
		"""
		self.ref = cpx[0]
		self.cpx = cpx-self.ref
		self.cpv = cpv
		
	def EvaluateAt(self,space,expand=True):
		"""
			space, array of points along the x-space, where the Spline is evaluated
		"""
		space = space-self.ref
		if expand:
			cpx,cpv,space = self.ExpandCoverage(space)
		else:
			cpx,cpv = self.cpx,self.cpv
		cpv = cpv.dimshuffle(1,0)
		
		return self.SplitSpaceByControlPoints(cpx,cpv,space)
		
	def SplitSpaceByControlPoints(self,cpx,cpv,space):
		cpxt = tt.cast(cpx,cpv.dtype)
		segments = []
				
		for i in range(cpx.shape[0]-3):
			idx = np.where((space >= cpx[i+1])*(space < cpx[i+2]))
			si = space[idx]
			if len(si) > 0:
			
				r = slice(i,i+4)
			
				segment = CentripetalCatmullRomSpline_splitControls(cpx[r],cpv[r],si)
				segments.append(segment)
		
		return tt.concatenate(segments,axis=0)
		
	def ExpandCoverage(self,space):
		""" Ensures that the ControlPoints cover the whole space by repeating the first/last control point"""
		cpx = self.cpx
		cpv = self.cpv
		
		# Handle Datetime --> convert [ns] to 1-day = 1 unit
		if cpx.dtype == "timedelta64[ns]":
			cpx = cpx.astype(int).to_numpy()/(1000000000.*60*60*24)
			space = space.astype(int).to_numpy()/(1000000000.*60*60*24)
		
		if space[0] <= cpx[1]:
			d = cpx[1]-cpx[0]
			ncpx = np.reshape(min(space[0],cpx[0]-d),(1,))
			ncpv = cpv[:,0].dimshuffle(0,'x')
			if space[0] <= cpx[0]:
				ncpx2 = np.reshape(space[0]-d,(1,))
				cpx = np.concatenate((ncpx2,ncpx,cpx))
				cpv = tt.concatenate((ncpv,ncpv,cpv),axis=1)
			else:
				cpx = np.concatenate((ncpx,cpx))
				cpv = tt.concatenate((ncpv,cpv),axis=1)
		
		if space[-1] >= cpx[-2]:
			d = cpx[-1]-cpx[-2]
			ncpx = np.reshape(max(space[-1],cpx[-1]+d),(1,))
			ncpv = cpv[:,-1].dimshuffle(0,'x')
			
			if space[-1] >= cpx[-1]:
				ncpx2 = np.reshape(space[-1]+d,(1,))
				cpx = np.concatenate((cpx,ncpx,ncpx2))
				cpv = tt.concatenate((cpv,ncpv,ncpv),axis=1)
			else:
				cpx = np.concatenate((cpx,ncpx))
				cpv = tt.concatenate((cpv,ncpv),axis=1)
			
		return cpx,cpv,space
		

def main():
	theano.config.gcc__cxxflags = "-Wno-c++11-narrowing"
	theano.config.optimizer="fast_run"
	
	cpx = np.array([2,4,6,7,12],"float64")
	cpy1 = np.array([1,2,2,3,1],"float64")
	cpy2 = np.array([2,3,4,2,5],"float64")
	cpy3 = np.array([1,6,3,-4,-2],dtype="float64")
	
	cpx = np.array(cpx)
	cpy = tt.stack([cpy1,cpy2,cpy3])
	
	space = np.linspace(1,10,32,"float64")
	
	print(cpx)
	print(cpy.eval())
	print(space,space.dtype)
	
	s1 = Spline(cpx,cpy)
	c = s1.EvaluateAt(space,True)
	
	print(c.eval())
	
	
def main2():
	import pandas as pd
	import datetime
	
	theano.config.gcc__cxxflags = "-Wno-c++11-narrowing"	# Doesn't seem to work fixing the OSX issue.
	theano.config.optimizer="fast_run"
	
	start,end = datetime.datetime(2020,1,1),datetime.datetime(2020,12,31)
	dr1 = pd.date_range(start,end,freq='M')
	dr2 = pd.date_range(start,end,freq='D')


	y = tt.cast(np.array([3,3,3,.8,.9,.9,1,1.1,1.2,1.1,1,1.2],"float64").reshape(1,12),"float64")

	s1 = Spline(dr1,y)
	print(s1.ref)
	v = s1.EvaluateAt(dr2).eval()

	print(y.shape)

	print(dr1)
	print(y)
	
	
if __name__ == "__main__":
	main2()
