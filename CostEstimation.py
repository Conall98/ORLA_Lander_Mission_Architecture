# -*- coding: utf-8 -*-
"""
Created on Mon Mar  3 12:26:44 2025

@author: cdepaor
"""
#FOMs
#System Acquisition Cost [€]
#Marginal Mission Cost [€/Mission]
#Specific Payload delivery Cost [€/kg]
#Specific Payload Return cost [€/kg]
#Delivery Time [hours]
#Landed Payload [kg]
#Returned Payload [kg]

class MA:
    def __init__(self, 
                 SAC, 
                 MMC,
                 SPDC,
                 SPRC,
                 DT,
                 LP,
                 RP):
        self.SAC = SAC
        self.MMC = MMC
        self.SPDC = SPDC
        self.SPRC = SPRC
        self.DT = DT
        self.LP = LP
        self.RP = RP
    
    