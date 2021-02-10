#!/usr/bin/env python3.7
#coding:utf-8

import datetime
import os
import wget

sdir = "https://www.lgl.bayern.de/gesundheit/infektionsschutz/infektionskrankheiten_a_z/coronavirus/karte_coronavirus/fallzahlen_archiv/"
#20210118_faelle_alter_geschlecht.csv"


def fetch(d):
    files = os.listdir()
    for i,ft in enumerate(["_todesfalle","_faelle_alter_geschlecht","_faelle_alter_geschlecht_tote"]):
        f = d+ft+".csv"
        if f not in files:# and not (d[:4] == "2020" and i == 0):
            url = sdir+f
            wget.download(url)
        
def main():
    today = datetime.date.today()
    monday = today-datetime.timedelta(days=today.weekday())
    
    for i in range(40):
        fstr = "%d%02d%02d"%(monday.year,monday.month,monday.day)
        fetch(fstr)
        monday = monday-datetime.timedelta(days=7)

if __name__ == "__main__":
    main()