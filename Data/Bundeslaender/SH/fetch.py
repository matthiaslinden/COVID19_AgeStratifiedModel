#!/usr/bin/env python3.7
#coding:utf-8

import pickle
import datetime

import os
import tarfile
import wget
import re


# SH-Version

#https://phpefi.schleswig-holstein.de/corona/data202011/cvd_sh_kreise.csv
#https://phpefi.schleswig-holstein.de/corona/data202011/cvd_sh_alter.csv
#https://phpefi.schleswig-holstein.de/corona/data202011/cvd_sh_verlauf.csv

sdir = "https://phpefi.schleswig-holstein.de/corona/data202011/"
filenames = zip(["cvd_sh_kreise","cvd_sh_alter","cvd_sh_verlauf"],["Kreise","Alter","Verlauf"])

def fetch(d):
    files = os.listdir()
    for i,x in enumerate(filenames):
        ft,out = ft
        f = d+ft+".csv"
        o = out+".csv"

        if f not in files:# and not (d[:4] == "2020" and i == 0):
            url = sdir+f
            wget.download(url,o)
        
def main():
    today = datetime.date.today()
    fstr = "%d%02d%02d"%(today.year,today.month,today.day)
    files = os.listdir()
    
    for i,x in enumerate(filenames):
        ft,out = x
        od = out+"_%s"%(fstr)
        odcsv = od+".csv"
        if odcsv not in files:
            url = sdir+ft+".csv"
            wget.download(url,odcsv)
        
        tarname = out+".tar.gz"
        if tarname not in files:
            tar = tarfile.open(tarname,"w:gz")
            tar.add(odcsv)
            tar.close()
            
        else:
            files = os.listdir()
            existing_files = [f for f in files if re.match(r'%s\_[0-9]{8}.*\.csv$'%out, f)]
            tar = tarfile.open(tarname,"r:gz")
            tarfiles = [t.name for t in tar]
            addfiles = []
            for efile in existing_files:
                if efile not in tarfiles:
                    print(efile)
                    addfiles.append(efile)
            if len(addfiles) > 0:
                tar.extractall()
            tar.close()
            
            if len(addfiles) > 0:
                existing_files = [f for f in os.listdir() if re.match(r'%s\_[0-9]{8}.*\.csv$'%out, f)]
                tar = tarfile.open(tarname,"w:gz")
                print("addfiles",addfiles)
                for afile in existing_files:
                    tar.add(afile)
                tar.close()
            
    """    rname = "%s_Covid19"%(k)
        name = "%s_Covid19_%s"%(k,fstr)
        fname = name + ".csv"
        if fname not in files:
            dname = wget.download(sdir+"%d.csv"%v)
            os.rename(dname,fname)
        tarname = rname+".tar.gz"
        if tarname not in files:
            tar = tarfile.open(tarname,"w:gz")
            tar.add(fname)
            tar.close()
        else:
            existing_files = [f for f in files if re.match(r'%s\_[0-9]{8}.*\.csv$'%rname, f)]
            print(existing_files)
            
            tar = tarfile.open(tarname,"r:gz")
            tarfiles = [t.name for t in tar]
            addfiles = []
            for efile in existing_files:
                if efile not in tarfiles:
                    print(efile)
                    addfiles.append(efile)
            if len(addfiles) > 0:
                tar.extractall()
            tar.close()
            if len(addfiles) > 0:
                existing_files = [f for f in os.listdir() if re.match(r'%s\_[0-9]{8}.*\.csv$'%rname, f)]
                tar = tarfile.open(tarname,"w:gz")
                print("addfiles",addfiles)
                for afile in existing_files:
                    tar.add(afile)
                tar.close()
                """
        
if __name__ == "__main__":
    main()