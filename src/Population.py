
import numpy as np
import pandas as pd
import xarray as xr

# Import Population
def ImportPopulation(f="../Data/Population/12421-0004_utf8.csv"):
    bls = {1:"Schleswig-Holstein",2:"Hamburg",3:"Niedersachsen",4:"Bremen",5:"Nordrhein-Westfalen",6:"Hessen",7:"Rheinland-Pfalz",8:"Baden-Württemberg"}
    bls.update({9:"Bayern",10:"Saarland",11:"Berlin",12:"Brandenburg",13:"Mecklenburg-Vorpommern",14:"Sachsen",15:"Sachsen-Anhalt",16:"Thüringen"})
    blsT = {}
    for k,v in bls.items():
        blsT[v] = k

    pf = pd.read_csv(f,sep=";",header=[6])
    col = pf.columns

    pf = pf.filter([col[0],col[1],col[3],col[4],col[5],col[6],col[7],col[8]])
    pf.rename(columns={col[0]:"BL",col[1]:"variant",col[3]:"sex",col[4]:"age"},inplace=True)

    pfv1 = pf[pf["variant"] == "BEV-VARIANTE-01"].drop(columns=["variant"])
    pfv1["BL"] = pfv1["BL"].map(lambda x : blsT[x])
    xv1 = pfv1.set_index(['BL','sex','age']).to_xarray().sel(sex=["männlich","weiblich"]).assign_coords({"sex":["male","female"]})

    new_age_index = {}
    new_age_index["unter 1 Jahr"] = 0
    for i in range(1,100):
        new_age_index["%d-Jährige"%i] = i
    new_age_index["100 Jahre und mehr"] = 100
    #new_age_index["Insgesamt"] = -1

    xv1 = xv1.sel(age=list(new_age_index.keys())).assign_coords({"age":np.array(list(new_age_index.values()),dtype="int8")})
    return xv1
    
    
def WeeklyPopulation(pop,weeks):
    years = {"31.12.2019":0,"31.12.2020":53,"31.12.2021":53+52,"31.12.2022":53+52*2}
    r_years,i_years = {},{}
    i = 0
    for k,v in years.items():
        r_years[v] = k
        i_years[i] = k
        i += 1
    print(r_years)
    
    w_pop = {}
    i,ky = 0,list(r_years.keys())
    for w in weeks:
        for j,k in enumerate(ky):
            if k > w:
                break
            else:
                i = j
        ki,kj = w-ky[i],ky[j]-w
        ks = kj+ki
        fi,fj = (ks-ki)/ks, (ks-kj)/ks
        
        w_pop[w] = pop[i_years[i]]*fi+pop[i_years[j]]*fj
    # Concatenate weekly arrays
    wpop = xr.concat(list(w_pop.values()),pd.Index(w_pop.keys())).rename({"concat_dim":"week"})
    return wpop*1000