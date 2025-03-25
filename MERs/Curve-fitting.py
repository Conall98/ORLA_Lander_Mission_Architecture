# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 15:16:41 2025

@author: cdepaor
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import pandas as pd
import random
import statistics as st
#%%
def func(x, a, b, c):
    return a*x**b + c

def func2(x, a, b, c):
    return a*np.log(b*x) +c
#%%
LDB = pd.read_excel(r"C:\Users\cdepaor2\Desktop\ORLA_Lander_Mission_Architecture\Lander DB 251 redux.xlsx", sheet_name = "All Real Landers")
mp = np.array(LDB["mp"])
mprop = np.array(LDB["mprop"])
md = np.array(LDB["md"])
#%%
xdata = np.array(mp)
ydata = np.array(md)
plt.figure()
plt.scatter(xdata, ydata, label='data')
#%% BAsic case
popt, pcov = curve_fit(func, xdata, ydata)
popt
xpoints = np.linspace(min(xdata), max(xdata), 100)
# plt.plot(xpoints, func(np.sort(xpoints), *popt), color = "red",
#          label='ax^b+c: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(popt))

plt.plot(xpoints, func(np.sort(xpoints), *popt), color = "red",
          label='power law')

popt, pcov = curve_fit(func2, xdata, ydata)
popt
xpoints = np.linspace(min(xdata), max(xdata), 100)
plt.plot(xpoints, func2(np.sort(xpoints), *popt), color = "blue",
         label='log law')


plt.legend()

#%%% Random cherry picking pick half of the datapoints randomly and see what happens
def MSA(xdata, ydata, foi):
    plt.figure()
    points = 1000
    xpoints = np.linspace(min(xdata), max(xdata), points)
    pairs = np.array([xdata,ydata])
    linesx = np.zeros([100, len(xpoints)])
    linesy = np.zeros([100, len(xpoints)])
    for i in range(0, len(linesx[:,0])):
        
        bucket1 = random.sample(range(0,int((1/3)*len(ydata))), 5)
        bucket2 = random.sample(range(int((1/3)*len(ydata)),int((2/3)*len(ydata))), 5)
        bucket3 = random.sample(range(int((2/3)*len(ydata)),int((3/3)*len(ydata))), 5)
        CPD = bucket1+ bucket2+ bucket3
        CPDx = []
        CPDy = []
        for j in CPD:
            CPDx.append(pairs[0, j])    
            CPDy.append(pairs[1, j])    
        popt, pcov = curve_fit(foi, CPDx, CPDy)
        popt
        # plt.scatter(CPDx, CPDy, color = "black", label = "data")
        plt.plot(xpoints, foi(np.sort(xpoints), *popt), color = "black",
                 label='log law', linestyle = "--")
        
        linesx[i, :] = xpoints
        linesy[i, :] = foi(xpoints, *popt)
    plt.ylim(0, max(ydata)*1.1)
    plt.scatter(xdata, ydata, label='data', color = "red")
    plt.xlabel("Payload mass, $m_p$ [kg]")
    plt.ylabel("dry mass $m_d$ [kg]")
    plt.title("$f_1 = m_d(m_p)$ Model Sensitivity Analysis 1")
    
    #making histograms from lines
    # print(linesy)
    # print(xpoints)
    
    return linesx, linesy
# plt.legend()

def histlines(lines, poi):
    plt.figure()
    plt.hist(lines[:, poi], 15)
    plt.xlabel("dry mass $m_d$ [kg]")

#%%
# plt.figure()
lines = MSA(xdata, ydata, func)
#%%
for i in range (20, 30):
    histlines(lines[1], i)
    
#%% plotting the average and std
mean_line = []
upper_std = []
lower_std = []
u2s = []
l2s = []
u3s = []
l3s = []
for i in range(0, 1000):
    m = np.mean(lines[1][:,i])
    s = st.stdev(lines[1][:,i])
    mean_line.append(m)
    upper_std.append(m+s)
    lower_std.append(m-s)
    u2s.append(m+2*s)
    l2s.append(m-2*s)
    u3s.append(m+3*s)
    l3s.append(m-3*s)
#%%
plt.figure()
plt.plot(lines[0][0], mean_line, color = "#000000")
plt.plot(lines[0][0], upper_std, color = "#999999", linestyle = "--")
plt.plot(lines[0][0], lower_std, color = "#999999", linestyle = "--")
plt.plot(lines[0][0], u2s, color = "#CCCCCC", linestyle = "--")
plt.plot(lines[0][0], l2s, color = "#CCCCCC", linestyle = "--")
plt.plot(lines[0][0], u3s, color = "#E1E1E1", linestyle = "--")
plt.plot(lines[0][0], l3s, color = "#E1E1E1", linestyle = "--")

plt.scatter(xdata, ydata, label='data', color = "red")
plt.xlabel("Payload mass, $m_p$ [kg]")
plt.ylabel("dry mass $m_d$ [kg]")
plt.title("$f_1 = m_d(m_p)$ Model Sensitivity Analysis 2")
plt.ylim(0, max(ydata))






























