# -*- coding: utf-8 -*-
"""
Created on Tue Mar 18 16:16:03 2025

@author: cdepaor
"""

import cost_fos as c
import mass_main as m
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#%% Main Cost function

def cost_main(MA, n, tvpow):    #mission architecture, number of missions
# =============================================================================
# Parsing the mission elements from the Mission Architecture
# =============================================================================
    k=0
    l_bin = []
    TVAC = 1
    for i in range(0, len(MA)): #applying the correct cost modules to each type
        # print(type(MA[i]) == m.LAUR.LV)
        
        if type(MA[i]) == m.LANR.MER.L:
            Lander = MA[i]
            LAC = c.Acq_Cost(MA[0]) #summation of all the true planning rules
            
        if type(MA[i]) == m.TVR.MER.TV:
            # print(type(MA[i]))
            TV = MA[i]
            
            TVAC = c.QC(TV.md, tvpow)[0]*1000
            # print(TVAC)

        if type(MA[i]) == m.LAUR.LV: #collecting the launchers
            l_bin.append(MA[i])
            # print("works")
        # print(l_bin)        
# =============================================================================
# parsing the operational and construction launch costs
# =============================================================================
    TLC = 0
    for i in range(0,len(l_bin)):
        TLC = TLC+l_bin[i].Lcost #total launch costs
        # print(l_bin)
    OLC = l_bin[-1].Lcost #operational launch costs. always the last launcher
    CLC = TLC - OLC #construction launch costs is everything other than operational
  
    #  
    # print("TVAC", TVAC)
    Acq_cost = LAC+TVAC+CLC
    # print(TV)
    
    
    # OP_cost = MA[4].Lcost*n
    PLC = MA[-1]*2720 #just use falcon 9 rideshare cost to LEO time 1.5
    OP_cost = (OLC+PLC)*n #find another operational cost model to add the other op costs
    
# =============================================================================
# Adding it all together
# =============================================================================
    LCC = Acq_cost + OP_cost
    MA_costs = {"Life Cycle Cost [M€]": np.round(LCC/1e6, 2), 
                    "Acquisition Cost [M€]": np.round(Acq_cost/1e6,2), 
                    "Total Operations Cost [M€]": np.round(OP_cost/1e6, 2)}
    
    # Cost_breakdown = {"Lander total": np.round(L_lcc/1e6, 2), 
    #                 "TV total [M€]": np.round(TV_lcc/1e6,5), 
    #                 "Opcost [M€]": np.round(OP_cost/1e6, 2)}
    # Cost_breakdown = 1
    
    return MA_costs
    
#%% Test
# MA1_costs, sc_costs = cost_main(MA1, 20)
# MA2_costs = cost_main(MA2, 20, 1000)
#%% Results function
def results(MA, MA_costs, n, tvpow):
    MA_costs = cost_main(MA, n, tvpow)
    #Life Cycle Cost [€]
    LCC = MA_costs["Life Cycle Cost [M€]"]
    #system acquisition cost [€]
    AC = MA_costs["Acquisition Cost [M€]"]
    #Marginal Mission cost [€/mission]
    MMC = MA_costs["Total Operations Cost [M€]"]/n
    #Specific payload delivery cost [€/kg]
    SPDC = MA_costs["Life Cycle Cost [M€]"]/(MA[0].mp*n)*10e6
    #specific payload return cost [€/kg]
    SPRC = MA_costs["Life Cycle Cost [M€]"]/(MA[0].mp*n)*10e6 # should be just the extra fuel cost for this
    #Delivery time [days]
    #DT = number of rdvs*days
    #Landed Payload per launch [kg/launch] #fuel launches will be the problem
    #Return Payload per launch [kg/launch] #fuel launches will be the problem
    RD = {"Life Cycle Cost                       [M€]    ":LCC, 
          "System Acquisition Cost               [M€]    ":AC, 
          "Marginal Mission cost                 [M€]    ":MMC, 
          "Specific Payload Delivery Cost        [€/kg]  ":SPDC, 
          "Specific Payload Return Cost          [€/kg]  ":SPRC}
    return RD
#%%
DB = pd.read_excel(r"C:\Users\cdepaor2\Desktop\ORLA_Lander_Mission_Architecture\Lander DB 251 redux.xlsx")

#%% inputs
mp = 2000
L_dv = 5000
L_Isp = 450
T_dv = 3800
T_dv2 = 2*640
#%% Masses
MA1 = m.MA1(mp, L_dv, L_Isp, T_dv)
MA2 = m.MA2(mp, L_dv, L_Isp, T_dv)
MA3 = m.MA3(mp, L_dv, L_Isp, T_dv, T_dv2)
MA4 = m.MA4(mp, L_dv, L_Isp, T_dv)
MA5 = m.MA5(mp, L_dv, L_Isp, T_dv)
#%% costs
MA1_costs = cost_main(MA1, 20, 1000)
MA2_costs = cost_main(MA2, 20, 1000)
MA3_costs = cost_main(MA3, 20, 6000)
MA4_costs = cost_main(MA4, 20, 1000)
MA5_costs = cost_main(MA5, 20, 1000)

#%% Results
MAR1 = results(MA1, MA1_costs, 20, 1000)
MAR2 = results(MA2, MA2_costs, 20, 1000)
MAR3 = results(MA3, MA3_costs, 20, 6000)
MAR4 = results(MA4, MA4_costs, 20, 1000)
MAR5 = results(MA5, MA5_costs, 20, 1000)


#%% propellant per cycle
mp = 2000
MA1_ef = [1, MA1[-1]/mp]
MA2_ef = [1, MA2[-1]/mp]
MA3_ef = [1, MA3[-1]/mp]
MA4_ef = [1, MA4[-1]/mp]
MA5_ef = [1, MA5[-1]/mp]
#%%
w = 0.25

pc = "blue"
fc = "orange"

plt.figure()
plt.bar(0, MA1_ef[1], 0.25, color=fc, label = "fuel")
plt.bar(0+w, MA1_ef[0], 0.25, color=pc, label = "payload")

plt.bar(1, MA2_ef[1], 0.25, color=fc, label = "fuel")
plt.bar(1+w, MA2_ef[0], 0.25, color=pc, label = "payload")

plt.bar(2, MA3_ef[1], 0.25, color=fc, label = "fuel")
plt.bar(2+w, MA3_ef[0], 0.25, color=pc, label = "payload")

plt.bar(3, MA4_ef[1], 0.25, color=fc, label = "fuel")
plt.bar(3+w, MA4_ef[0], 0.25, color=pc, label = "payload")

plt.bar(4, MA5_ef[1], 0.25, color=fc, label = "fuel")
plt.bar(4+w, MA5_ef[0], 0.25, color=pc, label = "payload")

plt.xticks([0.125, 1.125, 2.125, 3.125, 4.125], ["MA1", "MA2", "MA3", "MA4", "MA5"])



plt.xlabel("Mission Architectures")
plt.ylabel("mass")
plt.minorticks_on()
plt.grid(which = "major", color= "#bfbfbf")
plt.grid(which = "minor", color = "#E6E6E6")
plt.title("Initial guess vs. sizing algorithm")
plt.legend()





#%% the different sizing rule lines

# mp = 2000
# L_dv = 5000
# L_Isp = 450
# T_dv = 3800
# mps = np.linspace(20, 5000, 1000)
# dvs = [2000, 3500, 5000, 6500]
# mds = np.zeros([len(mps), len(dvs)])
# icount=0
# for i in mps:
#     jcount=0
#     icount = icount+1
#     for j in dvs:
#         # print("hello this is the payload mass!!!", i)
#         MA_test = m.MA2(i, j, L_Isp, T_dv)
       
#         mds[icount, jcount] = MA_test[0].md
#         jcount = jcount + 1

# plt.figure()
# plt.plot(mps[1:], mds[1:, 0], label = "$\Delta V$ = 2000")
# plt.plot(mps[1:], mds[1:, 1], label = "$\Delta V$ = 3500")
# plt.plot(mps[1:], mds[1:, 2], label = "$\Delta V$ = 5000")
# plt.plot(mps[1:], mds[1:, 3], label = "$\Delta V$ = 6500")
# plt.scatter(DB["mp"], DB["md"], color = "black")

# xdata= DB["mp"]
# ydata= DB["md"]

# plt.figure()
# plt.scatter(xdata, ydata, label='data', color = "black")

# np.linspace(min(xdata), max(xdata)+10, 100)

# plt.plot(np.linspace(min(xdata), 5000, 1000), m.LANR.MER.f1(mps), "--",color = "red",
#           label="Sizing rule")
# plt.plot(mps[1:], mds[1:,0], label = "$\Delta V = 2km/s$")
# plt.plot(mps[1:], mds[1:,1], label = "$\Delta V = 3.5km/s$")
# plt.plot(mps[1:], mds[1:,2], label = "$\Delta V = 5km/s$")
# plt.plot(mps[1:], mds[1:,3], label = "$\Delta V = 6km/s$")

# plt.xlabel("mp")
# plt.ylabel("md")
# plt.minorticks_on()
# plt.grid(which = "major", color= "#bfbfbf")
# plt.grid(which = "minor", color = "#E6E6E6")
# plt.title("Initial guess vs. sizing algorithm")
# plt.legend()
    
# #%%
# plt.figure()
# plt.scatter(xdata, ydata, label='data', color = "black")

# np.linspace(min(xdata), max(xdata)+10, 100)
# mps = np.linspace(20, 100000, 1000)
# plt.plot(mps, m.LANR.MER.f1(mps), "--",color = "red",
#           label="Sizing rule")

