import datetime
import re

def RKI_AG_to_int(x):
    return int(x.replace("+","-").split("-")[0])


re_date = re.compile(r"\D(\d{8})\D")

def DateFrom6digitName(nd):
    nd = int(nd)
    y,m,d = nd//10000,(nd//100)%100,nd%100
    dt = datetime.datetime(2000+y,m,d)
    return dt
    
def DateFrom8digitName(s):
    ds = re_date.findall(s)
    if len(ds) > 0:
        ds = ds[0]
        y,m,d = map(int,(ds[:4],ds[4:6],ds[6:],))
        return datetime.datetime(y,m,d)
    return None