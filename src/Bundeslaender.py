import datetime
import pandas as pd
import numpy as np
import xarray as xr
import time

bls = {1:"Schleswig-Holstein",2:"Hamburg",3:"Niedersachsen",4:"Bremen",5:"Nordrhein-Westfalen",6:"Hessen",7:"Rheinland-Pfalz",8:"Baden-Württemberg"}
bls.update({9:"Bayern",10:"Saarland",11:"Berlin",12:"Brandenburg",13:"Mecklenburg-Vorpommern",14:"Sachsen",15:"Sachsen-Anhalt",16:"Thüringen"})

blids = {1:"SH",2:"HH",3:"NI",4:"HB",5:"NW",6:"HE",7:"RP",8:"BW",9:"BY",10:"SL",11:"BE",12:"BB",13:"MV",14:"SN",15:"ST",16:"TH"}

class Bundeslaender(object):
    """ German Bundeslaender"""
    def __init__(self):
        self.blIDs = {1:"SH",2:"HH",3:"NI",4:"HB",5:"NW",6:"HE",7:"RP",8:"BW",9:"BY",10:"SL",11:"BE",12:"BB",13:"MV",14:"SN",15:"ST",16:"TH"}
        self.blNames = {1:"Schleswig-Holstein",2:"Hamburg",3:"Niedersachsen",4:"Bremen",5:"Nordrhein-Westfalen",6:"Hessen",7:"Rheinland-Pfalz",8:"Baden-Württemberg"}
        self.blNames.update({9:"Bayern",10:"Saarland",11:"Berlin",12:"Brandenburg",13:"Mecklenburg-Vorpommern",14:"Sachsen",15:"Sachsen-Anhalt",16:"Thüringen"})


class Feiertage(object):
    def __init__(self,blids=None):
        self.easter = {}
        self.easter[2017] = datetime.datetime(2017,4,16)
        self.easter[2018] = datetime.datetime(2018,4,1)
        self.easter[2019] = datetime.datetime(2019,4,21)
        self.easter[2020] = datetime.datetime(2020,4,13)
        self.easter[2021] = datetime.datetime(2021,4,5)
        self.easter[2022] = datetime.datetime(2022,4,18)
        self.easter[2023] = datetime.datetime(2023,4,10)
        self.easter[2024] = datetime.datetime(2024,4,1)
        self.easter[2025] = datetime.datetime(2025,4,21)
        self.easter[2026] = datetime.datetime(2026,4,6)
        self.easter[2027] = datetime.datetime(2027,3,29)
        self.easter[2028] = datetime.datetime(2028,4,17)
        self.easter[2029] = datetime.datetime(2029,4,2)
        self.easter[2030] = datetime.datetime(2030,4,22)
        
        self.years = {}
        self.feiertage = {}
        
        self.feiertage["Neujahr"] = self.FixedDate(1,1)
        self.feiertage["3Könige"] = self.FixedDate(1,6)
        self.feiertage["Frauentag"] = self.FixedDate(3,8)
        self.feiertage["Gründonnerstag"] = self.EasterOffset(-3)
        self.feiertage["KFreitag"] = self.EasterOffset(-2)
        self.feiertage["Ostern"] = self.EasterOffset()
        self.feiertage["Ostermontag"] = self.EasterOffset(1)
        self.feiertage["Himmelfahrt"] = self.EasterOffset(39)
        self.feiertage["Pfingstsonntag"] = self.EasterOffset(49)
        self.feiertage["Pfingstmontag"] = self.EasterOffset(50)
        self.feiertage["Fronleichnam"] = self.EasterOffset(60)
        self.feiertage["MariäHimmelfahrt"] = self.FixedDate(8,8)
        self.feiertage["Weltkindertag"] = self.FixedDate(9,20)
        self.feiertage["DeutscheEinheit"] = self.FixedDate(10,3)
        self.feiertage["Reformationstag"] = self.FixedDate(10,31)
        self.feiertage["Allerheiligen"] = self.FixedDate(11,1)
        self.feiertage["BBTag"] = self.BBTag
        self.feiertage["1Weihnachten"] = self.FixedDate(12,25)
        self.feiertage["2Weihnachten"] = self.FixedDate(12,26)
        
#        self.feiertage[""] = self.FixedDate(,)
        
        self.bundeslaender = {}
        self.bundeslaender["BW"] = ["Neujahr","3Könige","KFreitag","Ostermontag","1Mai","Himmelfahrt","Pfingstmontag","Fronleichnam","DeutscheEinheit","Allerheiligen","1Weihnachten","2Weihnachten"]
        self.bundeslaender["BY"] = ["Neujahr","3Könige","KFreitag","Ostermontag","1Mai","Himmelfahrt","Pfingstmontag","Fronleichnam","MariäHimmelfahrt","DeutscheEinheit","Allerheiligen","1Weihnachten","2Weihnachten"]
        self.bundeslaender["BE"] = ["Neujahr","Frauentag","KFreitag","Ostermontag","1Mai","Himmelfahrt","Pfingstmontag","DeutscheEinheit","1Weihnachten","2Weihnachten"]
        self.bundeslaender["BB"] = ["Neujahr","KFreitag","Ostern","Ostermontag","1Mai","Himmelfahrt","Pfingstsonntag","Pfingstmontag","DeutscheEinheit","Reformatonstag","1Weihnachten","2Weihnachten"]
        self.bundeslaender["HB"] = ["Neujahr","KFreitag","Ostermontag","1Mai","Himmelfahrt","Pfingstmontag","DeutscheEinheit","Reformatonstag","1Weihnachten","2Weihnachten"]
        self.bundeslaender["HH"] = ["Neujahr","KFreitag","Ostermontag","1Mai","Himmelfahrt","Pfingstmontag","DeutscheEinheit","Reformatonstag","1Weihnachten","2Weihnachten"]
        self.bundeslaender["HE"] = ["Neujahr","KFreitag","Ostersonntag","Ostermontag","1Mai","Himmelfahrt","Pfingstsonntag","Pfingstmontag","DeutscheEinheit","1Weihnachten","2Weihnachten"]
        self.bundeslaender["MV"] = ["Neujahr","KFreitag","Ostermontag","1Mai","Himmelfahrt","Pfingstmontag","DeutscheEinheit","Reformatonstag","1Weihnachten","2Weihnachten"]
        self.bundeslaender["NI"] = ["Neujahr","KFreitag","Ostermontag","1Mai","Himmelfahrt","Pfingstmontag","DeutscheEinheit","Reformatonstag","1Weihnachten","2Weihnachten"]
        self.bundeslaender["NW"] = ["Neujahr","KFreitag","Ostermontag","1Mai","Himmelfahrt","Pfingstmontag","Fronleichnam","DeutscheEinheit","Allerheiligen","1Weihnachten","2Weihnachten"]
        self.bundeslaender["RP"] = ["Neujahr","KFreitag","Ostermontag","1Mai","Himmelfahrt","Pfingstmontag","Fronleichnam","DeutscheEinheit","Allerheiligen","1Weihnachten","2Weihnachten"]
        self.bundeslaender["SL"] = ["Neujahr","KFreitag","Ostermontag","1Mai","Himmelfahrt","Pfingstmontag","Fronleichnam","MariäHimmelfahrt","DeutscheEinheit","Allerheiligen","1Weihnachten","2Weihnachten"]
        self.bundeslaender["SN"] = ["Neujahr","KFreitag","Ostermontag","1Mai","Himmelfahrt","Pfingstmontag","DeutscheEinheit","Reformatonstag","BBTag","1Weihnachten","2Weihnachten"]
        self.bundeslaender["ST"] = ["Neujahr","3Könige","KFreitag","Ostermontag","1Mai","Himmelfahrt","Pfingstmontag","DeutscheEinheit","Reformatonstag","BBTag","1Weihnachten","2Weihnachten"]
        self.bundeslaender["SH"] = ["Neujahr","KFreitag","Ostermontag","1Mai","Himmelfahrt","Pfingstmontag","DeutscheEinheit","Reformatonstag","1Weihnachten","2Weihnachten"]
        self.bundeslaender["TH"] = ["Neujahr","KFreitag","Ostermontag","1Mai","Himmelfahrt","Pfingstmontag","Weltkindertag","DeutscheEinheit","Reformatonstag","1Weihnachten","2Weihnachten"]
        
        if blids == None:
            blids = Bundeslaender().blIDs
        
        self.by_blids = {}
        for i,bl in blids.items():
            self.by_blids[i] = self.bundeslaender[bl]
            
        
    def FixedDate(self,month,day):
        return lambda year : datetime.datetime(year,month,day)
        
    def EasterOffset(self,offset=0):
        return lambda year : self.easter.get(year) + datetime.timedelta(days=offset)
        
    def BBTag(self,year):
        """ wednesday befor nov 23"""
        nov23 = datetime.datetime(year,11,23)
        offset = -((nov23.weekday()+4)%7)   -1
        return nov23 + datetime.timedelta(days=offset)
        
    def GetYear(self,year):
        feiertage = self.years.get(year,{})
        if len(feiertage) == 0:
            for name,generator in self.feiertage.items():
                feiertage[name] = generator(year)
            self.years[year] = feiertage
        return feiertage
        
    def IndexArray(self,startdate,enddate):
        drange = pd.date_range(startdate,enddate,freq="D")
        work = drange.dayofweek < 4
        friday = drange.dayofweek == 4
        saturday = drange.dayofweek == 5
        sunday = drange.dayofweek == 6
        
        days = np.stack([work,friday,saturday,sunday])
        
        xdays = xr.DataArray(days,dims=["status","date"],coords={"status":["workday","friday","saturday","sunday/holiday"],"date":drange})
        return xdays
        
    def BundeslandArray(self,startdate,enddate):
        """ Returns xarray with a status (workday,friday,saturday,sunday/holiday) for every date for each Bundesland (BL index)"""
        startyear,endyear = startdate.year,enddate.year
        years = {}
        for y in range(startyear,endyear+1):
            years[y] = self.GetYear(y)
        xdays = self.IndexArray(startdate,enddate)
        
        bldays = xdays.values
        bldays = bldays.reshape([1,bldays.shape[0],bldays.shape[1]])
        bldays = np.repeat(bldays,len(self.by_blids),0)
        
        # Holiday-ify
        for bi,bl in enumerate(self.by_blids.keys()):
            days = self.by_blids[bl]
            for y,holidays in years.items():
                for name,at in holidays.items():
                    if name in days:
                        if at >= startdate and at <= enddate:
                            iat = (at-startdate).days
                            bldays[bi,:,iat] = [False,False,False,True]
        
        xbldays = xr.DataArray(bldays,dims=["BL","status","date"],coords={"BL":list(self.by_blids.keys()),"status":xdays.coords["status"],"date":xdays.coords["date"]})
        
        return xbldays

def main():
    feiertage = Feiertage()
    
#    print(feiertage.GetYear(2020))
 #   print(feiertage.GetYear(2021))
    
    t1 = time.time()
    fdays = feiertage.BundeslandArray(datetime.datetime(2019,11,3),datetime.datetime(2022,4,3))
    t2 = time.time()
    print("in %.3f"%(t2-t1))

if __name__ == "__main__":
    main()