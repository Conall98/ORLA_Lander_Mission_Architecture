# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 17:46:37 2025

@author: cdepaor
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#%%
class TV:
    def __init__(self, name, mp, md, mprop, mt, CE):
        self.name = name
        self.mp = mp
        self.md = md
        self.mprop = mprop
        self.mt = mt
        self.CE = CE
#%%
DB = pd.read_excel(r"Transfer_vehicle_DB 25 redux.xlsx")
#%%
i=0
TV1 = TV(DB["Name"][i], DB["mp"][i], DB["md"][i], DB["mprop"][i], + DB["mp"][i] + DB["md"][i] + DB["mprop"][i], DB["CE*"][i])
#%%
def CE_curve(CE, md, mp): #GIVES THE ce CURVE OF ANY TV. Set lander weight to mp
    dv = np.sqrt((2*CE)/(md+mp))
    return dv


