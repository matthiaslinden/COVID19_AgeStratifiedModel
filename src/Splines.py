
import numpy as np
import theano

import theano.tensor as tt


"""

Implements chains multidimensional of Catmull-Rom-splines in Theano

TODO:
	* There is an issue on OSX, running as a script, where constant-folding optimization causes an errer. No problem running in a notebook or under linux...

"""
def tj05(ti,p1,p2):
	d = p2-p1
	dd = tt.dot(d,d)
	return tt.pow(dd,0.25)+ti
	
def tj05_split(ti,px1,px2,pv1,pv2,alpha=0.5):
	d = pv2-pv1
	dd = tt.dot(d,d)
	return tt.pow(dd+(px2-px1)*(px2-px1),alpha/2.)+ti

def CentripetalCatmullRomSpline_splitControls(cpx,cpv,space):
	""" Control points are split in location cpx and values (can be multi-dim),
	separating what's 'constant' numpy arrays (cpx, space) from theano objects (cpv)"""
	# scaled space (fixed positions, no theano)
	space1 = (space-cpx[1])/(cpx[2]-cpx[1])
		
	t0 = tt.cast(0.,"float64")
	t1 = tj05_split(t0,cpx[0],cpx[1],cpv[0],cpv[1])
	t2 = tj05_split(t1,cpx[1],cpx[2],cpv[1],cpv[2])
	t3 = tj05_split(t2,cpx[2],cpx[3],cpv[2],cpv[3])

	tspace = ( t1 + space1*(t2-t1) ).reshape((space.shape[0],1,))
	p = cpv.dimshuffle(0,'x',1)
	
	A1 = p[0] * (t1-tspace)/(t1) + p[1] * (tspace)/(t1)
	A2 = p[1] * (t2-tspace)/(t2-t1) + p[2] * (tspace-t1)/(t2-t1)
	A3 = p[2] * (t3-tspace)/(t3-t2) + p[3] * (tspace-t2)/(t3-t2)
	B1 = (t2-tspace)/(t2-t0)*A1 + (tspace-t0)/(t2-t0)*A2
	B2 = (t3-tspace)/(t3-t1)*A2 + (tspace-t1)/(t3-t1)*A3
	C = (t2-tspace)/(t2-t1)*B1 + (tspace-t1)/(t2-t1)*B2
	return C

class Spline(object):
	def __init__(self,cpx,cpv):
		"""
			cpx : control point x value, numpy:array [points]
			cpy : control point y value(s) theano:tensor [dimension,points]
		"""
		self.cpx = cpx
		self.cpv = cpv
		
	def EvaluateAt(self,space,expand=True):
		"""
			space, array of points along the x-space, where the Spline is evaluated
		"""
		if expand:
			cpx,cpv = self.ExpandCoverage(space)
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
			r = slice(i,i+4)
			segment = CentripetalCatmullRomSpline_splitControls(cpx[r],cpv[r],si)
			segments.append(segment)
		
		return tt.concatenate(segments,axis=0)
		
	def ExpandCoverage(self,space):
		""" Ensures that the ControlPoints cover the whole space by repeating the first/last control point"""
		cpx = self.cpx
		cpv = self.cpv		
		if space[0] < cpx[1]:
			d = cpx[1]-cpx[0]
			ncpx = np.reshape(cpx[0]-d,(1,))
			ncpv = cpv[:,0].dimshuffle(0,'x')
			if space[0] < cpx[0]:
				ncpx2 = np.reshape(space[0]-d,(1,))
				cpx = np.concatenate((ncpx2,ncpx,cpx))
				cpv = tt.concatenate((ncpv,ncpv,cpv),axis=1)
			else:
				cpx = np.concatenate((ncpx,cpx))
				cpv = tt.concatenate((ncpv,cpv),axis=1)
			
		if space[-1] > cpx[-2]:
			d = cpx[-1]-cpx[-2]
			ncpx = np.reshape(cpx[-1]+d,(1,))
			ncpv = cpv[:,-1].dimshuffle(0,'x')
			
			if space[-1] > cpx[-1]:
				ncpx2 = np.reshape(space[-1]+d,(1,))
				cpx = np.concatenate((cpx,ncpx,ncpx2))
				cpv = tt.concatenate((cpv,ncpv,ncpv),axis=1)
			else:
				cpx = np.concatenate((cpx,ncpx))
				cpv = tt.concatenate((cpv,ncpv),axis=1)
			
		return cpx,cpv
		

def main():
	theano.config.gcc.cxxflags = "-Wno-c++11-narrowing"	# Doesn't seem to work fixing the OSX issue.
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
	
	
if __name__ == "__main__":
	main()