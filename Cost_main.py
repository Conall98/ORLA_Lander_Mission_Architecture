# -*- coding: utf-8 -*-
"""
Created on Tue Mar 18 16:16:03 2025

@author: cdepaor
"""

import cost_fos as c
import mass_main as m
import numpy as np

#%%

def cost_main(MA):    
    Acq_cost = c.Acq_Cost(MA[0]) + c.QC(MA[1].md, 1000)[0] + MA[2].Lcost + MA[3].Lcost
    OP_cost = MA[4].Lcost
    
    LCC = Acq_cost + OP_cost
    return np.round(LCC, 0), np.round(Acq_cost, 0), np.round(OP_cost, 0)
    
#%%
mp = 2000
L_dv = 5000
L_Isp = 350
T_dv = 3800
MA = m.MA2(mp, L_dv, L_Isp, T_dv)

MA_costs = cost_main(MA)