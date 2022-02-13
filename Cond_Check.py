#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 14:44:48 2022

@author: karim
"""


from CoolProp.CoolProp import PropsSI as CPSI



def mass_to_mol_comp(conn, Molmasssum):
    x= conn.fluid.val
    for key in conn.fluid.val:
        x[key]= (conn.fluid.val[key])/CPSI('M', key)*(Molmasssum)
          
    return x

def mol_to_mass_comp(omega,x_dry,Molmasssum):
    
    for key in x_dry:
        omega[key]=x_dry[key]*CPSI('M',key)/Molmasssum
    return omega 



def cond_check (conn, T0, p0):
    omega=dict()
    x=dict()
    omega=conn.fluid.val
    if conn.fluid.val['H2O'] == None or conn.fluid.val['H2O']==0:
       omega=omega 
    else :
    
        Molmasssum=0
        for key in conn.fluid.val:
            Molmasssum+= conn.fluid.val[key]*(CPSI('M', key))
        
          
        x= mass_to_mol_comp(conn, Molmasssum)
        
        
        if p0*x['H2O']> CPSI('P', 'T', T0, 'Q', 0, 'H2O') :
            
            x_dry=x.copy()
            x_dry.pop('H2O')
            x_H2Og= sum(x_dry.values())/((p0/CPSI('P', 'T', T0, 'Q', 0, 'H2O'))-1)
            x_H2Of=x['H2O']-x_H2Og
            x['H2Og']=x.pop('H2O')
            x['H2Og']=x_H2Og
            x['H2Of']=x_H2Of
            
            omega=mol_to_mass_comp(omega, x_dry, Molmasssum)
            omega['H2Og']=x['H2Og']*CPSI('M','H2O')/Molmasssum
            omega['H2Of']=x['H2Of']*CPSI('M','H2O')/Molmasssum
           
        else :
            omega=omega
        
    return omega
    