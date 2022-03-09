#!/usr/bin/env python3.7
#coding:utf-8

import datetime
import os
import wget

sdir = "https://www.lgl.bayern.de/gesundheit/infektionsschutz/infektionskrankheiten_a_z/coronavirus/karte_coronavirus/fallzahlen_archiv/"
#20210118_faelle_alter_geschlecht.csv"


def fetch(d,monday):
    files = os.listdir()
    startdates = {}#{"_todesfalle":datetime.date(2020,1,1)}
    startdates["_faelle_alter_geschlecht"] = datetime.date(2020,1,1)
    startdates["_faelle_alter_geschlecht_tote"] = datetime.date(2020,1,1)
    startdates["_krankheitsschwere"] = datetime.date(2021,9,6)
    startdates["todesfalle"] = datetime.date(2022,3,1)
    startdates["_todesfaelle_nach_sterbewoche"] = datetime.date(2022,2,14)
#    startdates["_variantenLK_MW"] = datetime.date(2021,10,11)
 #   startdates["_variantenLK"] = datetime.date(2021,5,1)
    
    for i,ft in enumerate(startdates.keys()):
        f = d+ft+".csv"
        if f not in files:
           if startdates[ft] <= monday :# and not (d[:4] == "2020" and i == 0):
#                print(f)
                url = sdir+f
                wget.download(url)

def fetch2(d):
    files = os.listdir()
    startdates = {"_todesfaelle_nach_sterbewoche": datetime.date(2022,3,1)}
    for i,ft in enumerate(startdates.keys()):
        f = d+ft+".csv"
        if f not in files:
            url = sdir+f
            wget.download(url)

def main():
    today = datetime.date.today()
    monday = today-datetime.timedelta(days=today.weekday())
    
    for i in range(40):
        fstr = "%d%02d%02d"%(monday.year,monday.month,monday.day)
        fetch(fstr,monday)
        monday = monday-datetime.timedelta(days=7)

    for i in range(40):
        today = today-datetime.timedelta(days=1)
        fstr = "%d%02d%02d"%(today.year,today.month,today.day)
        fetch2(fstr)

if __name__ == "__main__":
    main()