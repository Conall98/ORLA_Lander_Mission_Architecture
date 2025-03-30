# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 16:48:24 2025

@author: cdepaor
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#%%
class LV:
    def __init__(self, name, launch_cost, mp2LEO, mp2TLI, Ek, role = None):
        self.name = name
        self.Lcost = launch_cost
        self.mp2LEO = mp2LEO
        self.mp2TLI = mp2TLI
        self.Ek = Ek
        self.role = role
        
#%%
def routine_1(L): #dedicated TLI. Gives the cheapest launcher from the database which can launch the payload to TLI. 
    mpTLI_req = L.mt
    count = 0#
    DB = pd.read_excel(r"Launcher DB 251 redux.xlsx")
    DB = DB.sort_values(by="$/launch")
    can = []
    for i in DB["mp2TLI"]:
        # print(i)
        if mpTLI_req < i:
            LV1 = LV(DB["Launcher"][count], DB["$/launch"][count], DB["mp2LEO"][count], DB["mp2TLI"][count], DB["Ek"][count])    
            break
        count = count + 1
    return LV1
#%%
def routine_2(L): #rideshare TLI. Gives the cheapest launcher from the database which can launch the payload to TLI. 
    mpTLI_req = L.mt
    # mpTLI_req = 3000
    count = 0#
    DB = pd.read_excel(r"Launcher DB 251 redux.xlsx")
    DB = DB.sort_values(by="$/kg TLI")

    for i in DB["mp2TLI"]:
        # print(i)
        if mpTLI_req < i:
            LV1 = LV(DB["Launcher"][count], DB["$/launch"][count], DB["mp2LEO"][count], DB["mp2TLI"][count], DB["Ek"][count])    
            break
        count = count + 1
    return LV1

#%%
def routine_3(mp_req): #dedicated LEO. Gives the cheapest launcher from the database which can launch the payload to LEO
    mpLEO_req = mp_req
    # mpTLI_req = 3000
    DB = pd.read_excel(r"Launcher DB 251 redux.xlsx")
    DB = DB.sort_values(by="$/launch")
    for i in DB["mp2LEO"]:
        # print(i)
        if mpLEO_req < i:
            # print("this one: ", i)
            index = pd.Index(DB["mp2LEO"]==i)
            count = 0
            for i in index:
                if i==True:
                    loc = count
                    # print(loc)
                count = count+1
            DB = DB.reset_index()
            LV1 = LV(DB["Launcher"][loc], DB["$/launch"][loc], DB["mp2LEO"][loc], DB["mp2TLI"][loc], DB["Ek"][loc])    
            break
    return LV1
