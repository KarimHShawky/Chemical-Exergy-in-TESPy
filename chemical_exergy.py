#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 19:50:02 2022

@author: Karim
"""
from CoolProp.CoolProp import PropsSI as CPSI
from tespy.tools import fluid_properties as fp
from ChemExDictionaryTest import Chem_Ex_Szargut
import CoolProp.CoolProp as CP





def calc_nonreact_exergy(conn, p0, T0):
    ex_nonreact=0
    hsum=0
    ssum=0
    if 1 in conn.fluid.val.values():
    
        ex_nonreact=0
    else: 
        for key in conn.fluid.val:
                hsum+= conn.fluid.val[key]*CPSI('H','T',T0,'P',p0, key)
                ssum+= conn.fluid.val[key]*CPSI('S','T',T0,'P',p0, key)
        #print(hsum)            
        ex_nonreact= ((fp.h_mix_pT([0, p0, 0, conn.fluid.val], T0)-hsum)
                    -T0*(fp.s_mix_pT([0, p0, 0, conn.fluid.val], T0)-ssum))
       # print((fp.h_mix_pT([0, p0, 0, conn.fluid.val], T0)-hsum))
    return ex_nonreact 



def mass_to_mol_comp(conn, Molmasssum):
    x= conn.fluid.val
    for key in conn.fluid.val:
        x[key]= (conn.fluid.val[key])/CPSI('M', key)*(Molmasssum)
          
    return x

def mol_to_mass_comp(omega,x_dry,Molmasssum):
    
    for key in x_dry:
        omega[key]=x_dry[key]*CPSI('M',key)/Molmasssum
    return omega 



def cond_check (conn, p0, T0):
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
def calc_reactive_exergy(omega):
        ex_react=0
        for fld in omega :
            if fld=='H2Of':
                ex_react+=  omega[fld]*Chem_Ex_Szargut['Water(l)'][2]
            else :
            
                    x=CP.get_aliases(fld)
                    y= [Chem_Ex_Szargut[k][2] for k in x if k in Chem_Ex_Szargut]
                    #print(y)
                    ex_react += omega[fld]*y[0]

        return ex_react


def get_chemical_exergy(conn, p0, T0):
    ex_nonreact=calc_nonreact_exergy(conn,p0, T0)
    
    omega=cond_check(conn,p0, T0)
    
    ex_react=calc_reactive_exergy(omega)
    
    Ex_react= ex_react* conn.m.val_SI
    Ex_nonreact= ex_nonreact* conn.m.val_SI
    
    ex_chemical= ex_react+ex_nonreact
    Ex_chemical= ex_chemical*conn.m.val_SI
    return ex_nonreact, ex_react
    


