#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Karim Shawky
"""
from CoolProp.CoolProp import PropsSI as CPSI
from tespy.tools import fluid_properties as fp
from libChemExAhrendts import Chem_Ex
import CoolProp.CoolProp as CP
import numpy as np

R=8.314462618/1000



def mass_to_mol_comp(conn, Molmasssum):
    x=dict()
    for key in conn.fluid.val:
        x[key]= (conn.fluid.val[key])/CPSI('M', key)*(Molmasssum)
          
    return x


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

def calc_chemical_exergy(conn, p0, T0):
    x=dict()
    Cond=dict()
    x_cond=dict()
    x1=dict()
    x2=0
    ex_react=0
    ex_react_cond=0
    ex_react_dry=0
    Molmasssum=0
    #Molmasssum=28.649/1000  # Air Molmass
    #Molmasssum=28.254/1000   #Fluegas Molmass
    
    for key in conn.fluid.val: #  if Molmasssum=0
             Molmasssum+= conn.fluid.val[key]*(CPSI('M', key))
             
    x= mass_to_mol_comp(conn, Molmasssum)
    
    
    for key in x: 
            
            if x[key]==1:
                a=CP.get_aliases(key)
                y= [Chem_Ex[k][Chem_Ex[k][4]] for k in a if k in Chem_Ex]
                ex_react_dry=(y[0])
              
            else:
                
                
                if x[key]!=0:
                    x, x_cond, Cond[key] =cond_check(key, p0, T0, Molmasssum,x)
                    
                          
                else:
                    Cond[key]=False
                   
                if x[key]==0:
                    ex_react+=0
                else:
                        #for key in x:
                        x1[key]=x[key]/sum(x.values())
                         
                        
                        if Cond[key]==True:
                            a=CP.get_aliases(key)
                            y= [Chem_Ex[k][2] for k in a if k in Chem_Ex]
                            
                            ex_react_cond+=  (x_cond[key]*y[0])
                            z= [Chem_Ex[k][3] for k in a if k in Chem_Ex]
                            
                            
                            ex_react_dry+=(x1[key]*z[0]+T0*R*x1[key]*np.log(x1[key]))
                            x2+=x_cond[key]
                        else :
                        
                   
                            a=CP.get_aliases(key)
                            y= [Chem_Ex[k][3] for k in a if k in Chem_Ex]
                            ex_react_dry+=(x1[key]*y[0]+T0*R*x1[key]*(np.log(x1[key])))
    
    ex_chemical= ex_react_cond + (1-x2)*ex_react_dry
    ex_chemical*= 1/Molmasssum
  
    return ex_chemical


def get_chemical_exergy(conn, p0, T0):
    
    
   
    
    ex_chemical=calc_chemical_exergy(conn, p0, T0)
    
   
    Ex_chemical= ex_chemical*conn.m.val_SI
    return Ex_chemical, ex_chemical
    


