import datetime

def FromNummericDate(nd):
    nd = int(nd)
    y,m,d = nd//10000,(nd//100)%100,nd%100
    dt = datetime.datetime(2000+y,m,d)
    return dt