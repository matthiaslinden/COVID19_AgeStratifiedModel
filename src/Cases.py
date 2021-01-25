import os
import datetime
import numpy as np
import pandas as pd
import xarray as xr

from Utility import FromNummericDate

def ParseSurvStatDay(dday):
    by_type = ["lab and clinical met","lab met, clinical not met","lab met, clinical undetermined"]
    lks = np.array([k for k in dday[2020].keys()],dtype="int16")
    weeks = np.arange(54*2,dtype="int16")
    sexes = ["male","female","unknown"]
    ages = np.arange(81,dtype="int8")

    d = np.zeros([len(by_type),len(lks),len(sexes),len(ages),len(weeks)],dtype="int16")

    for y,o in {2020:0,2021:53}.items():
        for ilk,lk in enumerate(lks[:]):
            dlk = dday[y].get(lk,{})
            for jtyp,typ in enumerate(by_type):
                dtyp = dlk.get(typ,{})
                for ksex,sex in enumerate(sexes):
                    dsex = dtyp.get(sex,None)
                    if dsex != None:
                        for week,dweek in dsex.items():
                            for age,data in dweek.items():
                                if type(age) == int:
                                    d[jtyp,ilk,ksex,age,week+o] += data
    return d

def ParseSurvStatDay_BL(dday):
    by_type = ["lab and clinical met","lab met, clinical not met","lab met, clinical undetermined"]
    lks = np.array([k for k in dday[2020].keys()],dtype="int16")
    bl = np.arange(1,17,dtype="int8")
    weeks = np.arange(54*2,dtype="int16")
    sexes = ["male","female","unknown"]
    ages = np.arange(81,dtype="int8")
    
    d = np.zeros([len(by_type),len(bl),len(sexes),len(ages),len(weeks)],dtype="int16")

    for y,o in {2020:0,2021:53}.items():
        for ilk,lk in enumerate(lks[:]):
            dlk = dday[y].get(lk,{})
            for jtyp,typ in enumerate(by_type):
                dtyp = dlk.get(typ,{})
                for ksex,sex in enumerate(sexes):
                    dsex = dtyp.get(sex,None)
                    if dsex != None:
                        for week,dweek in dsex.items():
                            for age,data in dweek.items():
                                if type(age) == int:
                                    d[jtyp,lk//1000-1,ksex,age,week+o] += data
    bs = xr.DataArray(d, dims=("category","BL","sex","age","week"), coords={"category":by_type,"BL":bl,"sex":sexes,"age":ages,"week":weeks})
    return bs
    
    
    
# Situation Reports' Age Structure without sex, but 80+ in 5 / 10 y groups

def RKI_Altersverteilung():
    directory = "../Data/Cases/SitRep_RKI/"
    fl = os.listdir(directory)
    
    ag10, ag5 = {},{}
    minweek,maxweek = 52,0
    for fn in fl:

        if fn[:16] == "Altersverteilung":
            nd = fn.replace(".csv","").split("_")[1]
            pdate = FromNummericDate(nd)
            df = pd.read_csv(directory+fn,sep=";")
            
            if pdate >= datetime.datetime(2020,11,24):
                #print(pdate,"weekly columns",fn)

                ags = df["Altersgruppe"]
                if len(ags) < 19:
                    data = Parse10yGroups(df)
                else:
                    data = Parse5yGroups(df)
                    ag5[pdate] = data
            else:
                print(pdate,"weekly rows",fn)

                data = ParseWeeklyRows(df)
    
    x = []
    for w in sorted(ag5.keys())[::-1]:
        d = ag5[w]
        d = d.assign_coords({"publication":w})
        if len(x) == 0:
            x = d
        else:
            x = xr.concat([x,d],"publication",fill_value=0)
    
    return ag10,x
            
def ParseWeeklyRows(df):
    pass

def Parse10yGroups(df):
    pass


def Parse5yGroups(df):
    
    def Weeks(i):
        if "_" in i:
            y_index = {2020:0,2021:53}
            y,w = map(int,i.split("_"))
            return(w+y_index[y])
        else:
            return int(i)
    
    adf = df.iloc[1:]
    adf.index = map(lambda x : int(x.replace("+","-").replace(" ","").split("-")[0]), adf["Altersgruppe"])
    del adf["Altersgruppe"]
    adf.index.name = "Altersgruppe"
    cols,idx = list(map(Weeks,adf.columns)),adf.index
    
    return xr.DataArray(adf.to_numpy(),dims=["age","week"],coords={"age":idx.to_numpy(),"week":cols})