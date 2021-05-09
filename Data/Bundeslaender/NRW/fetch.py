#!/usr/bin/env python3.7
#coding:utf-8

import pickle
import datetime

import os
import tarfile
import wget
import re

regions = {"NRW":5,"Koeln":5315,"Heinsberg":5370,"Siegen-W":5970,"Muenster":5515,"Bonn":5314,"Dortmund":5913,"Duisburg":5112,"Duesseldorf":5111,"Essen":5113,"Recklinghausen":5562,"Rhein-Sieg":5382,"Aachen":5334,"Wuppertal":5124,"Minden":5770,"Krefeld":5114,"Bielefeld":5711}

sdir = "https://www.lzg.nrw.de/covid19/daten/"


def fetch(d):
    files = os.listdir()
    for i,ft in enumerate(["_todesfalle","_faelle_alter_geschlecht","_faelle_alter_geschlecht_tote"]):
        f = d+ft+".csv"
        if f not in files:# and not (d[:4] == "2020" and i == 0):
            url = sdir+f
            wget.download(url)
        
def main():
    today = datetime.date.today()
    fstr = "%d%02d%02d"%(today.year,today.month,today.day)
    files = os.listdir()
    for k,v in regions.items():
        rname = "%s_Covid19"%(k)
        name = "%s_Covid19_%s"%(k,fstr)
        fname = name + ".csv"
        if fname not in files:
            dname = wget.download(sdir+"covid19_%d.csv"%v)
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
            for efile in reversed(sorted(existing_files)):
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
                
        
if __name__ == "__main__":
    main()