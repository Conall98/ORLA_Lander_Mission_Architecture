# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 15:16:41 2025

@author: cdepaor
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import pandas as pd
#%%
def func(x, a, b, c):
    return a*x**b + c
#%%
LDB = pd.read_excel(r"C:\Users\cdepaor2\Desktop\ORLA ACTA Paper\Lander mini_db 2025.xlsx", sheet_name = "All Real Unmanned Landers")
mp = np.array(LDB["mp"])
mprop = np.array(LDB["mprop"])
md = np.array(LDB["md"])
#%%
xdata = np.array(mp+mprop)
ydata = np.array(md)
plt.figure()
plt.scatter(xdata, ydata, label='data')
#%%
popt, pcov = curve_fit(func, xdata, ydata)
popt
plt.plot(np.sort(xdata), func(np.sort(xdata), *popt), color = "red",
         label='fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(popt))

plt.legend()