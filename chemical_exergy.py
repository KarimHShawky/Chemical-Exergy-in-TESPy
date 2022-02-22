#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 19:50:02 2022

@author: Karim
"""
from CoolProp.CoolProp import PropsSI as CPSI
from tespy.tools import fluid_properties as fp
from libChemExAhrendts import Chem_Ex
import CoolProp.CoolProp as CP
import numpy as np

R=8.314/1000


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
    x=dict()
    for key in conn.fluid.val:
        x[key]= (conn.fluid.val[key])/CPSI('M', key)*(Molmasssum)
          
    return x

def mol_to_mass_comp(omega,x_dry,Molmasssum):
    
    for key in x_dry:
        omega[key]=x_dry[key]*CPSI('M',key)/Molmasssum
    return omega 



def cond_check (key, p0, T0, Molmasssum, x):
    
    
    x_cond=dict()
    
   
   
    a=CP.get_aliases(key)
     
    y=[Chem_Ex[k] for k in a if k in Chem_Ex]
       
    if y[0][2]=='NaN':
            Cond=False
    else:
                
                if p0*x[key]> CPSI('P', 'T', T0, 'Q', 0, key) :
                
                    Cond=True
                    x_dry=x.copy()
                    x_dry.pop(key)
                    x_g= sum(x_dry.values())/((p0/CPSI('P', 'T', T0, 'Q', 0, key))-1)
                    x_cond[key]=x[key]-x_g
                    x[key]=x_g
           
                else :
                    Cond=False
                
    return  x, x_cond ,Cond

def calc_reactive_exergy(conn, p0, T0):
    x=dict()
    Cond=dict()
    x_cond=dict()
    ex_react=0
    Molmasssum=0
    #Molmasssum=28.649/1000   Air Molmass
    #Molmasssum=28.254/1000   Fluegas Molmass
    
    # for key in conn.fluid.val:   if Molmasssum=0
    #         Molmasssum+= conn.fluid.val[key]*(CPSI('M', key))
             
    x= mass_to_mol_comp(conn, Molmasssum)
    
   
    for key in conn.fluid.val: 
            
            if conn.fluid.val[key]==1:
                a=CP.get_aliases(key)
                y= [Chem_Ex[k][Chem_Ex[k][4]] for k in a if k in Chem_Ex]
                ex_react=(y[0])/CPSI('M', key)
              
            else:
                
                
                    if conn.fluid.val[key]!=0:
                        x, x_cond, Cond[key] =cond_check(key, p0, T0, Molmasssum,x)
                    
                    else:
                        Cond[key]=False
                        
                    if x[key]==0:
                        ex_react+=0
                    else:
                        if Cond[key]==True:
                            a=CP.get_aliases(key)
                            y= [Chem_Ex[k][2] for k in a if k in Chem_Ex]
                            
                            ex_react+=  (x_cond[key]*y[0])#/CPSI('M', key)
                            z= [Chem_Ex[k][3] for k in a if k in Chem_Ex]
                            
                            
                            ex_react+=(x[key]*z[0]+T0*R*x[key]*np.log(x[key]))#/(CPSI('M', key))
                      
                        else :
                        
                   
                            a=CP.get_aliases(key)
                            y= [Chem_Ex[k][3] for k in a if k in Chem_Ex]
                            ex_react+=(x[key]*y[0]+T0*R*x[key]*(np.log(x[key])))#/(CPSI('M', key))
    
    return ex_react


def get_chemical_exergy(conn, p0, T0):
    ex_nonreact=calc_nonreact_exergy(conn,p0, T0)
    
   
    
    ex_react=calc_reactive_exergy(conn, p0, T0)
    
    Ex_react= ex_react* conn.m.val_SI
    Ex_nonreact= ex_nonreact* conn.m.val_SI
    
    ex_chemical= ex_react+ex_nonreact
    Ex_chemical= ex_chemical*conn.m.val_SI
    return ex_chemical
    


