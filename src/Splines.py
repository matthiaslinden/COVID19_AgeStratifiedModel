
import numpy as np
import theano

import theano.tensor as tt


"""

Implements chains multidimensional of Catmull-Rom-splines in Theano

# Challenges
- split evaluation-space inbetween control-points
"""

#alpha = theano.tensor.dscalar()
#ti = theano.tensor.dscalar()
#p1 = theano.tensor.dvector()
#p2 = theano.tensor.dvector()

# t-space
def tj05(ti,p1,p2):
	d = p2-p1
	dd = tt.dot(d,d)
	return tt.pow(dd,0.25)+ti
	
#tj = theano.function([ti,p1,p2,alpha],f_tj(ti,p1,p2,alpha))

#def tj05_split(ti,px1,px2,pv1,pv2):
#	d = pv2-pv1
#	dd = tt.dot(d,d)
#	return tt.pow(dd+(px2-px1)*(px2-px1),0.25)+ti

def tj05_split(ti,px1,px2,pv1,pv2,alpha=0.5):
	d = pv2-pv1
	dd = tt.dot(d,d)
	return tt.pow(dd+(px2-px1)*(px2-px1),alpha/2.)+ti

def CentripetalCatmullRomSpline_splitControls(cpx,cpv,space):
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

def CentripetalCatmullRomSpline(cp,space):
	t0 = tt.cast(0.,"float32")
#	t1 = tj05(t0,cp[0],cp[1])
#	t2 = tj05(t1,cp[1],cp[2])
#	t3 = tj05(t2,cp[2],cp[3])
	
	t1 = tt.pow(tt.dot(cp[0]-cp[1],cp[0]-cp[1]),0.25)+t0
	t2 = tt.pow(tt.dot(cp[1]-cp[2],cp[1]-cp[2]),0.25)+t1
	t3 = tt.pow(tt.dot(cp[2]-cp[3],cp[2]-cp[3]),0.25)+t2
	
	print("cp",cp.eval())
	print("cp0",cp[0].eval())
	
	# map evaluation space
	space1 = (space-cp[1,0])/(cp[2,0]-cp[1,0])	
	tspace = ( t1 + space1*(t2-t1) )#.reshape((space.shape[0],1,1,))
	
#	print("tspace",tspace.eval())
	# broadcast
	p = cp[:,1:].dimshuffle('x',0,1)
	
	print(p.eval())

	print("ts",t0.eval(),t1.eval(),t2.eval(),t3.eval())
	print("p",p.eval())
	print("t1-tspace",(t1-tspace).eval())
	print("(t1-tspace)/(t1-t0)",((t1-tspace)/(t1-t0)).eval())
	print("(t1-tspace)/(t1-t0)",((t1-tspace)/(t1-t0)).reshape((space.shape[0],1)).eval())
	
	print("p0",p[:,0].eval())
	print("p0*(t1-tspace)/(t1-t0)",(p[:,0]*((t1-tspace)/(t1-t0)).reshape(space.shape[0],1)).eval())
#	print("p*(t1-tspace)")
	
#	print(((t1-tspace)/(t1-t0)).eval())
	
#	A1 = p[0,0] * (t1-tspace)/(t1-t0) + p[0,1] * (tspace-t0)/(t1-t0)
	
#	print(A1.eval())
	
#	A2 = p[1] * (t2-tspace)/(t2-t1) + p[2] * (tspace-t1)/(t2-t1)
#	A3 = p[2] * (t3-tspace)/(t3-t2) + p[3] * (tspace-t2)/(t3-t2)
#	B1 = (t2-tspace)/(t2-t0)*A1 + (tspace-t0)/(t2-t0)*A2
#	B2 = (t3-tspace)/(t3-t1)*A2 + (tspace-t1)/(t3-t1)*A3
#	C = (t2-tspace)/(t2-t1)*B1 + (tspace-t1)/(t2-t1)*B2
#	return C
	
	
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
		
		print(cpx)
		print(cpv.eval())
		
		return self.SplitSpaceByControlPoints(cpx,cpv,space)
		
	def SplitSpaceByControlPoints(self,cpx,cpv,space):
		
		cpxt = tt.cast(cpx,cpv.dtype)
#		cp = tt.concatenate([cpxt.dimshuffle(0,'x'),cpv.dimshuffle(1,0)],axis=1)
		
		segments = []
		
		for i in range(cpx.shape[0]-3):
#			cpi = cp[i:(i+4)]
			idx = np.where((space >= cpx[i+1])*(space < cpx[i+2]))
#			si = tt.cast(space[idx],cpv.dtype)
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
	theano.config.gcc.cxxflags = "-Wno-c++11-narrowing"
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