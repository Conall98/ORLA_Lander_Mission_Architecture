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
mp=3000
L_dv = 2500
L_Isp = 320
bucket = []
i = np.random.normal(3000, 200, 1000)
j = L_dv
k = L_Isp
for A in i:
# for j in L_dv:
#     for k in L_Isp:
        L1, Test = LANR.routine_1(A, j, k)
        LV1 = LAUR.routine_1(L1)
        bucket.append(L1.md)

#%% Histagrams

plt.figure()
mean = np.mean(bucket)
plt.hist(bucket, 100)
plt.axvline(mean, color = "black", linestyle = "--")
plt.xlabel("dry mass")

plt.figure()
plt.hist(i, 100)
plt.xlabel("mp")