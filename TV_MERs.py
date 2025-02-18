# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 17:46:37 2025

@author: cdepaor
"""

import nupy as np
#%%
class TV:
    def __init__(self, name, mp, md, mprop, mt, CE, dv, Isp):
        self.name = name
        self.mp = mp
        self.md = md
        self.mprop = mprop
        self.mt = mt
        self.CE = CE
        self.dv = dv
        self.Isp = Isp
        
#%%


def TV_dV(CE, md, mp): #Gives the DV of any transfer vehicle plus payload
    dv = np.sqrt((2*CE)/(md+mp))
    return dv


