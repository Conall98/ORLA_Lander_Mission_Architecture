# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 18:30:51 2025

@author: cdepaor
"""

import numpy as np
import matplotlib.pyplot as plt
import math as m
import pandas as pd
#%%
import TV_MERs as MER
from TV_MERs import TV
from FEB_MERs import L

#%%
DB = pd.read_excel(r"Transfer_vehicle_DB 25 redux.xlsx")
#%%
def routine_1(Tmp, dv):
    TVmp = Tmp #default params
    TVdv = dv#default params
        
    CE_req = 0.5*TVmp*TVdv**2
    CE_cans = []
    args = []
    count = 0
    for i in DB["CE*"]:
        CE_can = i
        if CE_can > CE_req:
            CE_cans.append(CE_can)
            args.append(count)
        count = count+1
        
    index = pd.Index(DB["CE*"]==min(CE_cans))
    count = 0
    for i in index:
        if i==True:
            loc = count
        count = count+1
    
    TV1 = TV(DB.iloc[loc, 0], 
             DB.iloc[loc, 1], 
             DB.iloc[loc, 3], 
             DB.iloc[loc, 2] + DB.iloc[8, 3] + TVmp,
             DB.iloc[loc, 6], #gigajoules of KE
             DB.iloc[loc, 8],
             TVmp, 
             TVdv)
    
    
    test_CE1 = MER.CE_test(TV1)
    test_Tsiolkovsky = MER.Tsiol_test(TV1)
    test_CE2 = MER.CE_test2(TV1, CE_req)
    tests = [test_CE1, test_Tsiolkovsky, test_CE2]
    # think about scaling the dry masss with the lower energy requirement
    # md = md*(CE_req/CE)
    return TV1, tests






    


