# -*- coding: utf-8 -*-
"""
Created on Mon Mar  3 11:57:21 2025

@author: cdepaor
"""

#%%
#FOMs
#System Acquisition Cost [€]
#Marginal Mission Cost [€/Mission]
#Specific Payload delivery Cost [€/kg]
#Specific Payload Return cost [€/kg]
#Delivery Time [hours]
#Landed Payload [kg]
#Returned Payload [kg]

def System_Acquisition_Cost(cost, norm, weighting): #positive sense (Down)
    normalised_cost = cost/norm
    return -normalised_cost*weighting

def Marginal_Mission_Cost(cost, norm, weighting): #positive sense (Down)
    normalised_cost = cost/norm
    return -normalised_cost*weighting

def Specific_Payload_Delivery_Cost(cost, norm, weighting): #positive sense (Down)
    normalised_cost = cost/norm
    return -normalised_cost*weighting

def Specific_Payload_Return_Cost(cost, norm, weighting): #positive sense (Down)
    normalised_cost = cost/norm
    return -normalised_cost*weighting

def Delivery_Time(cost, norm, weighting): #positive sense (Down)
    normalised_cost = cost/norm
    return -normalised_cost*weighting

def Landed_Payload(cost, norm, weighting): #positive sense (Up)
    normalised_cost = cost/norm
    return normalised_cost*weighting

def Returned_Payload(cost, norm, weighting): #positive sense (up)
    normalised_cost = cost/norm
    return normalised_cost*weighting
    

