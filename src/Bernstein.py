

import theano
import theano.tensor as tt

def BinomialCoefficient(n,k):
    
    # Hope that's not tooo inefficient, but theano will figure that out.
    return tt.gamma(n+1)/(tt.gamma(k+1)*tt.gamma(n-k+1))

def Bernstein(deg=4,n=128):
    x = tt.arange(n,dtype="float64")/(n-1)
    
    def fn(a,b):
        return (1-x)**(b-a) * x**a * BinomialCoefficient(b,a)
    
    result,_ = theano.scan(fn=fn,outputs_info=None,sequences=[tt.arange(deg+1,dtype="int64")],non_sequences=deg)
    return result