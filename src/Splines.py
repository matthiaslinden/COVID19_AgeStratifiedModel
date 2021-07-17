
import numpy as np
import theano

#theano.config.gcc__cxxflags = "-Wno-c++11-narrowing"
#theano.config.optimizer="fast_run"
theano.config.exception_verbosity="high"

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
		self.single_dim = len(cpv.broadcastable) == 1
		if self.single_dim:
			self.cpv = cpv.dimshuffle('x',0)
		else:
			self.cpv = cpv
		
	def EvaluateAt(self,space,expand=True,old=False):
		"""
			space, array of points along the x-space, where the Spline is evaluated
		"""
		space = space-self.ref
		if expand:
			cpx,cpv,space = self.ExpandCoverage(space)
		else:
			cpx,cpv = self.cpx,self.cpv
		
		# Which implementation to use
		if old:
			cpv = cpv.dimshuffle(1,0)
			if self.single_dim:
				return self.SplitSpaceByControlPoints_old(cpx,cpv,space)[:,0]
			else:
				return self.SplitSpaceByControlPoints_old(cpx,cpv,space)
		else:
			if self.single_dim:
				return self.CalculateSpline(cpx,cpv,space)[0]
			else:
				return self.CalculateSpline(cpx,cpv,space)
		
	def SplitSpaceByControlPoints_old(self,cpx,cpv,space):
		"""
			This version is garbage. It creates a lot of redundant theano code for each segment.
			The plus side should have been it's memory footprint. But I doubt that.
			Runtime in pymc4 scales O^2 which is not usable above space-length of 200.
		"""
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
	
	def GenIndex(self,cpx,space,numpy_index = False):
		""" Generate the space-index, mapping space to control-point-segments
			numpy-index doesn't seem to work, as broadcasting is not possible in this version
		"""
		if numpy_index:
			index = np.zeros((cpx.shape[0]-3,space.shape[0],),"int8")
		else:
			index = tt.zeros((cpx.shape[0]-3,space.shape[0],),"int8")
		for i in range(cpx.shape[0]-3):
			idx = np.where((space >= cpx[i+1])*(space < cpx[i+2]))[0]
			if len(idx) > 0:
				if numpy_index:
					index[i,idx] = 1
				else:
					index = tt.set_subtensor(index[i,idx],1)
		return index	# segment x 1st-control-point
		
	def SplitSpaceByControlPoints(self,cpx,cpv,space):
		"""
			Improved version.
			index-tensor only needs to be created once.
		"""
		index = tt.cast(self.GenIndex(cpx,space),cpv.dtype)
	
		cpx_theano = tt.cast(cpx,cpv.dtype).dimshuffle(0,'x')
		cp = tt.concatenate([cpx_theano,cpv.dimshuffle(1,0)],axis=1)

		# segment x cp_i x dimensions
		cpm = tt.stack([cp[:-3],cp[1:-2],cp[2:-1],cp[3:]],axis=1)
		return index,cpm
	
	def CalculateSpline(self,cpx,cpv,space):
		"""
			new improved version. Vectorized calculation for the whole evaluation-space
			cpv as dimension x cp_i, a row for each control-dimension
		"""
		index,cpm = self.SplitSpaceByControlPoints(cpx,cpv,space)
		# Match dims: segment x cp_i x dimension x space
		index = index.dimshuffle(0,'x','x',1)
		cpm = cpm.dimshuffle(0,1,2,'x')
		
		# Control points: cp_i x dimension x space
		cp = tt.sum(index*cpm,axis=0)
		
		t = tt.zeros((space.shape[0],),cpv.dtype)
		ti = [t]
		for i in range(3):
			d = tt.sum((cp[i+1]-cp[i])*(cp[i+1]-cp[i]),axis=0)
			t = tt.pow(d,.25) + t
			ti.append(t)
		# t_i x space
		t = tt.stack(ti)
		
		# Scale the space
		spacet = tt.cast(space,cpv.dtype)
		space1 = (spacet-cp[1,0])/(cp[2,0]-cp[1,0])
		tspace = (t[1] + space1 * (t[2]-t[1]))
		p = cp[:,1:]
		
		A1 = p[0] * (t[1]-tspace)/t[1] + p[1] * tspace/t[1]
		A2 = p[1] * (t[2]-tspace)/(t[2]-t[1]) + p[2] * (tspace-t[1])/(t[2]-t[1])
		A3 = p[2] * (t[3]-tspace)/(t[3]-t[2]) + p[3] * (tspace-t[2])/(t[3]-t[2])
		B1 = A1 * (t[2]-tspace)/t[2] + A2 * tspace/t[2]
		B2 = A2 * (t[3]-tspace)/(t[3]-t[1]) + A3 * (tspace-t[1])/(t[3]-t[1])
		C = B1 * (t[2]-tspace)/(t[2]-t[1]) + B2 * (tspace-t[1])/(t[2]-t[1])
		return C
		
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
		

def main1():
		
	cpx = np.array([2,4,6,7,12],"float64")
	cpy1 = np.array([1,2,2,3,1],"float64")
	cpy2 = np.array([2,3,4,2,5],"float64")
	cpy3 = np.array([1,6,3,-4,-2],dtype="float64")
	
	cpx = np.array(cpx)
	cpy = tt.stack([cpy1,cpy2,cpy3])
	
	space = np.linspace(4.5,6.5,32,"float64")
	
	print(cpx)
	print(cpy.eval())
	print(space,space.dtype)
	
	s1 = Spline(cpx,cpy)
	c = s1.EvaluateAt(space,True)
	
	print(c.eval())
	
	
def main2():
	import pandas as pd
	import datetime
	import time
		
	start,end = datetime.datetime(2020,1,1),datetime.datetime(2020,12,31)
	dr1 = pd.date_range(start,end,freq='M')
	dr2 = pd.date_range(start,end,freq='D')


	y = tt.cast(np.array([3,3,3,.8,.9,.9,1,1.1,1.2,1.1,1,1.2],"float64"),"float64")

	s1 = Spline(dr1,y)
	print(s1.ref)
	
	t0 = time.time()
	v = s1.EvaluateAt(dr2,expand=True,old=False).eval()
	t1 = time.time()
	print("in %.3fs"%(t1-t0))
	
	print(dr1)
	print(y)
	print(v.shape)
	
if __name__ == "__main__":
	main1()
	
	main2()
