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

class MA_FOM:
    def __init__(self, 
                 SAC, 
                 MMC,
                 SPDC,
                 SPRC,
                 DT,
                 LP,
                 RP):
        self.SAC = SAC # system acquisition cost
        self.MMC = MMC # mission marginal cost
        self.SPDC = SPDC # Specific Delivery Cost
        self.SPRC = SPRC # Specific return cost
        self.DT = DT # delivery time
        self.LP = LP # landed payload
        self.RP = RP # returned payload
    
#%% MA1
#MMC is launch cost +ten percent
flights = 20
mpd = 2000
mpr = 2000
total_mpd = flights*mpd
total_mpr = flights*mpr
SAC = 420.1*1e6
OPC=778.6*1e6
MMC = OPC/flights
LCC = SAC + OPC
LP = mpd
RP = mpr
DT = 7
SPDC = LCC/total_mpd
SPRC = LCC/total_mpr
MA1 = MA_FOM(SAC, MMC, SPDC, SPRC, DT, LP, RP)


#%% MA2
#MMC is launch cost +ten percent
flights = 20
mpd = 2000
mpr = 2000
DT = 7
SAC = 420.1*1e6
OPC=778.6*1e6

total_mpd = flights*mpd
total_mpr = flights*mpr
MMC = OPC/flights
LCC = SAC + OPC
LP = mpd
RP = mpr

SPDC = LCC/total_mpd
SPRC = LCC/total_mpr
MA1 = MA_FOM(SAC, MMC, SPDC, SPRC, DT, LP, RP)

#%% MA3
#MMC is launch cost +ten percent
flights = 20
mpd = 2000
mpr = 2000
DT = 7
SAC = 420.1*1e6
OPC=778.6*1e6

total_mpd = flights*mpd
total_mpr = flights*mpr
MMC = OPC/flights
LCC = SAC + OPC
LP = mpd
RP = mpr

SPDC = LCC/total_mpd
SPRC = LCC/total_mpr
MA1 = MA_FOM(SAC, MMC, SPDC, SPRC, DT, LP, RP)

#%% MA4
#MMC is launch cost +ten percent
flights = 20
mpd = 2000
mpr = 2000
DT = 7
SAC = 420.1*1e6
OPC=778.6*1e6

total_mpd = flights*mpd
total_mpr = flights*mpr
MMC = OPC/flights
LCC = SAC + OPC
LP = mpd
RP = mpr

SPDC = LCC/total_mpd
SPRC = LCC/total_mpr
MA1 = MA_FOM(SAC, MMC, SPDC, SPRC, DT, LP, RP)

#%% MA5
#MMC is launch cost +ten percent
flights = 20
mpd = 2000
mpr = 2000
DT = 7
SAC = 420.1*1e6
OPC=778.6*1e6

total_mpd = flights*mpd
total_mpr = flights*mpr
MMC = OPC/flights
LCC = SAC + OPC
LP = mpd
RP = mpr

SPDC = LCC/total_mpd
SPRC = LCC/total_mpr
MA1 = MA_FOM(SAC, MMC, SPDC, SPRC, DT, LP, RP)

