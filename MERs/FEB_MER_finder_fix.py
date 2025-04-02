# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 17:24:56 2025

@author: cdepaor
"""

import numpy as np
import matplotlib.pyplot as plt
import math as m
import pandas as pd
from scipy.optimize import curve_fit
#%% Functions
#mp2md
def f1(mp):
    return 367.29*np.log(mp) - 904.17

def f2(mp, md, dv, Isp):# gives mprop with mp+md
    return (mp+md)*(np.exp(dv/(Isp*9.81)) - 1)

def func(x, a, b):
    return a*x**b

#%% finding f3
# need three arrays: mp, mprop and md
LDB = pd.read_excel(r"C:\Users\cdepaor2\Desktop\ORLA_Lander_Mission_Architecture\Lander DB 251 redux.xlsx", sheet_name = "All Real Landers")
mp = np.array(LDB["mp"])
mprop = np.array(LDB["mprop"])
md = np.array(LDB["md"])

#%%
xdata = np.array(mp+mprop)
ydata = np.array(md)
popt, pcov = curve_fit(func, xdata, ydata)

A = np.round(popt[0], 2)
B = np.round(popt[1], 2)
# C = np.round(popt[2], 2)

def f3(mp, mprop, A, B):
    x = mp+mprop
    return A*x**B

#%%
plt.figure()
plt.scatter(xdata, ydata, label='data', color = "black")

np.linspace(min(xdata), max(xdata)+10, 100)

plt.plot(np.linspace(min(xdata), max(xdata)+10, 100), func(np.sort(np.linspace(min(xdata), max(xdata)+10, 100)), *popt), "--",color = "red",
          label=r"md = ${{{0}}} \cdot x^{{{1}}}$".format(A, B))

plt.xlabel("mp + mprop")
plt.ylabel("md")
plt.minorticks_on()
plt.grid(which = "major", color= "#bfbfbf")
plt.grid(which = "minor", color = "#E6E6E6")
plt.title("Unmanned Lunar Landers \n Payload Mass + Prop Mass Versus Dry Mass")
plt.legend()



#%% 3D finding f3
# ax = plt.figure().add_subplot(projection='3d')
# # Plot a sin curve using the x and y axes.
# x = mp
# y = mprop
# z = md
# ax.scatter(x, y, z, zdir='z', label='curve in (x, y)')

# ax.legend()
# ax.set_xlabel('mp')
# ax.set_ylabel('mprop')
# ax.set_zlabel('md')

# # ax.view_init(elev=20., azim=-35, roll=0)

# plt.show()