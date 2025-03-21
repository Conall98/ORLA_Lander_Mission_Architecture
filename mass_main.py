# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 18:46:56 2025

@author: cdepaor
"""

import Lander_Sizing_Routines as LANR
import Launcher_Sizing_Routines as LAUR
import TV_Sizing_Routine_Type1 as TVR
# import pandas as pd
import numpy as np

#%% calling the modules in the MA1 order
def MA1(mp, L_dv, L_Isp):
    
    L1, Test_L = LANR.routine_1(mp, L_dv, L_Isp)
    # TV only has to take mp not the lander total masss

    # construction launcher the dry mass of the lander and the transfer vehicle
    CLV1 = LAUR.routine_3(L1.md)
    CLV2 = LAUR.routine_3(L1.mprop) #assuming free fuel at LOPG
    # regular launcher only brings nominal payload every time
    RLV1 = LAUR.routine_3(mp)
    # mprop_per_cycle a key FOM    
    return L1, CLV1, CLV2, RLV1, Test_L

#%% MA-2 2t
# calling the modules in the actual MA2 order

#inputs
def MA2(mp, L_dv, L_Isp, Tdv):
    
    L1, Test_L = LANR.routine_1(mp, L_dv, L_Isp)
    # TV only has to take mp not the lander total masss
    TV1, Test_TV = TVR.routine_3(L1.mp, Tdv)
    # construction launcher the dry mass of the lander and the transfer vehicle
    CLV1 = LAUR.routine_3(TV1.md)
    CLV2 = LAUR.routine_3(L1.md)
    # regular launcher only brings nominal payload every time
    RLV1 = LAUR.routine_3(mp)
    # mprop_per_cycle a key FOM    
    
    return L1, TV1, CLV1, CLV2, RLV1, Test_L, Test_TV

#%% MA-3 2t
# calling the modules in the actual MA2 order

#inputs
def MA3(mp, L_dv, L_Isp, Tdv1, Tdv2):
    
    L1, Test_L = LANR.routine_1(mp, L_dv, L_Isp)
    # TV only has to take mp not the lander total masss
    TV1, Test_TV1 = TVR.routine_3(L1.mp, Tdv1)
    TV2, Test_TV2 = TVR.routine_3(L1.mp, Tdv2)
    
    
    # construction launcher the dry mass of the lander and the transfer vehicle
    CLV1 = LAUR.routine_3(TV1.md)
    CLV2 = LAUR.routine_3(TV2.md)
    CLV3 = LAUR.routine_3(L1.md)
    # regular launcher only brings nominal payload every time
    RLV1 = LAUR.routine_3(mp)
    # mprop_per_cycle a key FOM    
    
    TESTS = Test_L, Test_TV1, Test_TV2
    
    return L1, TV1, TV2, CLV1, CLV2, CLV3, RLV1, TESTS


#%% Outputs

def MA4(mp, L_dv, L_Isp, Tdv):
    L1, Test_L = LANR.routine_1(mp, L_dv, L_Isp)
    TV1, Test_TV1 = TVR.routine_2(L1.mp, Tdv) # use routine 2 for electric prop
    
    CLV1 = LAUR.routine_3(TV1.md)
    CLV2 = LAUR.routine_3(L1.md)
    
    RLV1 = LAUR.routine_3(mp)
    
    TESTS = Test_L, Test_TV1
    
    return L1, TV1, CLV1, CLV2, RLV1, TESTS

#%% MA-5 2t
def MA5(mp, L_dv, L_Isp):

    L1, Test_L = LANR.routine_1(mp, L_dv, L_Isp)
    LV1 = LAUR.routine_3(L1.mt)
    TESTS = Test_L
    
    return L1, LV1, TESTS


# #%% MA1 2t TEST
# mp = 2000
# L_dv = 5000 #LOPG - surface - LOPG
# L_Isp = 450

# MA1_obj_2t = MA1(mp, L_dv, L_Isp)
# #%% MA1 max
# mps = np.linspace(2000, 40000, 180)
# for i in mps:
#     MA1_obj_max = MA1(i, L_dv, L_Isp)
#     if MA1_obj_max[0].mprop > 60000: #the max constraint currently it is the 
#     #fuel to LEO constraint. Assuming one launch for the fuel. FH launches fuel
#         break
    

#%% MA2 2t TEST
mp = 2000 
L_dv = 5000 #LOPG - surface - LOPG
L_Isp = 450
Tdv = 3800 # LEO to LOPG
MA1_obj_2t = MA1(mp, L_dv, L_Isp)
#%% MA2 MAX
mps = np.linspace(2000, 40000, 180)
for i in mps:
    MA2_obj_max = MA2(i, L_dv, L_Isp, Tdv)
    if MA2_obj_max[1].mprop > 60000: #the max constraint currently it is the 
    #fuel to LEO constraint. Assuming one launch for the fuel. FH launches fuel
        break
  

# #%% MA3 2t TEST
# mp = 2000
# L_dv = 4000 #LLO - surface - LLO
# L_Isp = 450
# Tdv1 = 3800 # LEO to LOPG
# Tdv2 = 2*640 # LOPG to LLO
# MA3_obj_2t = MA3(mp, L_dv, L_Isp, Tdv1, Tdv2)
# #%% MA3 max
# mps = np.linspace(2000, 40000, 180)
# for i in mps:
#     MA3_obj_max = MA3(i, L_dv, L_Isp, Tdv1, Tdv2)
#     if MA3_obj_max[1].mprop > 60000: #the max constraint currently it is the 
#     #fuel to LEO constraint. Assuming one launch for the fuel. FH launches fuel
#         break


# #%% MA4 2t TEST
# mp = 2000
# L_dv = 5000 #LOPG - surface - LOPG
# L_Isp = 450
# Tdv1 = 3800 # LEO to LOPG
# MA4_obj_2t = MA4(mp, L_dv, L_Isp, Tdv1)
# #%% MA4 max
# mps = np.linspace(2000, 40000, 180)
# for i in mps:
#     MA4_obj_max = MA4(i, L_dv, L_Isp, Tdv1)
#     if MA4_obj_max[0].md > 60000: #the max constraint currently it is the 
#     #fuel to LEO constraint. Assuming one launch for the fuel. FH launches fuel
#         break

# #%%
# mp = 2000
# L_dv = 2500
# L_Isp = 450

# MA5_obj_2t = MA5(mp, L_dv, L_Isp)
# #%% MA5 max
# mps = np.linspace(2000, 60000, 180)
# for i in mps:
#     MA5_obj_max = MA5(i, L_dv, L_Isp)
#     if MA5_obj_max[0].mt > 95000: #the max constraint currently it is the 
#     #fuel to LEO constraint. Assuming one launch for the fuel. FH launches fuel
#         break








