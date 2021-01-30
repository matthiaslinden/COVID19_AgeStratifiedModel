import datetime
import re


re_date = re.compile(r"\D(\d{8})\D")

def DateFrom6digitName(nd):
    nd = int(nd)
    y,m,d = nd//10000,(nd//100)%100,nd%100
    dt = datetime.datetime(2000+y,m,d)
    return dt
    
def DateFrom8digitName(s):
    ds = re_date.findall(s)[0]
    y,m,d = map(int,(ds[:4],ds[4:6],ds[6:],))
    return datetime.datetime(y,m,d)