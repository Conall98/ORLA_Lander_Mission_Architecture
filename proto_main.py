# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 18:46:56 2025

@author: cdepaor
"""

import Lander_Sizing_Routines as LAN
import Launcher_Sizing_Routines as LAU
#%% MA-5 2t
mp = 2000
L_dv = 2500
L_Isp = 320

L1, Test = LAN.routine_1(mp, L_dv, L_Isp)
LV1 = LAU.routine_1(L1)


#%% MA-2 2t
mp = 2000
L_dv = 5000
L_Isp = 320

L1, Test = LAN.routine_1(mp, L_dv, L_Isp)



#%% Outputs
Out_1 = vars(L1)
Out_2 = vars(LV1)


