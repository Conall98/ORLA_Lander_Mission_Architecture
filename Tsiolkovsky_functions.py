# -*- coding: utf-8 -*-
"""
Created on Mon Apr  7 10:46:32 2025

@author: cdepaor
"""

import numpy as np
import matplotlib.pyplot as plt
import FEB_MERs as F

#%% segmented Tsiolkovsky
def Tsiol(mp1, mp2, md1, md2, dv1, dv2, Isp):
    mprop2 = (mp2+md2)*(np.exp((dv2)/(Isp*9.81)))
    mprop1 = (mp1+md1+mprop2)*(np.exp((dv1)/(Isp*9.81)))
    mprop = mprop1 + mprop2
    
    A = [np.round(mprop1 , 2), np.round(mprop2 , 2), np.round(mprop , 2)]
    return A
    
    
def MFR(L): #Marginal fuel requirement for ascending journeys
    mp1 = L.mp
    mp2 = 0
    md1 = L.md, 
    md2 = L.md 
    dv1 = L.dv/2 
    dv2 = L.dv/2
    Isp = L.Isp
    mprop2 = (mp2+md2)*(np.exp((dv2)/(Isp*9.81)))
    mprop1 = (mp1+md1+mprop2)*(np.exp((dv1)/(Isp*9.81)))
    mprop = mprop1 + mprop2
    
    A = [np.round(mprop2 , 2), np.round(mprop2/mprop, 3), np.round(mprop, 3)]
    return A    


def MDR(L): #marginal dry mass requirement 
    mfr = MFR(L)[0]
    mprop = L.mp
    md = L.md
    mp = L.mp
    mdr = F.f3(mp, mprop) - F.f3(mp, mprop - mfr) #the extra dry mass
    # print(F.f3(mp, mprop - mfr))
    A = [np.round(mdr, 2), np.round(mdr/md, 2), np.round(md, 2)]
    return A
    
    
#%%
# E = MFR(2000, 2000, 1800, 1800, 2500, 2500, 450)
G = MDR(MA1[0])
#%%
B = Tsiol(2000, 0, 1800, 1800, 2500, 2500, 450)
C = Tsiol(0, 2000, 1800, 1800, 2500, 2500, 450)
D = Tsiol(2000, 2000, 1800, 1800, 2500, 2500, 450)

js = np.linspace(1000, 3000, 100)
ks = np.linspace(4000, 6000, 100)
Ds = np.zeros([len(js), len(ks)])
i_counter = 0

for i in js:
    j_counter = 0
    for j in ks:
        C = Tsiol(i, i, 1800, 1800, j, j, 450)
        D = C[1]/C[0]
        Ds[i_counter, j_counter] = np.round(D, 3)
        j_counter = j_counter + 1
    i_counter = i_counter + 1
    
#%%
plt.figure()
# plt.imshow(Ds)
# plt.ylabel("payload mass [kg]")
# plt.xlabel("delta V [m/s]")
plt.plot(Ds[0, :])
    