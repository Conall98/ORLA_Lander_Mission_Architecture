# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 17:13:49 2025

@author: cdepaor
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 18:46:56 2025

@author: cdepaor
"""

import Lander_Sizing_Routines as LANR
import Launcher_Sizing_Routines as LAUR
import TV_Sizing_Routine_Type1 as TVR
import numpy as np
import matplotlib.pyplot as plt
# import pandas as pd
#%% MA-5 2t
# mp = np.random.normal(3000, 20, 1000)
mp = 2000
mp_sd = 100 #5%

L_dv = 2500
L_dv_sd = 125 #5%

L_Isp = 320
L_Isp_sd = 16 #5%



i = np.random.normal(mp, mp_sd, 1000)
j = np.random.normal(L_dv, L_dv_sd, 1000)
k = np.random.normal(L_Isp, L_Isp_sd, 1000)


#%% Gaussian Payload
bucket = []
bucket2 = []
bucket3 = []
for A in i:
# for j in L_dv:
#     for k in L_Isp:
        L1, Test = LANR.routine_1(A, L_dv, L_Isp)
        LV1 = LAUR.routine_1(L1)
        bucket.append(L1.md)
        bucket2.append(L1.mprop)
        bucket3.append(L1.mt)
#%%
bucket = []
bucket2 = []
bucket3 = []
for A in j:
# for j in L_dv:
#     for k in L_Isp:
        L1, Test = LANR.routine_1(mp, A, L_Isp)
        LV1 = LAUR.routine_1(L1)
        bucket.append(L1.md)
        bucket2.append(L1.mprop)
        bucket3.append(L1.mt)
        
#%%
bucket = []
bucket2 = []
bucket3 = []
for A in k:
# for j in L_dv:
#     for k in L_Isp:
        L1, Test = LANR.routine_1(mp, L_dv, A)
        LV1 = LAUR.routine_1(L1)
        bucket.append(L1.md)
        bucket2.append(L1.mprop)
        bucket3.append(L1.mt)

#%% Histagrams

# plt.figure()
# mean = np.mean(bucket)
# plt.hist(bucket, 100)
# plt.axvline(mean, color = "black", linestyle = "--")
# plt.xlabel("dry mass")

# plt.figure()
# plt.hist(i, 100)
# plt.xlabel("mp")
#%% ijk QUAD PLOTS GAUSSES
fig, axs = plt.subplots(2,2)
fig.suptitle("Uncertainty Propagation")

axs[0,0].hist(k, 100)
mean=np.mean(k)
axs[0,0].axvline(mean, color = "black", linestyle = "--")
axs[0,0].set_title("Input Uncertainty (Isp) sd = 5%")
axs[0,0].set_xlabel("Isp")

axs[0,1].hist(bucket, 100)
mean=np.mean(bucket)
axs[0,1].axvline(mean, color = "black", linestyle = "--")
axs[0,1].set_title("Output Uncertainty (md)")
axs[0,1].set_xlabel("dry mass")

axs[1,0].hist(bucket2, 100)
mean=np.mean(bucket2)
axs[1,0].axvline(mean, color = "black", linestyle = "--")
axs[1,0].set_title("Output Uncertainty (mprop)")
axs[1,0].set_xlabel("propellant mass")

axs[1,1].hist(bucket3, 100)
mean=np.mean(bucket3)
axs[1,1].axvline(mean, color = "black", linestyle = "--")
axs[1,1].set_title("Output Uncertainty (mt)")
axs[1,1].set_xlabel("Total Mass")

#%%
plt.figure()
plt.title("dv and the params when Isp is gaussian")
plt.scatter(j, bucket, label = "dry mass")
plt.scatter(j, bucket2, label = "propellant mass")
plt.scatter(j, bucket3, label = "total mass")
plt.legend()

#%%
plt.figure()
plt.title("mp and dv")
plt.scatter(i, bucket, label = "dry mass")
plt.legend()

































