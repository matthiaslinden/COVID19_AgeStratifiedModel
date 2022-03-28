#!/bin/bash

loc=${1:-"."}
echo $loc

git update-index $loc/SH/SH_hospital.csv
git update-index $loc/SN/SN_hospital.csv
git update-index $loc/BY/BY_hospital_*.csv

git update-index $loc/NDS/NDS_IVENA.csv
git update-index $loc/NDS/NDS_Hospital_Inzidenz.csv

git update-index $loc/BE/BE_*.csv

git update-index $loc/BW/BW_Covid19_DeathsAg.csv
git update-index $loc/BW/BW_Deaths_ManualParser.py

git update-index $loc/HE/HE_Hospitalisierungsinzidenz.csv
git update-index $loc/HH/HH_hospital.csv
