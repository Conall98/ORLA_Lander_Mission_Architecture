# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 16:13:45 2024

@author: cdepaor
"""
### TP_cost_functions ###
# reverse engineered CERs from TP. acquisition costs only

import numpy as np
#%% Project level CERs

#%%  System level CERs

#%% Subsystem (component level) CERs
def structure(m): #unmanned space planetary structures and mech primary
    return 0.0565*m + 6.796

def avionics(m): # assumed it was a programmable information processer from computer in legacy unmanned space
    return 0.2366*m + 10.15

def other(m): # assumed it was ADCS subsytem from legacy unmanned space
    return 0.2972*m + 6.958

def power(m): #EPS Legacy unmanned psace power
    return 0.2452*m + 7.93

def thermal(m): # unmanned spac planetary, thermal control, miscellaneous
    return 0.0447*m + 3.062

def motor(m): #unmanned space - earth orbiting, propulsion, thruster, liquid
    return 0.3181*m + 4.128

def tanks(m): #Unamanned space planetary, propulsion, tank, 
    return 0.0843*m + 4.572
    
#%% Polynomial CERs extracted from TruePlanning
def STR(m): #unmanned space planetary structures and mech primary
    dev = -22.33*m**2 + 53187*m + 3e06
    prod = -2.4928*m**2 + 23516*m + 210726
    return dev, prod

def AVIO(m): # assumed it was a programmable information processer from computer in legacy unmanned space
    dev = -74.614*m**2 + 177722*m + 9e06
    prod = -10.068*m**2 + 72853*m + 929305
    return dev, prod


def OTH(m): # assumed it was ADCS subsytem from legacy unmanned space
    dev = -62.302*m**2 + 148512*m + 7e06
    prod = -7.3598*m**2 + 141347*m + 2e06
    return dev, prod


def POW(m): #EPS Legacy unmanned psace power
    dev = -65.339*m**2 + 155462*m + 8e06
    prod = -10.921*m**2 + 92541*m + 996119
    return dev, prod


def THER(m): # unmanned spac planetary, thermal control, miscellaneous
    dev = -16.98*m**2 + 40326*m + 2e06
    prod = -1.5545*m**2 + 12404*m + 125758
    return dev, prod


def PRPLN(m): #unmanned space - earth orbiting, propulsion, thruster, liquid
    dev = -41.918*m**2 + 99640*m + 5e06
    prod = -6.3851*m**2 + 79597*m + 536495
    
    return dev, prod

def SYSINT(Ci): #system integration cost
    return Ci*1.044 # average found in the excel

#%% Accumulator

def Acq_Cost(L):
    A = sum(STR(L.md) + AVIO(L.md) + OTH(L.md) + POW(L.md) + THER(L.md) + PRPLN(L.md))
    AC = SYSINT(A)
    return AC

#%% QuickCost
#gives acquisition cost: the dev plus prod cost
def QC(md, POW):
    Drate = 0.5
    L = 120
    Nfrac = 0.5
    Planetary = 1
    Y = 2025
    Icomp = 0.5
    Eteam = 4
    
    A = (2.829*md**(0.457))
    B = (POW**(0.157))
    C = np.exp(0.171*Drate)
    D = np.exp(0.00209*L)
    E = np.exp(1.52*Nfrac)
    F = np.exp(0.258*Planetary)
    G = (1/(np.exp(0.0145*(Y-1960))))
    H = np.exp(0.467*Icomp)
    I = 1/np.exp(0.237*Eteam)
    Dev_cost = A*B*C*D*E*F*G*H*I
    Dev_cost = Dev_cost*(317.674/218.056) #inflation adjustment
    Dev_cost = Dev_cost*0.9227 #2023 Euro dollar rate
    Dev_cost = Dev_cost*1.02 # add two percent for phase A
    
    J    = {"A": A,
            "B": B,
            "C": C,
            "D": D,
            "E": E,
            "F": F,
            "G": G,
            "H": H,
            "I": I,}
    ADUs = 2
    Acq_cost = Dev_cost*ADUs**((1+((np.log(0.95)))/np.log(2)))
    Prod_cost = Acq_cost - Dev_cost
    return np.round(Acq_cost*1000, 2), np.round(Dev_cost*1000, 2), np.round(Prod_cost*1000, 2)
    
#%%
# md = 4540
# POW = 1000
# Drate = 0.5 
# L = 120
# Nfrac = 0.5
# Planetary = 1
# Y = 2025
# Icomp = 0.5
# Eteam = 4

# QC(4540, 1000)




































