#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 16:35:44 2019
@author: beileitang
"""
import json
import pandas as pd
from pandas.io.json import json_normalize
"""
[] are for JSON arrays, which are called list in Python
{} are for JSON objects, which are called dict in Python
"""

with open('data_2019.json','r') as myfile:
    data= myfile.read()

obj =json.loads(data)

#%%
key_list =[]
val_list =[]
for CVE_Items in obj["CVE_Items"]:
    for cve,val in CVE_Items['cve'].items():
        key_list.append(cve)
        val_list.append(val)


b=obj['CVE_Items'][1]

b_cve=b['cve']
                  #%%

#%%
from pandas.io.json import json_normalize

new_df = pd.DataFrame()

for CVE_Items in obj["CVE_Items"]:
    for i in range(len(obj['CVE_Items'])):
        df =json_normalize(obj["CVE_Items"])
        #store dataframe in list
        new_df.append(df)
        
new_df = pd.concat(new_df)


b=obj['CVE_Items'][1]
b_cve=b['cve']

#%%
data =json_normalize(a_cve)
df = json_normalize(b_cve)
c=data.append(df)
#%%
CVE_Items_list =[]
for i in range(len(obj['CVE_Items'])):
    cve_temp = obj['CVE_Items'][i]
    CVE_Items_list.append(cve_temp)
    #%%
cve_list =[]
CVE_Items_list =[]

for i in range(len(obj['CVE_Items'])):
    cve_temp = obj['CVE_Items'][i]
    CVE_Items_list.append(cve_temp)
    for j in range(len(CVE_Items_list)):
        data_temp = CVE_Items_list[j]['cve']
        cve_list.append(data_temp)

    
    

#%%

for CVE_Items in obj["CVE_Items"]:
    for key,val in CVE_Items['cve'].items():    
        print(key)


