# -*- coding: utf-8 -*-
"""
Created on Fri Apr  4 11:13:39 2025

@author: conal
"""

import Cost_main as CM
import mass_main as m
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
#%%

DB = pd.read_excel(r"C:\Users\conal\Desktop\PhD\ORLA_Lander_Mission_Architecture\Lander DB 251 redux.xlsx")

#%% inputs
mp = 2001
L_dv = 5000
L_Isp = 450
T_dv = 3800
T_dv2 = 2*640
n = 20
#%% Masses
MA1 = m.MA1(mp, L_dv, L_Isp, T_dv)
MA1_star = m.MA1_star(mp, L_dv, L_Isp, T_dv)
MA2 = m.MA2(mp, L_dv, L_Isp, T_dv)
MA3 = m.MA3(mp, 4000, L_Isp, T_dv, T_dv2)
MA4 = m.MA4(mp, L_dv, L_Isp, T_dv)
MA5 = m.MA5(mp, L_dv, L_Isp, T_dv)
#%% costs
MA1_costs = CM.cost_main(MA1, n, 1000)
MA1_star_costs = CM.cost_main(MA1_star, n, 1000)
MA2_costs = CM.cost_main(MA2, n, 1000)
MA3_costs = CM.cost_main(MA3, n, 6000)
MA4_costs = CM.cost_main(MA4, n, 1000)
MA5_costs = CM.cost_main(MA5, n, 1000)

#%% Results
MAR1 = CM.results(MA1, n, 1000, MA1_star)
MAR2 = CM.results(MA2, n, 1000)
MAR3 = CM.results(MA3, n, 6000)
MAR4 = CM.results(MA4, n, 1000)
MAR5 = CM.results(MA5, n, 1000)


#%% propellant per cycle
mp = 2000
MA1_ef = [1, MA1[-1]/mp]
MA2_ef = [1, MA2[-1]/mp]
MA3_ef = [1, MA3[-1]/mp]
MA4_ef = [1, MA4[-1]/mp]
MA5_ef = [1, MA5[-1]/mp]
#%% CHARTS
w = 0.25
fontsize = 12

pc = "blue"
fc = "orange"

plt.figure()
plt.bar(0, MA1_ef[1], 0.25, color=fc, label = "fuel")
plt.bar(0+w, MA1_ef[0], 0.25, color=pc, label = "payload")

plt.bar(1, MA2_ef[1], 0.25, color=fc)
plt.bar(1+w, MA2_ef[0], 0.25, color=pc)

plt.bar(2, MA3_ef[1], 0.25, color=fc)
plt.bar(2+w, MA3_ef[0], 0.25, color=pc)

plt.bar(3, MA4_ef[1], 0.25, color=fc)
plt.bar(3+w, MA4_ef[0], 0.25, color=pc)

plt.bar(4, MA5_ef[1], 0.25, color=fc)
plt.bar(4+w, MA5_ef[0], 0.25, color=pc)

plt.xticks([0.125, 1.125, 2.125, 3.125, 4.125], ["MA1", "MA2", "MA3", "MA4", "MA5"])



plt.xlabel("Mission Architectures", fontsize = 12)
plt.ylabel("kgs of fuel per kgs of payload", fontsize = 12)
plt.minorticks_on()
plt.grid(which = "major", color= "#bfbfbf", axis="y")
plt.grid(which = "minor", color = "#E6E6E6", axis="y")
plt.title("Initial guess vs. sizing algorithm", fontsize = 18)
plt.legend(fontsize = 12)





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

#%%












