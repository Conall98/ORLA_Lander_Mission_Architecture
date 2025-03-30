# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 16:32:44 2025

@author: cdepaor
"""
import numpy as np
import matplotlib.pyplot as plt
import math as m
import pandas as pd
import FEB_MERs as MER
from FEB_MERs import L
#%%
def routine_1(mp, dv, Isp):
    md_init = MER.f1(mp)
    
    mprop_init = MER.f2(mp, md_init, dv, Isp)
    
    mprop = [mprop_init]
    md = [md_init]
    mt = [md_init+mprop_init+mp]
    epsilon = 0.01
    
    for i in range(0, 100):
        md.append(MER.f3(mp, mprop[i]))
        mprop.append(MER.f2(mp, md[i+1], dv, Isp))
        mt.append(md[i+1]+mprop[i+1]+mp)
        if abs(md[i+1] - md[i]) < epsilon:
            break
    
    #%% subsystems sizing routine
    
    m_str = MER.STR(md[-1])
    m_prplsn = MER.PROP(md[-1])
    m_pow = MER.POW(md[-1])
    m_avio = MER.AVIO(md[-1])
    m_ther = MER.THER(md[-1])
    m_oth = MER.OTH(md[-1])
        
    L1 = L("L1", mp, md[-1], mprop[-1], mt[-1], dv, Isp, STR = m_str, PRPLSN = m_prplsn, POW = m_pow, AVIO = m_avio, THER = m_ther, OTH = m_oth)
    Test1 = MER.Tsiolkovsky(L1)    

    return L1, Test1

    # %% Convergence Views

    # #%%
    # # Create the figure
    # plt.figure(figsize=(12, 4))
    
    # Data for plotting
    # x = np.linspace(0, len(md)-1, len(md))
    # y1 = np.array(md)
    # y2 = np.array(mprop)
    # y3 = np.array(mt)
    
    # # First subplot
    # plt.subplot(1, 3, 1)
    # plt.scatter(x, y1, color='r')
    # plt.title("Dry mass")
    # plt.xlabel("iterations")
    # plt.ylabel("dry mass")
    # # plt.legend()
    
    # # Second subplot
    # plt.subplot(1, 3, 2)
    # plt.scatter(x, y2, color = 'g')
    # plt.title("Propellant mass")
    # plt.xlabel("iterations")
    # plt.ylabel("propellant mass")
    # # plt.legend()
    
    # # Third subplot
    # plt.subplot(1, 3, 3)
    # plt.scatter(x, y3, color = 'b')
    # plt.title("Total mass")
    # plt.xlabel("iterations")
    # plt.ylabel("total mass")
    # # plt.ylim(-5, 5)  # Limit y-axis to avoid extreme values
    # # plt.legend()
    
    # # Show the plot
    # plt.tight_layout()
    # plt.show()


