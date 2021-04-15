import numpy as np
import xarray as xr
import pandas as pd

import datetime

from sys import getsizeof,path
path.append("../../../src")

from Utility import DateFrom6digitName

ending,deaths_rev = {},{}

# 210208
ending["210208"] = datetime.datetime(2021,2,8)
deaths_rev["210208"] = [6,16,16,24,15,21,37,23,31,36,41,37,53,42,36,43,50,45,58,57,69,59,52,62,64,56,55,67,66,55,71,80,80,67,80,82,75,81,67,69,68,89,79,95,82,75,65,87,87,93,89,88,76,79,93,81,85,79,76,60,83,73,78,76,62,58,65,52,58,53,52,48,49,56,52,47,54,47,37,34,39,33,34,40,31,28,40,30,24,23,29,17,28,26,25,20,20,16,17,20,11,15,11,17,14,20,9,10,7,8,5,9,6,11,8,8,6,4,7,2,2,2,2,1,1,2,5,2,1,2,3,3,0,1,1,1,2,2,1,1,1,0,0,0,4,0,2,1 ]

# 210209
ending["210209"] = datetime.datetime(2021,2,9)
deaths_rev["210209"] = [5,10,20,21,30,19,22,38,25,33,36,41,38,53,42,37,43,50,45,58,57,69,59,52,63,65,56,55,68,67,56,71,80,81,67,81,82,75,81,67,69,68,89,79,95,82,75,65,87,87,93,89,88,76,79,93,81,85,79,76,60,83,73,78,76,62,58,65,52,58,53,52,48,49,56,52,47,54,47,37,34,39,33,34,40,31,28,40,30,24,23,29,17,28,26,25,20,20,16,17,20,11,15,11,17,14,20,9,10,7,8,5,9,6,11,8,8,6,4,7,2,2,2,2,1,1,2,5,2,1,2,3,3,0]

# 210210 - seems to be the same as 2021-02-09
#ending["210210"] = datetime.datetime(2021,2,10)
#deaths_rev["210210"] = []

# 210211
ending["210211"] = datetime.datetime(2021,2,11)
deaths_rev["210211"] = [7,22,25,19,26,23,34,20,24,42,28,35,38,43,40,55,43,38,45,52,45,62,58,69,60,53,63,66,58,55,69,69,59,72,81,82,67,82,83,74,82,68,70,70,89,80,96,82,76,65,86,87,93,89,88,77,79,92,81,85,78,75,61,82,73,78,74,61,57,65,52,58,53,52,48,48,57,52,47,57,47,37,35,39,33,35,40,31,28,40,30,24,23,29,17,28,26,25,20,20,16,17,20,11,15,11,17,14,20,9,10,7,8,5,9,6,11,8,8,6,4,7,2,2,2,2,1,1,2,5,2,1,2,3,3,0]


# 210319
ending["210319"] = datetime.datetime(2021,3,19)
deaths_rev["210319"] = [2,2,10,10,10,11,5,13,11,12,16,16,16,9,18,9,20,21,22,18,12,8,13,7,23,11,15,17,16,19,21,21,16,28,29,36,34,32,34,25,31,35,42,27,29,50,31,39,43,51,46,58,47,42,51,58,49,68,64,71,67,55,66,68,61,60,75,76,62,73,88,84,75,89,86,74,86,73,75,73,93,84,100,85,79,70,89,87,94,90,90,77,80,94,80,86,78,78,63,84,74,82,77,64,58,73,52,59,56,55,54,47,60,56,48,60,48,37,37,39,35,35,41,32,29,40,30,24,23,29,18,30]

# 210320
ending["210320"] = datetime.datetime(2021,3,20)
deaths_rev["210320"] = [0,4,3,11,12,10,11,5,13,12,12,16,16,16,9,18,9,20,21,22,18,12,8,13,7,23,11,15,17,16,20,21,21,16,28,29,36,34,32,34,25,31,35,42,27,29,50,31,39,43,51,46,58,47,42,51,58,49,68,64,71,67,55,66,68,61,60,75,76,62,73,88,84,75,89,86,74,86,73,75,73,93,84,100,85,79,70,89,87,94,90,90,77,80,94,80,86,78,78,63,84,74,82,77,64,58,73,52,59,56,55,54,47,60,56,48,60,48,37,37,39,35,35,41,32,29,40,30,24,23,29,18,30,26,26,20,20,16,17,21,11,15,11,17,14,21,9,10,7,8,5,9,6,11,8,8,6,4,8,2,2,2,2,1,1,2,5,2,1,2,3,3,0,1,1,1,2,2,1,1,1,0,0,0,4,0,2,1]

# 210330
#ending["210330"] = datetime.datetime(2021,3,30)
#deaths_rev["210330"] =

# 210331
ending["210331"] = datetime.datetime(2021,3,31)
deaths_rev["210331"] = [1,7,9,8,7,18,11,12,10,12,10,6,9,5,16,18,13,12,6,16,12,12,16,16,17,11,19,9,22,21,23,18,13,10,13,7,23,11,15,17,16,21,21,21,16,28,29,36,34,33,35,27,32,35,42,27,29,50,31,39,43,52,47,59,47,42,52,59,49,68,64,71,67,55,66,68,63,61,75,76,62,73,89,84,75,89,87,75,87,75,76,73,93,85,101,86,79,70,90,89,94,90,90,77,80,95,80,86,78,78,63,84,74,82,78,65,58,73,52,59,56,55,54,47,60,57,48,60,48,37,37,39,35,35,41,32,29,40,30,24,23,29,18,30,26,26,20,20,16,17,21,11,15,11,17,14,21,9,10,7,8,5,9,6,11,8,8,6,4,8,8,2,2,2,2,1,1,2,5,2,1,2,3,3,0,1,1,1,2,2,1,1,1]

# 210401
ending["210401"] = datetime.datetime(2021,4,1)
deaths_rev["210401"] = [4,8,10,11,8,7,18,12,12,10,12,10,6,9,5,16,18,13,12,6,16,12,12,16,16,17,11,19,9,22,21,24,18,15,10,13,7,23,11,15,17,16,21,21,21,16,28,29,36,34,33,35,27,32,35,42,27,29,50,31,39,43,52,47,59,47,42,52,59,49,68,64,71,67,56,66,68,63,61,75,76,62,73,89,84,75,89,88,75,87,75,77,74,93,85,101,86,79,70,90,89,94,90,90,77,80,95,80,86,78,78,63,84,74,82,78,65,58,73,52,59,56,55,54,47,60,57,48,60,48,37,37,39,35,35,41,32,29,40,30,24,23,29,18,30,26,26,20,20,16,17,21,11,15,11,17,14,21,9,10,7,8,5,9,6,11,8,8,6,4,8,2,2,2,2,1,1,2,5,2,1,2,3,3,0,1,1,1,2,2,1,1,1]

# 210402
ending["210402"] = datetime.datetime(2021,4,2)
deaths_rev["210402"] = [1,8,9,10,11,8,7,18,12,12,10,12,10,6,9,5,16,19,13,12,6,16,12,12,16,16,17,11,19,9,22,21,24,18,15,10,13,7,23,11,15,17,16,21,21,21,16,28,29,36,34,33,35,27,32,35,42,27,29,50,31,39,43,52,47,59,47,42,52,59,49,68,64,71,67,56,66,68,63,61,75,76,62,73,89,84,75,89,88,75,87,75,77,74,93,85,101,86,79,70,90,89,94,90,90,77,80,95,80,86,78,78,63,84,74,82,78,65,58,73,52,59,56,55,54,47,60,57,48,60,48,37,37,39,35,35,41,32,29,40,30,24,23,29,18,30,26,26,20,20,16,17,21,11,15,11,17,14,21,9,10,7,8,5,9,6,11,8,8,6,4,8,2,2,2,2,1,1,2,5,2,1,2,3,3,0,1,1,1,2,2,1,1,1]

# 210403
ending["210403"] = datetime.datetime(2021,4,3)
deaths_rev["210403"] = [2,4,10,9,10,11,8,7,18,12,12,10,12,10,6,9,5,16,19,13,12,6,16,12,12,16,16,17,11,19,9,22,21,24,18,15,10,13,7,23,11,15,17,16,21,21,21,16,28,29,36,34,33,35,27,32,35,42,27,29,50,31,39,43]

# 210404
ending["210404"] = datetime.datetime(2021,4,4)
deaths_rev["210404"] = [1,3,5,10,9,10,11,8,7,18,12,12,10,12,10,6,9,5,16,19,13,12,6,16,12,12,16,16,17,11,19,9,22,21,24,18,15,10,13,7,23,11,15,17,16,21,21,21,16,28,29,36,34,33,35,27,32,35,42,27,29,50,31,39,43,52,47,59,47,42,52,59,49,68,64,71,67,56,66,68,63,61,75,76,62,73]

# 210405
ending["210405"] = datetime.datetime(2021,4,5)
deaths_rev["210405"] = [1,3,7,6,10,9,10,11,8,8,18,12,12,10,13,10,6,9,5,16,19,13,12,6,16,12,12,16,16,17,11,19,9,22,22,24,18,15,10,13,7,23,11,15,17,16,21,21,21,16,28,29,36,34,33,35,27,32,35,42,27,29,50,31,39,43,52,47,59,47,42,52,59,49,68,64,71,67,56,66,69,63,62,75,76,62,73,89,84,75,89,88,75,87,75,77,74,93,85,101,86,79,70,90,89,94,90,90,77,80,95,80,86,78,78,63,84,74,82,78,65,58,73,52,59,56,55,54,47,60,57,48,60,48,37,37,39,35,35,41,32,29,40,30,24,23,29,18,30,26,26,20,20,16,17,21,11,15,11,17,14,21,9,10,7,8,5,9,6,11,8,8,6,4,8,2,2,2,2,1,1,2,5,2,1,2,3,3,0,1,1,1,2,2,1,1,1]

# 210406
ending["210406"] = datetime.datetime(2021,4,6)
deaths_rev["210406"] = [5,7,9,11,7,12,12,11,12,9,8,19,12,12,11,13,10,6,9,5,16,19,14,12,6,16,12,12,16,16,17,11,19,9,22,22,24,18,15,10,13,7,23,11,15,17,16,21,21,21,16,28,29,36,34,33,35,27,32,35,42,27,29,50,31,39,43,52,47,59,47,42,52,59,49,68,64,71,67,56,66,69,63,61,75,76,62,73,89,84,75,89,88,75,87,75,77,74,93,85,101,86,79,70,90,89,94,90,90,77,80,95,80,86,78,78,63,84,74,82,78,65,58,73,52,59,56,55,54,47,60,57,48,60,48,37,37,39,35,35,41,32,29,40,30,24,23,29,18,30,26,26,20,20,16,17,21,11,15,11,17,14,21,9,10,7,8,5,9,6,11,8,8,6,8,2,2,2,2,1,1,2,5,2,1,2,3,3,0,1,1,1,1,2,2,1,1,1]

# 210407
ending["210407"] = datetime.datetime(2021,4,7)
deaths_rev["210407"] = [3,12,11,14,14,10,13,12,12,13,10,8,19,12,13,12,13,10,6,9,5,16,19,14,12,6,16,12,12,16,16,17,11,19,9,22,22,24,18,15,10,13,7,23,11,15,17,16,21,21,21,16,29,29,36,34,33,35,27,32,35,42,27,29,50,31,39,44,53,47,59,47,42,52,59,49,68,64,71,67,56,66,69,63,61,75,76,62,73,89,84,75,89,88,75,87,75,77,74,93,85,101,86,79,70,90,89,94,90,90,78,80,95,80,86,77,79,63,84,74,82,78,65,59,73,52,59,56,55,54,47,60,57,48,60,48,37,37,39,35,35,41,32,29,40,30,24,23,29]

# 210408
ending["210408"] = datetime.datetime(2021,4,8)
deaths_rev["210408"] = [4,16,19,11,18,15,13,14,12,12,13,10,8,19,12,14,12,13,10,6,9,5,16,19,14,12,6,16,13,12,16,16,17,11,19,9,22,22,24,18,15,10,13,7,23,11,15,17,16,21,21,22,16,29,29,36,34,33,35,27,32,35,42,27,29,50,31,39,44,53,47,59,47,42,52,59,49,68,64,71,67,56,66,69,63,61,75,76,62,73,89,84,75,89,88,75,87,75,77,74,93,85,101,86,79,70,90,89,94,90,90,78,80,95,80,86,77,79,63,84,74,82,78,65,59,73,52,59,56,55,54,47,60,57,48,60,48,37,37,39,35,35,41,32,29,40,30,24,23,29,18,30,26,26,20,20,16,17,21,11,15,11,17,14,21,9,10,7,8,5,9,6,11,8,8,6,4,8,2,2,2,2,1,1,2,5,2,1,2,3,3,0,1,1,1,2,2,1,1,1]

# 210409
ending["210409"] = datetime.datetime(2021,4,9)
deaths_rev["210409"] = [2,8,18,20,11,18,16,15,15,12,13,13,13,10,19,12,14,14,13,10,6,9,5,16,19,14,12,6,16,13,12,17,16,17,11,19,9,22,22,24,18,15,10,13,7,23,12,16,17,16,21,21,22,16,29,29,36,34,33,35,27,32,35,42,27,29,50,31,39,44,53,47,59,47,42,52,59,49,68,64,71,67,56,66,69,63,61,75,76,62,73,89,84,75,89,89,75,87,77,77,76,93,85,101,86,79,70,90,90,94,91,90,78,80,95,80,86,77,79,63,84,74,82,78,65,59,73]

# 210410
ending["210410"] = datetime.datetime(2021,4,10)
deaths_rev["210410"] = [2,7,9,18,21,11,18,16,16,16,12,14,13,13,10,19,12,14,14,13,10,6,9,5,16,19,14,12,6,16,13,12,17,16,17,11,19,9,22,22,24,18,15,10,13,7,23,12,16,17,16,21,21,22,16,29,29,36,34,33,35,27,32,35,42,27,29,50,31,39,44,53,47,59,47,42,52,59,49,68,64,71,67,56,66,69,63,61,75,76,62,73,89,84,75,89,89,75,87,77,77,76,93,85,101,86,79,70,90,90,94,91,90,78,80,95,80,86,77,79,63,84,74,82,78,65,59,73,52,59,56,55,54,47,60,57,48,60,48,37,37,39,35,35,41,32,29,40,30,24,23,29,18,30,26,26,20,20,16,17,21,11,15,11]

# 210411
ending["210411"] = datetime.datetime(2021,4,11)
deaths_rev["210411"] = [0,7,12,11,19,21,12,18,17,16,16,12,14,13,13,10,19,12,14,14,13,10,6,9,5,16,19,14,12,6,16,13,12,17,16,17,11,19,9,22,22,24,18,15,10,13,7,23,12,16,17,16,21,21,22,16,29,29,36,34,33,35,27,32,35,42,27,29,50,31,39,44,53,47,59,47,42,52,59,49,68,64,71,67,56,66,69,63,61,75,76,62,73,89,84,75,89,89,75,87,77,77,76,93,85,101,86,79,70,90,90,94,91,90,78,80,95,80,86,77,79,63,84,74,82,78,65,59,73,52,59,56,55,54,47,60,57,48,60,48,37,37,39,35,35,41,32,29,40,30,24,23,29,18,30,26,26,20,20,16,17,21]

#  210412
ending["210412"] = datetime.datetime(2021,4,12)
deaths_rev["210412"] = [3,5,9,14,14,19,21,12,18,17,17,16,12,14,14,13,10,20,12,14,14,13,10,6,9,5,16,19,14,12,6,16,13,12,17,16,17,11,19,9,22,22,24,18,15,10,13,7,23,12,16,17,16,21,21,22,16,29,29,36,34,33,35,27,32,35,42,27,29,50,31,39,44,53,47,59,47,42,52,59,49,68,64,71,67,56,66,69,63,61,75,76,62,73,89,84,75,89,89,75,87,77,77,76,93,85,101,86,79,70,90,90,94,91,90,78,80,95,80,86,77,79,63]

#  210413
ending["210413"] = datetime.datetime(2021,4,13)
deaths_rev["210413"] = [2,11,12,14,17,15,20,21,14,18,18,17,16,13,14,14,13,10,21,12,14,14,14,10,6,9,5,17,20,14,12,6,16,14,12,17,16,17,11,19,9,22,23,24,18,14,10,13,7,23,12,16,17,16,21,21,22,16,29,29,36,34,33,35,27,32,35,42,27,29,50,31,39,44,53,47,59,47,42,52,59,49,68,64,71,67,56,66,69,63,61,75,76,62,73]

#  210414
ending["210414"] = datetime.datetime(2021,4,14)
deaths_rev["210414"] = [3,9,13,13,19,17,16,20,21,15,18,19,17,18,13,14,14,13,11,21,12,15,14,14,10,6,9,5,17,20,14,12,6,16,14,12,17,16,17,11,19,9,22,23,24,18,14,10,13,7,23,12,16,17,16,21,21,22,16,29,29,36,34,33,35,27,32,35,42,27,29,50,31,39,44,53,47,59,47,42,52,59,49,68,64,71,67,56,66,69,63,61,75,76,62,73,89,84,75,89,89,75,75,87,77,77,76,93,85,101,86,79,70,90,90,94,91,90,78,80,95,80,86,77,79,63,84,74,82,78,65,65,59,73,52,59,56,55,54,47,60,57,48,60,48,37,39,41]

#  210415
ending["210415"] = datetime.datetime(2021,4,15)
deaths_rev["210415"] = [2,7,11,13,13,21,18,16,21,21,16,18,20,17,17,13,14,14,13,11,21,12,15,14,14,10,6,9,5,17,20,14,12,7,16,14,12,17,16,17,11,19,9,22,23,24,18,14,10,13,7,23,12,16,17,16,21,21,22,16,29,29,36,34,33,35,27,32,35,42,27,29,50,31,39,44,53,47,59,47,42,52,59,49,68,64,71,67,56,66,69,63,61,75,76,62,73,89,84,75,89,89]


for k,v in deaths_rev.items():
	print(k,v[:40])






