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
    # print("c md_init", md_init)
    mprop_init = MER.f2(mp, md_init, dv, Isp)
    # print("D mprop_init", mprop_init)
    mprop = [mprop_init]
    md = [md_init]
    mt = [md_init+mprop_init+mp]
    epsilon = 0.01
    
    for i in range(0, 100):
        # print("F", MER.f3(mp, mprop[i]))
        # print("G", mp, mprop[i])
        # print("H", mp+mprop)
        md.append(MER.f3(mp, mprop[i]))
        mprop.append(MER.f2(mp, md[i+1], dv, Isp))
        mt.append(md[i+1]+mprop[i+1]+mp)
        if abs(md[i+1] - md[i]) < epsilon:
            break
    # print("E", md[-1])
    m_str = MER.STR(md[-1])
    m_prplsn = MER.PROP(md[-1])
    m_pow = MER.POW(md[-1])
    m_avio = MER.AVIO(md[-1])
    m_ther = MER.THER(md[-1])
    m_oth = MER.OTH(md[-1])
        
    L1 = L("L1", mp, md[-1], mprop[-1], mt[-1], dv, Isp, STR = m_str, PRPLSN = m_prplsn, POW = m_pow, AVIO = m_avio, THER = m_ther, OTH = m_oth)
    Test1 = MER.Tsiolkovsky(L1)    

    return L1, Test1
#%% For MAi_STAR
def routine_2(mp, dv, Isp):
    dv_down = dv/2
    dv_up = dv/2
    
    #sizing for the downward portion'
    md_init = MER.f1(mp)
    # print("c md_init", md_init)
    mprop_init = MER.f2(mp, md_init, dv_down, Isp)
    # print("D mprop_init", mprop_init)
    mprop = [mprop_init]
    md = [md_init]
    mt = [md_init+mprop_init+mp]
    epsilon = 0.01
    
    for i in range(0, 100):
        # print("F", MER.f3(mp, mprop[i]))
        # print("G", mp, mprop[i])
        # print("H", mp+mprop)
        md.append(MER.f3(mp, mprop[i]))
        mprop.append(MER.f2(mp, md[i+1], dv_down, Isp))
        mt.append(md[i+1]+mprop[i+1]+mp)
        if abs(md[i+1] - md[i]) < epsilon:
            break
    # print("E", md[-1])

#sizing adjustment for the upward portion
    m_prop_up_init = MER.f2(0, md[-1], dv_up, Isp)
    m_prop_ups = [m_prop_up_init]
    
    m_props_new = [mprop[-1] + m_prop_up_init]
    mds_new = [md[-1]]
    mts_new = [mt[-1]]
    
    for i in range(0, 100):
        # print("F", MER.f3(mp, mprop[i]))
        # print("G", mp, mprop[i])
        # print("H", mp+mprop)
        # print("A", i)
        # print("B", m_prop_ups[i])
        mds_new.append(MER.f3(mp, m_props_new[i])) # new md with the extra mprop
        m_props_new.append(mprop[-1] + MER.f2(0, mds_new[i+1], dv_up, Isp)) # new mprop with the extra md
        mts_new.append(md[i+1]+mprop[i+1]+mp) # new mt for theway down
        if abs(mds_new[i+1] - mds_new[i]) < epsilon:
            break

    

# final sizing of the subsystems
    
    m_str = MER.STR(md[-1])
    m_prplsn = MER.PROP(md[-1])
    m_pow = MER.POW(md[-1])
    m_avio = MER.AVIO(md[-1])
    m_ther = MER.THER(md[-1])
    m_oth = MER.OTH(md[-1])
        
    L1 = L("L1", mp, mds_new[-1], m_props_new[-1], mts_new[-1], dv, Isp, STR = m_str, PRPLSN = m_prplsn, POW = m_pow, AVIO = m_avio, THER = m_ther, OTH = m_oth)
    Test1 = MER.Tsiolkovsky_star(L1)    

    return L1, Test1


#%%
L_star, Test_star = routine_2(2000, 5000, 450)

#%% star test



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


