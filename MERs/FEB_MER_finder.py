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

def func(x, a, b, c):
    return a*x**b + c

#%% finding f3
# need three arrays: mp, mprop and md
LDB = pd.read_excel(r"C:\Users\cdepaor2\Desktop\ORLA ACTA Paper\Lander mini_db 2025.xlsx", sheet_name = "All Real Unmanned Landers")
mp = np.array(LDB["mp"])
mprop = np.array(LDB["mprop"])
md = np.array(LDB["md"])

#%%
xdata = np.array(mp+mprop)
ydata = np.array(md)
popt, pcov = curve_fit(func, xdata, ydata)

A = np.round(popt[0], 2)
B = np.round(popt[1], 2)
C = np.round(popt[2], 2)

def f3(mp, mprop, A, B, C):
    x = mp+mprop
    return A*x**B+C

def fp(x, a, b, c):
    return a*x**2+b*x+c

#%%
plt.figure()
plt.scatter(xdata, ydata, label='data', color = "black")

np.linspace(min(xdata), max(xdata)+10, 100)

plt.plot(np.linspace(min(xdata), max(xdata)+10, 100), func(np.sort(np.linspace(min(xdata), max(xdata)+10, 100)), *popt), "--",color = "red",
          label=r"md = ${{{0}}} \cdot x^{{{1}}}+{2}$".format(A, B, C))

plt.xlabel("mp + mprop")
plt.ylabel("md")
plt.minorticks_on()
plt.grid(which = "major", color= "#bfbfbf")
plt.grid(which = "minor", color = "#E6E6E6")
plt.title("Unmanned Lunar Landers \n Payload Mass + Prop Mass Versus Dry Mass")
plt.legend()


#%% TP sizing rule replotting
y1data = [7669432, 12462013,	16552061,	20244599, 23672831]
y2data = [2532355,	4824784,	7039092,	9210067,	11349670]
xdata = [100,	200,	300,	400,	500]

y1data= [x/1e6 for x in y1data]
y2data= [x/1e6 for x in y2data]

popt, pcov = curve_fit(fp, xdata, y1data)
popt2, pcov2 = curve_fit(fp, xdata, y2data)

a = np.round(popt[0], 2)
b = np.round(popt[1], 2)
c = np.round(popt[2], 2)

a2 = np.round(popt2[0], 2)
b2 = np.round(popt2[1], 2)
c2 = np.round(popt2[2], 2)


plt.figure()
plt.scatter(xdata, y1data, label='Dev cost data', color = "blue")
plt.scatter(xdata, y2data, label='Prod cost data', color = "orange")

np.linspace(min(xdata), max(xdata)+10, 100)

plt.plot(np.linspace(min(xdata), max(xdata)+10, 100), fp(np.sort(np.linspace(min(xdata), max(xdata)+10, 100)), *popt), "--",color = "blue",
          label=r"Dev cost model")

plt.plot(np.linspace(min(xdata), max(xdata)+10, 100), fp(np.sort(np.linspace(min(xdata), max(xdata)+10, 100)), *popt2), "--",color = "orange",
          label=r"Prod. cost model")

plt.xlabel("Mass [kg]")
plt.ylabel("Cost [M€]")
plt.minorticks_on()
plt.grid(which = "major", color= "#bfbfbf")
plt.grid(which = "minor", color = "#E6E6E6")
plt.title("Surrogate models for cost estimation of structure.")
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