#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Karim Shawky
@author: Mathias Hofmann, TU Berlin
"""

import numpy as np
from CoolProp.CoolProp import PropsSI              # CP dublette
import CoolProp.CoolProp as CP                      # CP dublette
from tespy.tools.helpers import molar_mass_flow
from .libChemExAhrendts import Chem_Ex

R = 8.314462618*1E-3  # kJ/(mol K)


def mass2molar_fraction(conn, molar_mass_mixture):
    molar_fraction = dict()
    for key in conn.fluid.val:
        molar_fraction[key] = conn.fluid.val[key] / PropsSI('M', key) * molar_mass_mixture
          
    return molar_fraction


def flash_routine(key, ambient_pressure, ambient_temperature, x):
    x_cond = dict()
    a = CP.get_aliases(key)
    y = [Chem_Ex[k] for k in a if k in Chem_Ex]
       
    if y[0][2] == 'NaN':
        condensation = False                    # Was ist hier die Idee? ### Falls kein Flüssiger Wert vorliegt würde es rechnerisch keinen Sinn ergeben eine Kondensationsprüfung durch zuführen
    else:
        if ambient_pressure * x[key] > PropsSI('P', 'T', ambient_temperature, 'Q', 0, key):
            condensation = True
            x_dry = x.copy()
            x_dry.pop(key)
            x_g = sum(x_dry.values())/((ambient_pressure / PropsSI('P', 'T', ambient_temperature, 'Q', 0, key)) - 1)
            x_cond[key] = x[key] - x_g
            x[key] = x_g
        else:
            condensation = False
            
    return x, x_cond, condensation


def calc_chemical_exergy(conn, ambient_pressure, ambient_temperature):
    x = dict()
    cond = dict()
    x_cond = dict()
    x1 = dict()
    x2 = 0
    ex = 0
    ex_cond = 0
    ex_dry = 0
    molar_mass_mixture = 0

    x = {
            fluid: y / (PropsSI('M', fluid) * molar_mass_flow(conn.fluid.val))
            for fluid, y in conn.fluid.val.items()
        }

    molar_mass_mixture = sum([x * PropsSI('M', fluid) for fluid, x in x.items()])

    for key in x:
        if x[key] == 1:                         # pure substance
            a = CP.get_aliases(key)
            y = [Chem_Ex[k][Chem_Ex[k][4]] for k in a if k in Chem_Ex]
            ex_dry = y[0]
        else:
            if x[key] != 0:
                x, x_cond, cond[key] = flash_routine(key, ambient_pressure, ambient_temperature, x)
            else:
                cond[key] = False
            if x[key] == 0:
                ex += 0
            else:
                # for key in x:
                x1[key] = x[key]/sum(x.values())
                if cond[key]:                   # cond[key] == True
                    a = CP.get_aliases(key)
                    y = [Chem_Ex[k][2] for k in a if k in Chem_Ex]
                            
                    ex_cond += x_cond[key] * y[0]
                    z = [Chem_Ex[k][3] for k in a if k in Chem_Ex]
                    ex_dry += x1[key] * z[0] + ambient_temperature * R * x1[key] * np.log(x1[key])
                    x2 += x_cond[key]
                else:
                    a = CP.get_aliases(key)
                    y = [Chem_Ex[k][3] for k in a if k in Chem_Ex]
                    ex_dry += x1[key] * y[0] + ambient_temperature * R * x1[key] * np.log(x1[key])
    
    ex_chemical = ex_cond + (1 - x2) * ex_dry
    ex_chemical *= 1 / molar_mass_mixture
  
    return ex_chemical


def get_chemical_exergy(conn, ambient_pressure, ambient_temperature):
    ex_chemical = calc_chemical_exergy(conn, ambient_pressure, ambient_temperature)
    Ex_chemical = ex_chemical * conn.m.val_SI

    return Ex_chemical, ex_chemical
