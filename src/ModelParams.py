import numpy as np
import xarray as xr
import pandas as pd
import datetime

from collections import OrderedDict

import theano
import theano.tensor as tt


"""
Helper functions for index handling and data-matching

"""

def IndexProperties(x):
    """ Try to infer properties of the index, countable [1,3,4] vs categorical
    stepsize
    continuity
    """
    try:
        steps = np.diff(x)
        stepsizes = len(set(steps))
    
        return {"countable":True,"continous":stepsizes==1,"stepsize":min(steps)}
    except:
        return {"countable":False}

def IndexMap(x,common):
    """ compare two indices: For each element of x that is in common, mark True else False """
    return np.array([(a in common) for a in x ])
    
    
def IndexSumToMatch(X,iX,iC,dims,axis,sum_dir="skip"):
    """ Pick out values from X where iX (index lables) is in iC (common/comparison index)
        Depending on the properties of the indices (countable,continous,stepsize), values along an axis are
        either sliced or (boolean)-masked [theano compatible numpy-indexing].
        If the common index is not continous, sum skipped elements and add them either left or right if sum_dir != skip
    
        X,iX tensor and index along axis
        iC common index
        dims,axis number of dimensions and axis
        sum_dir skip, left or right
    """
    slice_blueprint = [slice(None) for n in range(dims)]
    # Skipped output
    slice_blueprint[axis] = IndexMap(iX,iC)  
    O = X[slice_blueprint]
    
    if sum_dir == "skip":
        pass
    else:
        # Accumulator zero
        slice_blueprint[axis] = 0
        z = tt.zeros_like(X[slice_blueprint])
        
        # Setup loop variables, x-counter, number of summed entries, accumulator(xsum)
        nc,nsum,xsum = 0,0,z
        iCnext = iC[0]
        for nx,ix in enumerate(iX):
            if ix != iCnext:
                nsum += 1
                slice_blueprint[axis] = nx
                xsum += X[slice_blueprint]
            else:
                if nsum > 0:
                    if sum_dir == "right":
                        slice_blueprint[axis] = nc
                        O = tt.inc_subtensor(O[slice_blueprint],xsum)
                    elif sum_dir == "left" and nc != 0:
                        slice_blueprint[axis] = nc-1
                        O = tt.inc_subtensor(O[slice_blueprint],xsum)
                        
                if iCnext < iC[-1]:
                    nc += 1
                    iCnext = iC[nc]
                # Reset sum
                nsum = 0
                xsum = z
        # Edge case, left add
        if sum_dir == "left" and nsum > 0:
            slice_blueprint[axis] = nc
            O = tt.inc_subtensor(O[slice_blueprint],xsum)
            
    return O


"""
ModelParams keeps track of coordinate-ranges for Model-internal datasets

"""


class ModelParams(object):
    def __init__(self,coords={}):
        self.coords = coords
        
        self.params = {}
        
    def AddParam(self,param):
        
        pname = param.name
        if pname not in self.params.keys():
            self.params[pname] = param
        else:
            print("Param %s already exists",pname)
            
    def __getitem(self,name):
        return self.params.get(name,None)
    
    def Overlap(self):
        pass

class DimParam(object):
    """ only works if variable is a theano object 
    mimics some of xarray's functionallity wrapping theano shared_variables"""
    def __init__(self,coords,param):
        self.coords = coords
        self.param = param
        
    def Dims(self):
        return list(self.coords.keys())
        
    def DimIndex(self,dim_name):
        return self.Dims().index(dim_name)
        
    def AsModelParam(self,name):
        return ModelParam(name,self.coords,self.param)
        
#    def _SingleOutSlice(self,index):
        
        
    def Sel(self,**kwargs):
        print(kwargs)
        
        coords = OrderedDict()
        index_array = []
        for i,k in enumerate(self.coords.keys()):
            if k in kwargs.keys():
                v = kwargs[k]
                print(v)
            else:
                index_array.append(slice(None))
                coords[k] = self.coords[k]
                
                
        
        index_array = [slice(None)]*(first_index)
        index_array
    
    def iSel(self,axes):
        pass
    
    def Sum(self,axes):
        """ Sum the parameter along supplied axes.  """
        coords = OrderedDict()
        if type(axes) == list:
            index_array = []
            for i,k in enumerate(self.coords.keys()):
                if k in axes:
                    index_array.append(i)
                else:
                    coords[k] = self.coords[k]
            sparam = tt.sum(self.param,index_array)
        else:
            index = self.DimIndex(axes)
            sparam = tt.sum(self.param,index)
            coords = self.coords.copy()
            coords.pop(axes)
        return DimParam(coords,sparam)
        
    def __str__(self):
        s = "DimParam dims=%d"%(len(self.coords))
        for k,v in self.coords.items():
            s += "\n\t%s n=%d %s ... %s"%(k,len(v),v[0],v[-1])
        return s
        
    def RollByCoord(self,base_coord,offset_coord,unroll=False):
        """ Align data along base_coord axis by shifting entries along base_coord axis by offset_coord value.
            The output-tensor is extended by max(offset) along base_coord-axis
        """
        rdir = 1 if unroll == False else -1 # Roll direction
        base,offset = self.coords[base_coord],self.coords[offset_coord]
        min_roll,max_roll = min(offset),max(offset)
        nroll = max_roll-min_roll
        base_prop,offset_prop = IndexProperties(base), IndexProperties(offset)
        
        if base_prop["continous"] == True:
            # Prepare index-slice
            index = self.DimIndex(base_coord)
            index_slice = []
            roll_slice = slice(min_roll,max_roll)
            post_roll_slice = []
            for i in range(index):
                index_slice.append(slice(None))
                post_roll_slice.append(slice(None))
            index_slice.append(0)
            post_roll_slice.append(roll_slice)
            for i in range(index+1,len(self.coords)):
                index_slice.append(slice(None))
                post_roll_slice.append(slice(None))
            # Prepare offset-slice
            offset_index = self.DimIndex(offset_coord)
            offset_slice = []
            for i in range(offset_index):
                offset_slice.append(slice(None))
            offset_slice.append(0)
            for i in range(offset_index+1,len(self.coords)):
                offset_slice.append(slice(None))
            if rdir == 1:   # enlarge the param-tensor by the max roll_range
                zero_element = tt.zeros_like(self.param[index_slice])
                padding = tt.stack([zero_element]*nroll)
                padding = [self.param,padding]
                to_roll = tt.concatenate(padding,axis=index)
            else:   # roll back doesn't require padding
                to_roll = self.param
            # Roll
            for i in range(len(offset)):
                offset_slice[offset_index] = i
                r = (offset[i]-min_roll)*rdir
                if r != 0:
                    to_roll = tt.set_subtensor(to_roll[offset_slice],tt.roll(to_roll[offset_slice],r,axis=index))
            # Do the coordinate-magic on base_coord
            new_start,new_end = base[0]+np.timedelta64(min_roll,"D"),base[-1]+np.timedelta64(max_roll,"D")
            new_base_coord = pd.date_range(start=new_start,end=new_end,freq="D")
            if rdir == -1:
                new_base_coord = new_base_coord[:nroll]
                index_slice[index] = slice(0,len(new_base_coord))
                to_roll = to_roll[index_slice]
            new_coords = self.coords.copy()
            new_coords[base_coord] = new_base_coord
            
            return DimParam(new_coords,to_roll)
                
        else:
            print("Roll not possible, Base_coord is not continous",base_prop,offset_prop)
            return None
        
    def UnRollByCoord(self,base_coord,offset_coord):
        return self.RollByCoord(base_coord,offset_coord,True)

class ModelParam(DimParam):
    """ Everything is a parameter in a bayesian model """
    def __init__(self,name,coords,param,is_variable=True):
        super(ModelParam,self).__init__(coords,param)
    
        
    def Overlap(self,other,sum_missing={}):
        """ Returns overlap of both params,
            returns A overlap with B, B with A, Common coords
        """
        dims,other_dims = self.Dims(),other.Dims()
        dimS,other_dimS = set(dims),set(other_dims)
        
        dim_overlap = dimS.intersection(other_dimS)
        overlap,other_overlap = self.param, other.param
        if len(dim_overlap) > 0:
            # figure non-matching dimensions, sum over non-matching dimensions
            not_in,other_not_in = dimS-other_dimS,other_dimS-dimS
            not_index,other_not_index = list(map(self.DimIndex,not_in)),list(map(other.DimIndex,other_not_in))
            if len(not_in) > 0:
                overlap = overlap.sum(axis=not_index)
                for k in not_in:
                    dims.remove(k)
            if len(other_not_in) > 0:
                other_overlap = other_overlap.sum(axis=other_not_index)
                for k in other_not_in:
                    other_dims.remove(k) # dims, other_dims are the new indices
            
            # Transpose matching dimensions
            other_transpose = list(map(other_dims.index,dims))
            other_overlap = other_overlap.dimshuffle(other_transpose)
            
            # Reduce coordinates for both theano objects
            overlap_index = {k:self.coords[k] for k in dims}
            other_index = {other_dims[i]:other.coords[other_dims[i]] for i in other_transpose}
            
            # Do the nasty stuff
            A,B,common_index = self.Overlap_Axes(overlap,other_overlap,overlap_index,other_index,sum_missing)
            return A,B,common_index
        else:
            return None,None,None
        
    def Overlap_Axes(self,A,B,A_index,B_index,sum_missing={}):
        """ Returns theano objects A,B
        
            For each axis, compare indizes and slice inputs A,B to match each other
        """
        
        A_indexer,B_indexer,common_index = [],[],{}
        for axis,dim in enumerate(A_index.keys()):
            iA,iB = A_index[dim], B_index[dim] 
                   
            iC = np.array(sorted( set(iA).intersection(set(iB)) ))
            common_index[dim] = iC
            
            iPA,iPB = IndexProperties(iA),IndexProperties(iB)
            A_sum = sum_missing.get(dim,"skip") 
            B_sum = sum_missing.get(dim,"skip")
            
            if iPA["countable"] == iPB["countable"] and iPA["countable"] == False:
                # Simple case for non-countable indices, only skipping with a boolean mask
                A_indexer.append(IndexMap(iA,iC))
                B_indexer.append(IndexMap(iB,iC))
                
            else: # more complex case, might involve skipping/summing of elements
                iPC = IndexProperties(iC) 
                
                if iPC["continous"] == True:
                    if iPC["stepsize"] == iPA["stepsize"]:
                        A_indexer.append( slice(iA.index(iC[0]),iA.index(iC[-1])+1) )
                    else:
                        A = IndexSumToMatch(A,iA,iC,len(A_index.keys()),axis,A_sum)
                        A_indexer.append(slice(None))

                    if iPC["stepsize"] == iPB["stepsize"]:
                        B_indexer.append( slice(iB.index(iC[0]),iB.index(iC[-1])+1) )
                    else:
                        B = IndexSumToMatch(B,iB,iC,len(B_index.keys()),axis,B_sum)
                        B_indexer.append(slice(None))
                        
                else: # involves skipping/summing in A and/or B
                    
                    print(axis,iPC)
                    print("\nA",iA)
                    A = IndexSumToMatch(A,iA,iC,len(A_index.keys()),axis,A_sum)
                    A_indexer.append(slice(None))
                    
                    print("\nB",iB)
                    B = IndexSumToMatch(B,iB,iC,len(B_index.keys()),axis,B_sum)
                    B_indexer.append(slice(None))
                    
        
        return A[A_indexer],B[B_indexer],common_index        

class ObservedData(ModelParam):
    """ Holds Data, allows index-based matching of data """
    def __init__(self,name,data):
        """ data : xarray"""
        coords = OrderedDict() # xarray.DataArray.coords is not properly ordered.
        for d in data.dims:
            coords[d] = sorted(data.coords[d].values) # Make sure indices are sorted as well.
        param = theano.shared(data.sel(coords).values)
        super(ObservedData,self).__init__(name,coords,param,is_variable=False)
        
