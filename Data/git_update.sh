#!/bin/bash

loc=${1:-"."}
echo $loc

git update-index Cases/SitRep_RKI/Hospitalisierung_SitRep.csv
git update-index ICU/SitRepICU.csv
git update-index Deaths/DeathsRKI_fromArcgis.csv

#Thursday
git update-index Deaths/SitRep_RKI/CopiedData.py

Bundeslaender/git_update.sh Bundeslaender/