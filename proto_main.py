# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 18:46:56 2025

@author: cdepaor
"""

import Lander_Sizing_Routines as LANR
import Launcher_Sizing_Routines as LAUR
import TV_Sizing_Routine_Type1 as TVR
# import pandas as pd
#%% MA-5 2t
mp = 2000
L_dv = 2500
L_Isp = 320

L1, Test = LANR.routine_1(mp, L_dv, L_Isp)
LV1 = LAUR.routine_1(L1)

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

#%% MA1 TEST
mp = 5000
L_dv = 5000 #LOPG - surface - LOPG
L_Isp = 450

B = MA1(mp, L_dv, L_Isp)
vars(B[2])
#%% MA-2 2t
# calling the modules in the actual MA2 order

#inputs
def MA2(mp, L_dv, L_Isp, Tdv):
    
    L1, Test_L = LANR.routine_1(mp, L_dv, L_Isp)
    # TV only has to take mp not the lander total masss
    TV1, Test_TV = TVR.routine_1(L1.mp, Tdv)
    # construction launcher the dry mass of the lander and the transfer vehicle
    CLV1 = LAUR.routine_3(TV1.md)
    CLV2 = LAUR.routine_3(L1.md)
    # regular launcher only brings nominal payload every time
    RLV1 = LAUR.routine_3(mp)
    # mprop_per_cycle a key FOM    
    
    return L1, TV1, CLV1, CLV2, RLV1, Test_L, Test_TV

#%% MA2 TEST
mp = 5000
L_dv = 5000 #LOPG - surface - LOPG
L_Isp = 450
Tdv = 3800 # LEO to LOPG
A = MA2(mp, L_dv, L_Isp, Tdv)
# vars(A[4])

#%% MA-3 2t
# calling the modules in the actual MA2 order

#inputs
def MA3(mp, L_dv, L_Isp, Tdv):
    
    L1, Test_L = LANR.routine_1(mp, L_dv, L_Isp)
    # TV only has to take mp not the lander total masss
    TV1, Test_TV1 = TVR.routine_1(L1.mp, Tdv1)
    TV2, Test_TV2 = TVR.routine_1(L1.mp, Tdv2)
    
    
    # construction launcher the dry mass of the lander and the transfer vehicle
    CLV1 = LAUR.routine_3(TV1.md)
    CLV2 = LAUR.routine_3(TV2.md)
    CLV3 = LAUR.routine_3(L1.md)
    # regular launcher only brings nominal payload every time
    RLV1 = LAUR.routine_3(mp)
    # mprop_per_cycle a key FOM    
    
    TESTS = Test_L, Test_TV1, Test_TV2
    
    return L1, TV1, CLV1, CLV2, RLV1, TESTS

#%% MA3 TEST
mp = 5000
L_dv = 5000 #LOPG - surface - LOPG
L_Isp = 450
Tdv1 = 3800 # LEO to LOPG
Tdv2 = 3800 # LEO to LOPG
MA2 = MA2(mp, L_dv, L_Isp, Tdv)
# vars(A[4])
#%% Outputs

# 

