# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 17:46:37 2025

@author: cdepaor
"""

import numpy as np
import pandas as pd
#%%
class TV:
    def __init__(self, name, md, mprop, mt, CE, Isp, mp = None, dv = None):
        self.name = name
        self.md = md
        self.mprop = mprop
        self.mt = mt
        self.CE = CE
        self.Isp = Isp
        self.mp = mp
        self.dv = dv
#%%
DB = pd.read_excel(r"Transfer_vehicle_DB 25 redux.xlsx")

TV1 = TV(DB.iloc[8, 0], 
         DB.iloc[8, 1], 
         DB.iloc[8, 3], 
         DB.iloc[8, 2] + DB.iloc[8, 3],
         DB.iloc[8, 6], 
         DB.iloc[8, 8])


def CE_test(TV): #Gives the DV of any transfer vehicle plus payload
    if TV.dv - np.sqrt((2*TV.CE)/(TV.md+TV.mp)) < TV.dv/0.01:
        return True
    else:
        return False

def Tsiol_test(TV):
    mp = TV.mp
    md = TV.md
    mprop = TV.mprop
    dv = TV.dv
    isp = TV.Isp
    # print("payload mass", mp, 
    #       "\ndry mass", md, 
    #       "\nmprop", mprop, 
    #       "\ndv", dv, 
    #       "\nIsp", isp)
    if abs(dv - isp*9.81*np.log((mp+mprop+md)/(mp+md))) < abs(dv/0.01):
        return True
    else:
        return False

def CE_test2(TV, CE_req):
    if CE_req<=TV.CE:
        return True
    else:
        return False
