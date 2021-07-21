import unittest

import numpy as np
import xarray as xr
import pickle
import pandas as pd
import datetime
from sys import getsizeof,path

import theano
import theano.tensor as tt

path.append("../src")
from Splines import CentripetalCatmullRomSpline_splitControls,Spline

class SplineTest(unittest.TestCase):
    pass
    
unittest.main()