import numpy as np
import xarray as xr
import pandas as pd

import datetime

from sys import getsizeof,path
path.append("../../../src")

from Utility import DateFrom6digitName

def DeathsPerAG():
    mdeaths = {}
    
    # April
#    mdeaths[datetime.date(2020,4,24)] = {#  This is sum over previous
 #       "male" : [   0,   0,   0,   0,  0, 171, 357, 865,1300, 338,   0],
  #      "female":[   0,   0,   0,   0,  0,  58, 118, 388,1106, 605,   0]}
#    mdeaths[datetime.date(2020,4,25)] = {
 #       "male" : [   0,   0,   0,   0,  33, 131, 370, 882,1337, 356,   3],
  #      "female":[   0,   0,   0,   0,   8,  41, 120, 400,1145, 604,  27]}
#    mdeaths[datetime.date(2020,4,26)] = {
 #       "male" : [   0,   0,   0,   4,  32, 132, 380, 900,1368, 369,   3],
  #      "female":[   0,   0,   0,   0,   8,  41, 124, 404,1185, 620,  29]}
        
    mdeaths[datetime.date(2020,4,27)] = {
        "male" : [   0,   1,   3,   5,  35, 137, 386, 917,1399, 376,   3],
        "female":[   1,   0,   2,   4,   9,  42, 129, 414,1206, 643,  32]}
    mdeaths[datetime.date(2020,4,28)] = {
        "male" : [   0,   1,   4,   8,  35, 142, 394, 937,1437, 382,   4],
        "female":[   1,   0,   2,   4,   9,  44, 132, 431,1250, 658,  32]}
    mdeaths[datetime.date(2020,4,29)] = {
        "male" : [   0,   1,   4,   9,  35, 152, 411, 957,1479, 390,   4],
        "female":[   1,   0,   2,   5,  10,  47, 138, 446,1296, 689,  33]}
    mdeaths[datetime.date(2020,4,30)] = {
        "male" : [   0,   1,   4,   9,  36, 157, 425, 976,1518, 404,   4],
        "female":[   1,   0,   2,   5,  10,  48, 139, 455,1340, 709,  35]}
    
    # May
    mdeaths[datetime.date(2020,5,1)] = {
        "male" : [   0,   1,   4,   9,  36, 161, 435,1001,1570, 425,   4],
        "female":[   1,   0,   2,   5,  11,  50, 145, 466,1376, 734,  36]}
    mdeaths[datetime.date(2020,5,2)] = {
        "male" : [   0,   1,   4,   9,  36, 164, 442,1018,1588, 430,   4],
        "female":[   1,   0,   2,   5,  11,  51, 150, 473,1393, 746,  37]}
    mdeaths[datetime.date(2020,5,3)] = {
        "male" : [   0,   1,   4,   9,  37, 166, 444,1026,1599, 433,   4],
        "female":[   1,   0,   2,   5,  11,  54, 152, 482,1416, 756,  37]}
    mdeaths[datetime.date(2020,5,4)] = {
        "male" : [   0,   1,   4,   9,  37, 167, 446,1035,1609, 437,   4],
        "female":[   1,   0,   2,   5,  11,  54, 152, 484,1427, 759,  37]}
    mdeaths[datetime.date(2020,5,5)] = {
        "male" : [   0,   1,   5,  10,  37, 172, 454,1052,1645, 443,   4],
        "female":[   1,   0,   2,   5,  11,  56, 155, 495,1456, 779,  38]}
    mdeaths[datetime.date(2020,5,6)] = {
        "male" : [   0,   1,   5,  11,  37, 176, 466,1073,1681, 453,   4],
        "female":[   1,   0,   2,   5,  12,  57, 161, 507,1489, 806,  41]}
    mdeaths[datetime.date(2020,5,7)] = {
        "male" : [   0,   1,   5,  11,  37, 180, 477,1085,1708, 458,   4],
        "female":[   1,   0,   2,   6,  12,  58, 165, 517,1526, 816,  41]}
    mdeaths[datetime.date(2020,5,8)] = {
        "male" : [   0,   1,   5,  12,  39, 184, 488,1106,1734, 469,   4],
        "female":[   1,   0,   2,   6,  13,  60, 172, 527,1556, 840,  41]}
    mdeaths[datetime.date(2020,5,9)] = {
        "male" : [   0,   1,   5,  12,  39, 185, 495,1121,1761, 476,   5],
        "female":[   1,   0,   2,   6,  13,  61, 176, 536,1573, 854,  41]}
    mdeaths[datetime.date(2020,5,10)] = {
        "male" : [   0,   1,   5,  12,  39, 187, 499,1125,1768, 476,   5],
        "female":[   1,   0,   2,   6,  13,  61, 176, 536,1577, 860,  41]}
    mdeaths[datetime.date(2020,5,11)] = {
        "male" : [   0,   1,   5,  12,  39, 186, 502,1129,1773, 479,   5],
        "female":[   1,   0,   2,   6,  13,  61, 176, 538,1582, 860,  41]}
    mdeaths[datetime.date(2020,5,11)] = {
        "male" : [   0,   1,   5,  12,  39, 186, 502,1129,1773, 479,   5],
        "female":[   1,   0,   2,   6,  13,  61, 176, 538,1582, 860,  41]}
    mdeaths[datetime.date(2020,5,12)] = {
        "male" : [   0,   1,   5,  13,  40, 194, 504,1146,1801, 494,   5],
        "female":[   1,   0,   2,   6,  14,  62, 177, 544,1603, 874,  41]}
    mdeaths[datetime.date(2020,5,13)] = {
        "male" : [   0,   1,   6,  14,  40, 195, 515,1161,1822, 499,   5],
        "female":[   1,   0,   2,   6,  14,  62, 180, 553,1628, 883,  41]}
    mdeaths[datetime.date(2020,5,14)] = {
        "male" : [   0,   1,   6,  13,  40, 195, 520,1174,1838, 501,   5],
        "female":[   1,   0,   2,   6,  14,  62, 182, 563,1652, 901,  41]}
    mdeaths[datetime.date(2020,5,15)] = {
        "male" : [   0,   1,   6,  13,  40, 199, 534,1181,1861, 506,   5],
        "female":[   1,   0,   2,   6,  14,  66, 185, 570,1668, 917,  43]}
    mdeaths[datetime.date(2020,5,16)] = {
        "male" : [   0,   1,   6,  13,  40, 201, 537,1191,1868, 509,   5],
        "female":[   1,   0,   2,   6,  15,  68, 187, 573,1680, 928,  44]}
    mdeaths[datetime.date(2020,5,17)] = {
        "male" : [   0,   1,   7,  13,  41, 201, 540,1199,1873, 511,   5],
        "female":[   1,   0,   2,   6,  15,  68, 187, 575,1686, 933,  44]}
    mdeaths[datetime.date(2020,5,18)] = {
        "male" : [   0,   2,   6,  13,  41, 203, 541,1200,1877, 514,   5],
        "female":[   1,   0,   2,   6,  15,  67, 188, 579,1689, 936,  45]}
    mdeaths[datetime.date(2020,5,19)] = {
        "male" : [   0,   2,   6,  13,  42, 204, 548,1212,1891, 515,   5],
        "female":[   1,   0,   2,   6,  15,  68, 194, 582,1704, 947,  45]}
    mdeaths[datetime.date(2020,5,20)] = {
        "male" : [   0,   2,   6,  13,  42, 205, 554,1225,1911, 520,   5],
        "female":[   1,   0,   2,   6,  16,  69, 197, 589,1723, 954,  45]}
    mdeaths[datetime.date(2020,5,21)] = {
        "male" : [   0,   2,   6,  13,  42, 206, 558,1233,1929, 520,   5],
        "female":[   1,   0,   2,   6,  16,  70, 199, 594,1734, 954,  45]}
    mdeaths[datetime.date(2020,5,22)] = {
        "male" : [   0,   2,   6,  14,  43, 206, 561,1235,1935, 521,   5],
        "female":[   1,   0,   2,   6,  17,  70, 199, 597,1738, 966,  45]}
    mdeaths[datetime.date(2020,5,23)] = {
        "male" : [   0,   2,   6,  14,  45, 209, 561,1243,1945, 522,   5],
        "female":[   1,   0,   2,   6,  17,  70, 200, 601,1743, 974,  45]}
    mdeaths[datetime.date(2020,5,24)] = {
        "male" : [   0,   2,   6,  14,  45, 211, 565,1248,1949, 524,   5],
        "female":[   1,   0,   2,   6,  17,  71, 201, 602,1750, 978,  45]}
    mdeaths[datetime.date(2020,5,25)] = {
        "male" : [   0,   2,   6,  14,  45, 211, 565,1249,1951, 524,   5],
        "female":[   1,   0,   2,   6,  17,  72, 202, 602,1753, 980,  45]}
    mdeaths[datetime.date(2020,5,26)] = {
        "male" : [   0,   2,   6,  14,  46, 211, 571,1254,1960, 528,   5],
        "female":[   1,   0,   3,   6,  17,  71, 204, 605,1766, 982,  45]}
    mdeaths[datetime.date(2020,5,27)] = {
        "male" : [   0,   2,   6,  14,  47, 213, 574,1261,1969, 528,   5],
        "female":[   1,   0,   3,   6,  17,  71, 205, 607,1780, 990,  45]}
    mdeaths[datetime.date(2020,5,28)] = {
        "male" : [   0,   2,   6,  14,  49, 216, 582,1272,1982, 530,   5],
        "female":[   1,   0,   3,   6,  18,  71, 205, 609,1789,1001,  45]}
    mdeaths[datetime.date(2020,5,29)] = {
        "male" : [   0,   2,   6,  14,  49, 217, 586,1280,1990, 535,   5],
        "female":[   1,   0,   3,   6,  18,  71, 207, 612,1794,1005,  45]}
    mdeaths[datetime.date(2020,5,30)] = {
        "male" : [   0,   2,   6,  14,  49, 218, 588,1286,1998, 538,   5],
        "female":[   1,   0,   3,   6,  18,  71, 211, 616,1803,1007,  45]}
    mdeaths[datetime.date(2020,5,31)] = {
        "male" : [   0,   2,   6,  14,  49, 218, 590,1286,1999, 539,   5],
        "female":[   1,   0,   3,   6,  18,  72, 211, 616,1807,1008,  45]}
    
    # June
    mdeaths[datetime.date(2020,6,1)] = {
        "male" : [   0,   2,   6,  14,  49, 218, 591,1287,2003, 540,   5],
        "female":[   1,   0,   3,   6,  18,  72, 211, 618,1808,1009,  45]}
    mdeaths[datetime.date(2020,6,2)] = {
        "male" : [   0,   2,   6,  14,  49, 218, 592,1290,2002, 541,   5],
        "female":[   1,   0,   3,   6,  18,  72, 210, 620,1811,1012,  45]}
    mdeaths[datetime.date(2020,6,3)] = {
        "male" : [   0,   2,   6,  15,  49, 218, 594,1298,2009, 543,   5],
        "female":[   1,   0,   3,   6,  18,  72, 211, 620,1818,1013,  45]}
    mdeaths[datetime.date(2020,6,4)] = {
        "male" : [   0,   2,   6,  15,  49, 220, 600,1300,2018, 543,   5],
        "female":[   1,   0,   3,   6,  18,  72, 211, 624,1823,1015,  45]}
    mdeaths[datetime.date(2020,6,5)] = {
        "male" : [   0,   2,   6,  15,  49, 221, 600,1307,2020, 545,   5],
        "female":[   1,   0,   3,   6,  18,  76, 211, 627,1829,1022,  45]}
    mdeaths[datetime.date(2020,6,6)] = {
        "male" : [   0,   2,   6,  15,  49, 221, 603,1310,2028, 545,   5],
        "female":[   1,   0,   3,   6,  19,  76, 210, 631,1836,1030,  45]}
    mdeaths[datetime.date(2020,6,7)] = {
        "male" : [   0,   2,   6,  15,  49, 222, 604,1312,2034, 546,   6],
        "female":[   1,   0,   3,   6,  19,  76, 211, 635,1839,1032,  45]}
    mdeaths[datetime.date(2020,6,8)] = {
        "male" : [   0,   2,   6,  15,  49, 222, 605,1313,2035, 546,   6],
        "female":[   1,   0,   3,   6,  19,  76, 211, 636,1839,1034,  45]}
    mdeaths[datetime.date(2020,6,9)] = {
        "male" : [   0,   2,   6,  15,  49, 222, 610,1316,2047, 549,   6],
        "female":[   1,   0,   3,   6,  19,  77, 211, 636,1849,1037,  45]}
    mdeaths[datetime.date(2020,6,10)] = {
        "male" : [   0,   2,   6,  15,  49, 223, 612,1319,2048, 550,   6],
        "female":[   1,   0,   3,   6,  19,  80, 213, 639,1850,1039,  45]}
    mdeaths[datetime.date(2020,6,11)] = {
        "male" : [   0,   2,   6,  16,  49, 222, 612,1325,2056, 553,   5],
        "female":[   1,   0,   3,   6,  19,  80, 215, 644,1852,1039,  45]}
    mdeaths[datetime.date(2020,6,12)] = {
        "male" : [   0,   2,   6,  17,  49, 222, 611,1325,2058, 554,   5],
        "female":[   1,   0,   3,   6,  19,  80, 215, 647,1853,1040,  45]}
    mdeaths[datetime.date(2020,6,13)] = {
        "male" : [   0,   2,   6,  17,  49, 225, 614,1327,2063, 555,   5],
        "female":[   1,   0,   3,   6,  20,  80, 216, 650,1852,1040,  45]}
    mdeaths[datetime.date(2020,6,14)] = {
        "male" : [   0,   2,   6,  17,  49, 225, 614,1327,2065, 555,   5],
        "female":[   1,   0,   3,   6,  20,  81, 217, 651,1853,1040,  45]}
    mdeaths[datetime.date(2020,6,15)] = {
        "male" : [   0,   2,   6,  17,  49, 225, 614,1329,2065, 555,   5],
        "female":[   1,   0,   3,   6,  20,  81, 217, 651,1855,1040,  45]}
    mdeaths[datetime.date(2020,6,16)] = {
        "male" : [   0,   2,   6,  17,  49, 226, 615,1329,2066, 555,   5],
        "female":[   1,   0,   3,   6,  20,  81, 220, 651,1856,1042,  45]}
    mdeaths[datetime.date(2020,6,17)] = {
        "male" : [   0,   2,   6,  17,  49, 227, 618,1333,2071, 556,   6],
        "female":[   1,   0,   3,   6,  20,  82, 221, 653,1859,1050,  45]}
    mdeaths[datetime.date(2020,6,18)] = {
        "male" : [   0,   2,   6,  17,  49, 228, 621,1341,2076, 556,   6],
        "female":[   1,   0,   3,   6,  20,  82, 221, 653,1862,1056,  45]}
    mdeaths[datetime.date(2020,6,19)] = {
        "male" : [   0,   2,   6,  17,  49, 228, 622,1341,2081, 556,   6],
        "female":[   1,   0,   3,   6,  20,  82, 221, 655,1865,1061,  45]}
    mdeaths[datetime.date(2020,6,20)] = {
        "male" : [   0,   2,   6,  17,  49, 228, 624,1343,2085, 556,   6],
        "female":[   1,   0,   3,   6,  20,  83, 221, 655,1866,1062,  45]}
    mdeaths[datetime.date(2020,6,21)] = {
        "male" : [   0,   2,   6,  17,  49, 228, 624,1343,2084, 556,   6],
        "female":[   1,   0,   3,   6,  20,  83, 221, 655,1866,1062,  45]}
    mdeaths[datetime.date(2020,6,22)] = {
        "male" : [   0,   2,   6,  17,  49, 228, 624,1346,2085, 556,   6],
        "female":[   1,   0,   3,   6,  20,  83, 221, 655,1866,1062,  45]}
    mdeaths[datetime.date(2020,6,23)] = {
        "male" : [   0,   2,   6,  17,  49, 228, 626,1346,2086, 555,   6],
        "female":[   1,   0,   3,   6,  20,  84, 222, 657,1868,1063,  45]}
    mdeaths[datetime.date(2020,6,24)] = {
        "male" : [   0,   2,   6,  17,  50, 229, 627,1346,2090, 559,   6],
        "female":[   1,   0,   3,   6,  20,  84, 223, 657,1872,1066,  45]}
    mdeaths[datetime.date(2020,6,25)] = {
        "male" : [   0,   2,   7,  17,  50, 230, 627,1351,2092, 560,   6],
        "female":[   1,   0,   3,   6,  22,  84, 223, 658,1873,1065,  45]}
    mdeaths[datetime.date(2020,6,26)] = {
        "male" : [   0,   2,   7,  17,  50, 232, 627,1356,2093, 561,   6],
        "female":[   1,   0,   3,   6,  22,  85, 223, 659,1878,1070,  45]}
    mdeaths[datetime.date(2020,6,27)] = {
        "male" : [   0,   2,   7,  17,  50, 233, 628,1357,2093, 562,   6],
        "female":[   1,   0,   3,   6,  22,  84, 224, 659,1882,1068,  45]}
    mdeaths[datetime.date(2020,6,28)] = {
        "male" : [   0,   2,   7,  17,  50, 233, 629,1357,2093, 562,   6],
        "female":[   1,   0,   3,   6,  22,  84, 224, 659,1884,1068,  45]}
    mdeaths[datetime.date(2020,6,29)] = {
        "male" : [   0,   2,   7,  17,  50, 233, 630,1359,2094, 562,   6],
        "female":[   1,   0,   3,   6,  22,  84, 224, 659,1884,1068,  45]}
    mdeaths[datetime.date(2020,6,30)] = {
        "male" : [   0,   2,   7,  17,  50, 233, 631,1359,2094, 562,   6],
        "female":[   1,   0,   3,   6,  22,  84, 226, 660,1888,1072,  45]}
    
    # July
    mdeaths[datetime.date(2020,7,1)] = {
        "male" : [   0,   2,   7,  17,  51, 233, 632,1362,2097, 562,   6],
        "female":[   1,   0,   3,   6,  21,  84, 226, 662,1890,1074,  44]}
    mdeaths[datetime.date(2020,7,2)] = {
        "male" : [   0,   2,   7,  17,  51, 233, 631,1363,2100, 562,   6],
        "female":[   1,   0,   3,   6,  21,  84, 226, 663,1894,1075,  44]}
    mdeaths[datetime.date(2020,7,3)] = {
        "male" : [   0,   2,   7,  17,  51, 233, 633,1365,2102, 564,   6],
        "female":[   1,   0,   3,   6,  21,  85, 226, 663,1894,1075,  44]}
    mdeaths[datetime.date(2020,7,4)] = {
        "male" : [   0,   2,   7,  17,  52, 234, 635,1366,2101, 563,   6],
        "female":[   1,   0,   3,   6,  22,  85, 226, 663,1896,1077,  44]}
    mdeaths[datetime.date(2020,7,5)] = {
        "male" : [   0,   2,   6,  17,  52, 235, 635,1366,2101, 564,   7],
        "female":[   1,   0,   3,   6,  22,  85, 227, 663,1896,1076,  44]}
    mdeaths[datetime.date(2020,7,6)] = {
        "male" : [   0,   2,   6,  17,  53, 234, 635,1367,2101, 564,   6],
        "female":[   1,   0,   3,   6,  22,  85, 227, 664,1897,1076,  44]}
    mdeaths[datetime.date(2020,7,7)] = {
        "male" : [   0,   2,   6,  17,  53, 234, 638,1369,2102, 564,   7],
        "female":[   1,   0,   3,   6,  22,  85, 227, 664,1899,1076,  44]}
    mdeaths[datetime.date(2020,7,8)] = {
        "male" : [   0,   2,   6,  17,  53, 235, 639,1370,2101, 565,   7],
        "female":[   1,   0,   3,   6,  22,  85, 229, 666,1901,1079,  44]}
    mdeaths[datetime.date(2020,7,9)] = {
        "male" : [   0,   2,   6,  17,  53, 236, 641,1372,2101, 565,   7],
        "female":[   1,   0,   3,   6,  22,  85, 229, 667,1904,1082,  44]}
    mdeaths[datetime.date(2020,7,10)] = {
        "male" : [   0,   2,   6,  17,  53, 236, 641,1373,2102, 566,   7],
        "female":[   1,   0,   3,   6,  22,  85, 230, 667,1904,1084,  44]}
    mdeaths[datetime.date(2020,7,11)] = {
        "male" : [   0,   2,   6,  17,  54, 236, 642,1373,2104, 566,   7],
        "female":[   1,   0,   3,   6,  22,  85, 230, 668,1904,1085,  44]}
    mdeaths[datetime.date(2020,7,12)] = {
        "male" : [   0,   2,   6,  17,  54, 236, 642,1373,2104, 567,   7],
        "female":[   1,   0,   3,   6,  22,  85, 231, 669,1904,1085,  44]}
    mdeaths[datetime.date(2020,7,13)] = {
        "male" : [   0,   2,   6,  17,  54, 236, 642,1373,2104, 567,   7],
        "female":[   1,   0,   3,   6,  22,  85, 231, 669,1905,1085,  44]}
    mdeaths[datetime.date(2020,7,14)] = {
        "male" : [   0,   2,   6,  17,  54, 236, 642,1374,2105, 567,   7],
        "female":[   1,   0,   3,   6,  22,  85, 232, 670,1905,1085,  44]}
    mdeaths[datetime.date(2020,7,15)] = {
        "male" : [   0,   2,   6,  17,  54, 236, 642,1374,2106, 567,   7],
        "female":[   1,   0,   3,   6,  22,  85, 232, 670,1906,1086,  44]}
    mdeaths[datetime.date(2020,7,16)] = {
        "male" : [   0,   2,   6,  17,  54, 236, 644,1377,2106, 567,   7],
        "female":[   1,   0,   3,   6,  22,  85, 232, 670,1907,1087,  44]}
    mdeaths[datetime.date(2020,7,17)] = {
        "male" : [   0,   2,   6,  17,  54, 236, 644,1378,2108, 567,   6],
        "female":[   1,   0,   3,   6,  22,  85, 232, 671,1908,1087,  44]}
    mdeaths[datetime.date(2020,7,18)] = {
        "male" : [   0,   2,   6,  17,  54, 236, 645,1379,2108, 567,   6],
        "female":[   1,   0,   3,   6,  22,  85, 232, 671,1908,1086,  44]}
    mdeaths[datetime.date(2020,7,19)] = {
        "male" : [   0,   2,   6,  17,  54, 236, 645,1379,2108, 567,   6],
        "female":[   1,   0,   3,   6,  22,  85, 232, 671,1908,1087,  44]}
    mdeaths[datetime.date(2020,7,20)] = {
        "male" : [   0,   2,   6,  17,  54, 237, 645,1379,2109, 567,   6],
        "female":[   1,   0,   3,   6,  22,  85, 232, 671,1908,1087,  44]}
    mdeaths[datetime.date(2020,7,21)] = {
        "male" : [   0,   2,   6,  17,  54, 237, 645,1378,2112, 567,   6],
        "female":[   1,   0,   3,   6,  22,  85, 232, 671,1910,1087,  44]}
    mdeaths[datetime.date(2020,7,22)] = {
        "male" : [   0,   2,   6,  17,  54, 238, 645,1380,2112, 568,   6],
        "female":[   1,   0,   3,   6,  22,  85, 232, 670,1912,1087,  44]}
    mdeaths[datetime.date(2020,7,23)] = {
        "male" : [   0,   2,   6,  17,  54, 239, 645,1381,2113, 567,   6],
        "female":[   1,   0,   3,   6,  22,  86, 232, 670,1914,1088,  44]}
    mdeaths[datetime.date(2020,7,24)] = {
        "male" : [   0,   2,   6,  17,  54, 239, 646,1381,2114, 570,   6],
        "female":[   1,   0,   3,   6,  22,  86, 233, 670,1917,1089,  44]}
    mdeaths[datetime.date(2020,7,25)] = {
        "male" : [   0,   2,   6,  17,  56, 240, 647,1382,2114, 570,   6],
        "female":[   1,   0,   3,   6,  22,  86, 233, 670,1917,1091,  44]}
    mdeaths[datetime.date(2020,7,26)] = {
        "male" : [   0,   2,   6,  17,  56, 240, 647,1382,2114, 570,   6],
        "female":[   1,   0,   3,   6,  22,  86, 233, 670,1917,1091,  44]}
    mdeaths[datetime.date(2020,7,27)] = {
        "male" : [   0,   2,   6,  17,  56, 240, 647,1382,2114, 570,   6],
        "female":[   1,   0,   3,   6,  22,  86, 233, 670,1917,1091,  44]}
    mdeaths[datetime.date(2020,7,28)] = {
        "male" : [   0,   2,   6,  17,  56, 240, 648,1382,2116, 571,   6],
        "female":[   1,   0,   3,   6,  22,  86, 233, 670,1917,1091,  44]}
    mdeaths[datetime.date(2020,7,29)] = {
        "male" : [   0,   2,   6,  17,  57, 241, 648,1382,2117, 572,   6],
        "female":[   1,   0,   3,   6,  22,  86, 235, 670,1917,1091,  44]}
    mdeaths[datetime.date(2020,7,29)] = {
        "male" : [   0,   2,   6,  17,  57, 241, 648,1382,2117, 572,   6],
        "female":[   1,   0,   3,   6,  22,  86, 235, 670,1917,1091,  44]}
    mdeaths[datetime.date(2020,7,30)] = {
        "male" : [   0,   2,   6,  17,  57, 240, 648,1384,2117, 573,   6],
        "female":[   1,   0,   3,   6,  22,  86, 235, 671,1919,1092,  44]}
    # No Data on 2020-07-31
    
    # August
    mdeaths[datetime.date(2020,8,1)] = {
        "male" : [   0,   2,   6,  17,  57, 240, 650,1386,2120, 574,   6],
        "female":[   1,   0,   3,   6,  22,  87, 235, 672,1922,1093,  44]}
    mdeaths[datetime.date(2020,8,2)] = {
        "male" : [   0,   2,   6,  16,  57, 240, 650,1387,2118, 572,   6],
        "female":[   1,   0,   3,   6,  22,  87, 235, 672,1919,1093,  44]}
    mdeaths[datetime.date(2020,8,3)] = {
        "male" : [   0,   2,   6,  17,  57, 240, 650,1387,2120, 573,   6],
        "female":[   1,   0,   3,   6,  22,  87, 235, 672,1921,1094,  44]}
    mdeaths[datetime.date(2020,8,4)] = {
        "male" : [   0,   2,   6,  17,  57, 240, 655,1388,2123, 573,   6],
        "female":[   1,   0,   3,   6,  22,  87, 235, 672,1922,1094,  44]}
    mdeaths[datetime.date(2020,8,5)] = {
        "male" : [   0,   2,   6,  17,  57, 240, 655,1390,2126, 574,   6],
        "female":[   1,   0,   3,   6,  22,  87, 235, 673,1924,1095,  44]}
    mdeaths[datetime.date(2020,8,6)] = {
        "male" : [   0,   2,   6,  17,  57, 241, 655,1391,2128, 574,   6],
        "female":[   1,   0,   3,   6,  22,  87, 235, 673,1926,1096,  44]}
    mdeaths[datetime.date(2020,8,7)] = {
        "male" : [   0,   2,   6,  17,  57, 241, 656,1391,2129, 577,   6],
        "female":[   1,   0,   3,   6,  22,  87, 235, 675,1927,1098,  44]}
    mdeaths[datetime.date(2020,8,8)] = {
        "male" : [   0,   2,   6,  17,  57, 241, 656,1393,2134, 578,   6],
        "female":[   1,   0,   3,   6,  22,  87, 235, 676,1928,1098,  44]}
    mdeaths[datetime.date(2020,8,9)] = {
        "male" : [   0,   2,   6,  17,  57, 241, 656,1393,2135, 578,   6],
        "female":[   1,   0,   3,   6,  22,  87, 235, 676,1928,1098,  44]}
    mdeaths[datetime.date(2020,8,10)] = {
        "male" : [   0,   2,   6,  17,  57, 241, 656,1393,2136, 578,   6],
        "female":[   1,   0,   3,   6,  22,  87, 235, 676,1928,1098,  44]}
    mdeaths[datetime.date(2020,8,11)] = {
        "male" : [   0,   2,   7,  17,  57, 241, 656,1395,2137, 578,   6],
        "female":[   1,   0,   3,   6,  22,  88, 235, 676,1928,1098,  44]}
    mdeaths[datetime.date(2020,8,12)] = {
        "male" : [   0,   2,   7,  17,  57, 242, 656,1397,2137, 579,   6],
        "female":[   1,   0,   3,   6,  22,  88, 235, 676,1930,1098,  44]}
    mdeaths[datetime.date(2020,8,13)] = {
        "male" : [   0,   2,   7,  17,  57, 242, 656,1398,2138, 579,   6],
        "female":[   1,   0,   3,   6,  22,  88, 235, 676,1932,1098,  44]}
    mdeaths[datetime.date(2020,8,14)] = {
        "male" : [   0,   2,   7,  17,  57, 242, 658,1401,2141, 580,   6],
        "female":[   1,   0,   3,   6,  22,  88, 235, 677,1935,1099,  44]}
    mdeaths[datetime.date(2020,8,15)] = {
        "male" : [   0,   2,   7,  17,  57, 242, 658,1402,2144, 580,   6],
        "female":[   1,   0,   3,   6,  22,  88, 235, 677,1937,1099,  44]}
    mdeaths[datetime.date(2020,8,16)] = {
        "male" : [   0,   2,   7,  17,  57, 242, 658,1402,2144, 580,   6],
        "female":[   1,   0,   3,   6,  22,  88, 235, 677,1937,1099,  44]}
    mdeaths[datetime.date(2020,8,17)] = {
        "male" : [   0,   2,   7,  17,  57, 242, 658,1402,2144, 580,   6],
        "female":[   1,   0,   3,   6,  22,  88, 235, 677,1937,1100,  44]}
    mdeaths[datetime.date(2020,8,18)] = {
        "male" : [   0,   2,   7,  17,  57, 242, 658,1402,2144, 582,   6],
        "female":[   1,   0,   3,   6,  22,  88, 235, 678,1938,1100,  44]}
    mdeaths[datetime.date(2020,8,19)] = {
        "male" : [   0,   2,   7,  17,  57, 242, 658,1402,2146, 583,   6],
        "female":[   1,   0,   3,   6,  22,  88, 235, 678,1940,1101,  44]}
    mdeaths[datetime.date(2020,8,20)] = {
        "male" : [   0,   2,   7,  17,  57, 242, 658,1403,2148, 584,   6],
        "female":[   1,   0,   3,   6,  22,  89, 235, 678,1943,1102,  45]}
    mdeaths[datetime.date(2020,8,21)] = {
        "male" : [   0,   2,   7,  17,  58, 242, 658,1403,2152, 585,   6],
        "female":[   1,   0,   3,   6,  22,  89, 235, 679,1944,1102,  45]}
    mdeaths[datetime.date(2020,8,22)] = {
        "male" : [   0,   2,   7,  17,  58, 243, 659,1403,2152, 585,   6],
        "female":[   1,   0,   3,   6,  22,  89, 235, 680,1946,1103,  46]}
    mdeaths[datetime.date(2020,8,23)] = {
        "male" : [   0,   2,   7,  17,  59, 243, 659,1403,2152, 585,   6],
        "female":[   1,   0,   3,   6,  22,  89, 235, 680,1947,1103,  46]}
    mdeaths[datetime.date(2020,8,24)] = {
        "male" : [   0,   2,   7,  17,  59, 243, 660,1403,2153, 585,   6],
        "female":[   1,   0,   3,   6,  22,  89, 235, 680,1947,1104,  46]}
    mdeaths[datetime.date(2020,8,25)] = {
        "male" : [   0,   2,   7,  17,  59, 243, 660,1406,2153, 585,   6],
        "female":[   1,   0,   3,   6,  22,  89, 235, 681,1948,1104,  46]}
    mdeaths[datetime.date(2020,8,26)] = {
        "male" : [   0,   2,   7,  17,  59, 243, 661,1407,2152, 585,   6],
        "female":[   1,   0,   3,   6,  22,  90, 235, 681,1948,1105,  46]}
    mdeaths[datetime.date(2020,8,27)] = {
        "male" : [   0,   2,   7,  17,  59, 243, 664,1408,2151, 586,   6],
        "female":[   1,   0,   3,   6,  22,  90, 235, 681,1949,1105,  46]}
    mdeaths[datetime.date(2020,8,28)] = {
        "male" : [   0,   2,   7,  17,  59, 244, 664,1409,2151, 586,   6],
        "female":[   1,   0,   3,   6,  22,  90, 236, 681,1949,1105,  46]}
    mdeaths[datetime.date(2020,8,29)] = {
        "male" : [   0,   2,   7,  17,  59, 244, 663,1408,2152, 587,   6],
        "female":[   1,   0,   3,   6,  22,  90, 237, 680,1950,1105,  46]}
    mdeaths[datetime.date(2020,8,30)] = {
        "male" : [   0,   2,   7,  17,  59, 245, 663,1409,2155, 587,   6],
        "female":[   1,   0,   3,   6,  22,  90, 237, 680,1950,1105,  46]}
    mdeaths[datetime.date(2020,8,31)] = {
        "male" : [   0,   2,   7,  18,  59, 244, 664,1409,2155, 587,   6],
        "female":[   1,   0,   3,   6,  22,  90, 237, 680,1952,1105,  46]}
    
    # September
    mdeaths[datetime.date(2020,9,1)] = {
        "male" : [   0,   2,   7,  18,  59, 246, 664,1410,2157, 587,   6],
        "female":[   1,   0,   3,   6,  22,  90, 237, 680,1952,1105,  46]}  
    mdeaths[datetime.date(2020,9,2)] = {
        "male" : [   0,   1,   7,  18,  59, 246, 667,1414,2157, 588,   6],
        "female":[   1,   0,   3,   6,  22,  90, 237, 680,1954,1106,  46]}
    mdeaths[datetime.date(2020,9,3)] = {
        "male" : [   0,   1,   7,  18,  59, 247, 668,1415,2157, 588,   6],
        "female":[   1,   0,   3,   6,  22,  91, 240, 681,1954,1106,  46]}
    # No Data on 2020-09-04
    mdeaths[datetime.date(2020,9,5)] = {
        "male" : [   0,   1,   7,  18,  59, 248, 670,1416,2157, 587,   6],
        "female":[   1,   0,   3,   6,  22,  91, 239, 681,1956,1106,  46]}
    mdeaths[datetime.date(2020,9,6)] = {
        "male" : [   0,   1,   7,  18,  59, 248, 670,1416,2157, 587,   6],
        "female":[   1,   0,   3,   6,  22,  91, 239, 681,1957,1106,  46]}
    mdeaths[datetime.date(2020,9,7)] = {
        "male" : [   0,   1,   7,  18,  59, 248, 670,1416,2157, 587,   6],
        "female":[   1,   0,   3,   6,  22,  91, 239, 681,1957,1106,  46]}
    mdeaths[datetime.date(2020,9,8)] = {
        "male" : [   0,   1,   7,  18,  59, 248, 669,1418,2158, 587,   6],
        "female":[   1,   0,   3,   7,  22,  92, 239, 681,1957,1106,  46]}
    mdeaths[datetime.date(2020,9,9)] = {
        "male" : [   0,   1,   7,  18,  59, 248, 670,1422,2158, 587,   6],
        "female":[   1,   0,   3,   7,  22,  92, 239, 683,1959,1106,  46]}
    mdeaths[datetime.date(2020,9,10)] = {
        "male" : [   0,   1,   7,  18,  59, 249, 670,1423,2158, 587,   6],
        "female":[   1,   0,   3,   7,  22,  92, 239, 683,1959,1107,  46]}
    mdeaths[datetime.date(2020,9,11)] = {
        "male" : [   0,   1,   7,  18,  59, 249, 670,1424,2158, 587,   6],
        "female":[   1,   0,   3,   7,  22,  91, 239, 683,1960,1107,  46]}
    mdeaths[datetime.date(2020,9,12)] = {
        "male" : [   0,   1,   7,  18,  59, 249, 670,1425,2159, 587,   6],
        "female":[   1,   0,   3,   7,  23,  92, 240, 683,1960,1107,  46]}
    mdeaths[datetime.date(2020,9,13)] = {
        "male" : [   0,   1,   7,  18,  59, 249, 670,1425,2159, 588,   6],
        "female":[   1,   0,   3,   7,  23,  92, 240, 683,1961,1107,  46]}
    # No more daily deaths after 13.09.2020
    mdeaths[datetime.date(2020,9,15)] = {
        "male" : [   0,   1,   7,  18,  59, 251, 670,1427,2162, 589,   6],
        "female":[   1,   0,   3,   7,  23,  93, 241, 683,1962,1109,  46]}
    mdeaths[datetime.date(2020,9,22)] = {
        "male" : [   0,   1,   7,  18,  59, 253, 673,1430,2173, 591,   6],
        "female":[   1,   0,   3,   8,  23,  94, 241, 690,1964,1111,  46]}
    mdeaths[datetime.date(2020,9,29)] = {
        "male" : [   0,   1,   7,  18,  60, 255, 682,1438,2188, 597,   7],
        "female":[   1,   0,   3,   8,  23,  94, 241, 700,1976,1122,  46]}
    
    # October
    mdeaths[datetime.date(2020,10,6)] = {
        "male" : [   0,   1,   7,  18,  60, 263, 683,1445,2209, 602,   7],
        "female":[   1,   0,   3,   9,  24,  95, 241, 704,1995,1129,  46]}
    mdeaths[datetime.date(2020,10,6)] = {
        "male" : [   0,   1,   7,  18,  60, 263, 683,1445,2209, 602,   7],
        "female":[   1,   0,   3,   9,  24,  95, 241, 704,1995,1129,  46]}
    mdeaths[datetime.date(2020,10,13)] = {
        "male" : [   0,   1,   8,  18,  60, 265, 691,1467,2226, 610,   7],
        "female":[   1,   0,   3,   8,  24,  96, 244, 708,2006,1139,  46]}
    mdeaths[datetime.date(2020,10,20)] = {
        "male" : [   0,   1,   9,  19,  60, 270, 701,1493,2285, 625,   7],
        "female":[   1,   0,   3,   9,  25,  98, 246, 719,2053,1158,  46]}
    mdeaths[datetime.date(2020,10,27)] = {
        "male" : [   0,   1,  11,  19,  62, 271, 716,1527,2337, 647,   8],
        "female":[   1,   0,   3,   9,  25, 100, 258, 758,2114,1196,  47]}
    
    # November
    mdeaths[datetime.date(2020,11,3)] = {
        "male" : [   0,   1,  11,  21,  67, 286, 742,1594,2478, 708,   8],
        "female":[   1,   0,   3,   9,  30, 101, 268, 775,2223,1273,  51]}
    mdeaths[datetime.date(2020,11,10)] = {
        "male" : [   0,   1,  11,  23,  70, 297, 790,1706,2696, 767,   9],
        "female":[   1,   0,   5,   9,  31, 114, 282, 829,2394,1401,  58]}
    mdeaths[datetime.date(2020,11,17)] = {
        "male" : [   1,   3,  10,  24,  76, 324, 840,1873,3058, 876,  12],
        "female":[   2,   0,   4,  12,  37, 120, 311, 906,2672,1575,  65]}
    mdeaths[datetime.date(2020,11,24)] = {
        "male" : [   1,   3,  13,  27,  90, 352, 931,2070,3449,1000,  15],
        "female":[   2,   0,   5,  13,  40, 131, 339,1012,3006,1773,  74]}
    
    # December  - NO actual 100+ any more...
    mdeaths[datetime.date(2020,12,1)] = {
        "male" : [   2,   3,  14,  27, 100, 391,1044,2357,3929,1206,  15],
        "female":[   4,   0,   6,  15,  46, 149, 391,1189,3525,2124,  74]}
    mdeaths[datetime.date(2020,12,8)] = {
        "male" : [   2,   3,  15,  29, 106, 427,1167,2666,4573,1400,  15],
        "female":[   5,   0,   9,  17,  47, 168, 468,1381,4165,2577,  74]}
    mdeaths[datetime.date(2020,12,15)] = {
        "male" : [   1,   3,  17,  30, 121, 480,1318,3039,5327,1647,  15],
        "female":[   7,   1,  10,  20,  53, 187, 524,1607,4933,3022,  74]}
    mdeaths[datetime.date(2020,12,22)] = {
        "male" : [   4,   4,  17,  40, 131, 555,1537,3548,6408,2012,  15],
        "female":[   8,   1,  11,  24,  66, 206, 620,1920,6003,3760,  74]}
    mdeaths[datetime.date(2020,12,29)] = {
        "male" : [   3,   3,  19,  43, 142, 621,1735,3997,7381,2330,  15],
        "female":[   7,   0,  10,  24,  71, 240, 701,2180,6952,4376,  74]}
    
    # Jan 2021
    mdeaths[datetime.date(2021,1,5)] = {
        "male" : [   4,   4,  20,  45, 156, 688,1934,4553,8411,2730,  0],
        "female":[   9,   0,  13,  26,  77, 271, 803,2458,8060,5190,  0]}
    mdeaths[datetime.date(2021,1,12)] = {
        "male" : [   4,   3,  22,  49, 168, 788,2217,5247,9907,3215,  0],
        "female":[   7,   0,  14,  27,  85, 312, 933,2841,9498,6149,  0]}
    mdeaths[datetime.date(2021,1,19)] = {
        "male" : [   4,   3,  25,  55, 178, 883,2520,5962,11292,3692,  0],
        "female":[   6,   0,  14,  29,  90, 349,1069,3237,10922,7182,  0]}
    mdeaths[datetime.date(2021,1,26)] = {
        "male" : [   3,   2,  27,  58, 197, 968,2759,6568,12520,4151,  0],
        "female":[   7,   0,  14,  33, 101, 400,1185,3608,12210,8021,  0]}
    
    # Feb 2021
    mdeaths[datetime.date(2021,2,2)] = {
        "male" : [   3,   2,  27,  60, 215,1037,3033,7128,13618,4558,  0],
        "female":[   8,   0,  18,  33, 104, 431,1298,3951,13414,8851,  0]}
    mdeaths[datetime.date(2021,2,9)] = {
        "male" : [   2,   2,  27,  62, 232,1105,3255,7619,14572,4880,  0],
        "female":[   6,   0,  19,  30, 110, 460,1391,4230,14376,9570,  0]}
    mdeaths[datetime.date(2021,2,16)] = {
        "male" : [   2,   2,  28,  65, 242,1178,3449,8056,15373, 5160,  0],
        "female":[   6,   0,  19,  32, 111, 489,1483,4474,15150,10084,  0]}
    mdeaths[datetime.date(2021,2,22)] = {
        "male" : [   2,   3,  27,  68, 248,1234,3606,8392,15988, 5354,  0],
        "female":[   5,   0,  20,  33, 117, 508,1562,4872,15782,10487,  0]}
    
    # March 2021
    mdeaths[datetime.date(2021,3,2)] = {
        "male" : [   3,   3,  28,  72, 256,1279,3740,8666,16475, 5494,  0],
        "female":[   5,   0,  20,  38, 120, 524,1614,4846,16250,10818,  0]}
    mdeaths[datetime.date(2021,3,9)] = {
        "male" : [   3,   3,  28,  75, 265,1323,3860,8906,16890, 5605,  0],
        "female":[   5,   0,  20,  42, 129, 542,1656,4981,16615,11032,  0]}
    mdeaths[datetime.date(2021,3,16)] = {
        "male" : [   2,   3,  30,  84, 268,1353,3960,9120,17228, 5698,  0],
        "female":[   5,   0,  20,  49, 130, 558,1719,5094,16923,11201,  0]}
    mdeaths[datetime.date(2021,3,22)] = {
        "male" : [   2,   3,  31,  87, 276,1397,4047,9315,17499, 5780,  0],
        "female":[   6,   0,  21,  50, 137, 578,1778,5197,17199,11349,  0]}
    mdeaths[datetime.date(2021,3,30)] = {
        "male" : [   3,   3,  32,  90, 285,1433,4146,9473,17743, 5863,  0],
        "female":[   7,   0,  21,  51, 144, 599,1808,5288,17420,11472,  0]}
    
    # April 2021
    mdeaths[datetime.date(2021,4,6)] = {
        "male" : [   4,   4,  32,  93, 293,1475,4222,9625,17989, 5909,  0],
        "female":[   8,   2,  21,  56, 148, 610,1853,5372,17621,11553,  0]}

    mdeaths[datetime.date(2021,4,13)] = {
        "male" : [   4,   4,  35, 102, 312,1535,4383,9869,18361, 6002,  0],
        "female":[   8,   1,  22,  59, 158, 645,1921,5530,17909,11677,  0]}

    mdeaths[datetime.date(2021,4,20)] = {
        "male" : [   5,   5,  38, 108, 335,1587,4561,10131,18697, 6072,  0],
        "female":[   8,   1,  23,  61, 165, 673,1986, 5669,18164,11803,  0]}

    mdeaths[datetime.date(2021,4,27)] = {
        "male" : [   3,   5,  42, 115, 348,1678,4726,10441,18984, 6152,  0],
        "female":[   8,   2,  24,  63, 172, 705,2067, 5852,18438,11928,  0]}

    # Mai 2021
    mdeaths[datetime.date(2021,5,4)] = {
        "male" : [   3,   4,  42, 122, 366,1753,4914,10712,19269, 6233,  0],
        "female":[   8,   2,  26,  66, 177, 735,2149, 6034,18723,12040,  0]}

    mdeaths[datetime.date(2021,5,11)] = {
        "male" : [   4,   4,  44, 133, 386,1837,5068,11003,19543, 6278,  0],
        "female":[   8,   3,  26,  68, 188, 755,2205, 6184,18979,12172,  0]}

    mdeaths[datetime.date(2021,5,18)] = {
        "male" : [   4,   5,  46, 140, 406,1905,5195,11243,19771, 6330,  0],
        "female":[   8,   3,  27,  71, 196, 777,2264, 6321,19170,12275,  0]}

    mdeaths[datetime.date(2021,5,25)] = {
        "male" : [   4,   5,  46, 144, 424,1962,5340,11430,19949, 6394,  0],
        "female":[   8,   3,  27,  74, 204, 803,2319, 6441,19312,12346,  0]}
    
    # Juni 2021
    mdeaths[datetime.date(2021,6,1)] = {
        "male" : [   3,   5,  50, 148, 443,2030,5469,11623,20156, 6447,  0],
        "female":[   8,   4,  27,  75, 211, 827,2386, 6563,19478,12422,  0]}

    mdeaths[datetime.date(2021,6,8)] = {
        "male" : [   3,   5,  50, 153, 452,2070,5568,11763,20296, 6488,  0],
        "female":[   8,   4,  28,  76, 217, 843,2423, 6656,19620,12485,  0]}

    mdeaths[datetime.date(2021,6,15)] = {
        "male" : [   3,   5,  52, 155, 458,2115,5634,11869,20394, 6510,  0],
        "female":[   9,   4,  28,  76, 220, 861,2453, 6695,19699,12535,  0]}

    mdeaths[datetime.date(2021,6,22)] = {
        "male" : [   4,   6,  53, 156, 467,2144,5686,11952,20489, 6540,  0],
        "female":[  10,   4,  29,  77, 226, 873,2477, 6741,19794,12582,  0]}

    kdates = sorted(mdeaths.keys())
    kages = [0,10,20,30,40,50,60,70,80,90,100]
    kag = ["%02d-%02d"%(k,k+9) for k in kages][:-1]+["100+"]
    ksex = ["male","female"]
    
    d = np.zeros( (len(kdates),2,len(kages)) ,dtype = "int32")
    for dn,dt in enumerate(kdates):
        for sm,s in enumerate(ksex):
            for ak,a in enumerate(kages):
                d[dn,sm,ak] = mdeaths[dt][s][ak]
    
    print(np.prod(d.shape),"Datapoints")
    
    
#    mages = pd.MultiIndex.from_tuples(list(zip(kages,kag)), names=["start","string"])
    ar = xr.DataArray(d,dims=("date","sex","age",),coords={"age":kages,"sex":ksex,"date":kdates }) 
    
    
    return ar

def main():
    print(DeathsPerAG())
    
if __name__ == '__main__':
    main()