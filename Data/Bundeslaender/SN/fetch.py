#!/usr/bin/env python3.7
#coding:utf-8

import pickle
import datetime

import os
import tarfile
import re

import subprocess


sdir = "https://www.coronavirus.sachsen.de/"
ddir = "corona-statistics/rest/"
names = ["newInfectionsDevelopment.jsp","incidenceVaccinationDevelopment.jsp","hospitalDevelopment.jsp","hospitalBedOccupancyDevelopment.jsp","mutationDevelopment.jsp"]

# curl 'https://www.coronavirus.sachsen.de/corona-statistics/rest/newInfectionsDevelopment.jsp' \
# -X 'GET' \
# -H 'Accept: */*' \
# -H 'Accept-Language: en-us' \
# -H 'Host: www.coronavirus.sachsen.de' \
# -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15' \
# -H 'Referer: https://www.coronavirus.sachsen.de/infektionsfaelle-in-sachsen-4151.html?_cp=%7B%7D' \
# -H 'Accept-Encoding: br, gzip, deflate' \
# -H 'Connection: keep-alive' \
# -H 'X-Requested-With: XMLHttpRequest'

def fetch(ft):
    today = datetime.date.today()
    fstr = "%d%02d%02d"%(today.year,today.month,today.day)
    
    print(ft,fstr)
    files = os.listdir()
    
    url = sdir+ddir+ft
    ofn = ft[:-4]+"_"+fstr+".jsp"
    print(url,ofn)
    
    if ofn not in files:
        call = (["wget","--referer","https://www.coronavirus.sachsen.de/infektionsfaelle-in-sachsen-4151.html","-O",ofn,url])
        subprocess.run(call)
#   for k,v in regions.items():
#        rname = "%s_Covid19%s"%(k,ft)
#        name = "%s_Covid19%s_%s"%(k,ft,fstr)
#        fname = name + ".csv"
#        if fname not in files:
#            url = sdir+"covid19%s_%d.csv"%(ft,v)
#            call = ('wget -q --referer https://www.lzg.nrw.de/covid19/covid19.html -O %s %s'%(fname,url)).split(" ")
#            subprocess.run(call,check="True").wait()
##            dname = wget.download(sdir+"covid19%s_%d.csv"%(ft,v),referer="https://www.lzg.nrw.de/covid19/covid19.html")
# #           os.rename(dname,fname)
#        tarname = rname+".tar.gz"
#        if tarname not in files:
#            tar = tarfile.open(tarname,"w:gz")
#            tar.add(fname)
#            tar.close()
#        else:
#            existing_files = [f for f in files if re.match(r'%s\_[0-9]{8}.*\.csv$'%rname, f)]
#            print(existing_files)
#            
#            tar = tarfile.open(tarname,"r:gz")
#            tarfiles = [t.name for t in tar]
#            addfiles = []
#            for efile in reversed(sorted(existing_files)):
#                if efile not in tarfiles:
#                    print(efile)
#                    addfiles.append(efile)
#            if len(addfiles) > 0:
#                tar.extractall()
#            tar.close()
#            if len(addfiles) > 0:
#                existing_files = [f for f in os.listdir() if re.match(r'%s\_[0-9]{8}.*\.csv$'%rname, f)]
#                tar = tarfile.open(tarname,"w:gz")
#                print("addfiles",addfiles)
#                for afile in existing_files:
#                    tar.add(afile)
#                tar.close()
#                
        
if __name__ == "__main__":
	for i,ft in enumerate(names):
		fetch(ft)