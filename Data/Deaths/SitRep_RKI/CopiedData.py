import numpy as np
import xarray as xr
import pandas as pd

from sys import getsizeof,path
path.append("../../../src")

from Utility import DateFrom6digitName

def SitRepDeathsAgeGroupsSex(fn):
    pass



def main():
    """ Generate *.csv files """
    SitRepDeathsAgeGroupsSex("test.csv")
    
if __name__ == '__main__':
    main()