# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 17:24:56 2025

Hard coded sizing rules functions

@author: cdepaor
"""

import numpy as np
#%%
class L:
    def __init__(self, name, mp, md, mprop, mt, dv=None, isp=None, STR = None, PRPLSN = None, POW = None, AVIO = None, THER = None, OTH = None):
        self.name = name
        self.mp = np.round(mp, 2)
        self.md = np.round(md, 2)
        self.mprop = np.round(mprop, 2)
        self.mt = np.round(mt, 2)
        self.dv = np.round(dv, 2)
        self.Isp = np.round(isp, 2)
        self.STR = np.round(STR, 2)
        self.PRPLSN = np.round(PRPLSN, 2)
        self.POW = np.round(POW, 2)
        self.AVIO = np.round(AVIO, 2)
        self.THER = np.round(THER, 2)
        self.OTH = np.round(OTH, 2)

#%% Functions
#mp2md
def f1(mp):
    return 367.29*np.log(mp) - 904.17

def f2(mp, md, dv, Isp):# gives mprop with mp+md
    return (mp+md)*(np.exp(dv/(Isp*9.81)) - 1)

def f3(mp, mprop):
    x = mp+mprop
    return 12.49*x**0.55


#%% subsystem functions
def STR(md):
    return md*0.276

def PROP(md):
    return md*0.337

def POW(md):
    return md*0.076

def AVIO(md):
    return md*0.088

def THER(md):
    return md*0.13

def OTH(md):
    return md*0.062

#%% TESTS

def Tsiolkovsky(L):
    mp = L.mp
    md = L.md
    mprop = L.mprop
    dv = L.dv
    isp = L.Isp
    # print("payload mass", mp, 
    #       "\ndry mass", md, 
    #       "\nmprop", mprop, 
    #       "\ndv", dv, 
    #       "\nIsp", isp)
    if abs(dv - isp*9.81*np.log((mp+mprop+md)/(mp+md))) < dv/0.01:
        
        return True
    else:
        return False
#%%
def Tsiolkovsky_star(L):
    mp = L.mp
    md = L.md
    mprop = L.mprop
    dv = L.dv
    dv_down = dv/2
    dv_up = dv/2
    Isp = L.Isp
    
    mprop_down = f2(mp, md, dv_down, Isp)
    mprop_up = f2(0, md, dv_up, Isp)
    
    # print("A", mprop_up)
    # print("B", mprop_down)
    
    if abs(dv_down - Isp*9.81*np.log((mp+mprop_down+md)/(mp+md))) < dv_down/0.01:
        # print("C: Down should be true")
        Down = True
    else: 
        Down = False
        
    if abs(dv_up - Isp*9.81*np.log((mprop_up+md)/(md))) < dv_up/0.01:
        up = True
    else:
        up = False
    
    if Down == True & up == True:
        return True
    else: 
        return False













#