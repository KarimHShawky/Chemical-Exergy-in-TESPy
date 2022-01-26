# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 11:16:24 2021

@author: kshaw
"""
import CoolProp as CP
from CoolProp.CoolProp import PropsSI
from tespy.tools import fluid_properties as fp

fluid={"water": 0.7, "NH3": 0.3}
p0=100000
T0=298.15


def calc_nonreact_exergy(conn, T0, p0)
    ex_nonreact=0
    hsum=0
    ssum=0
    if 1 in conn.fluid.values():
    
        ex_nonreact=0
    else: 
            for key in conn.fluid:
                hsum+= conn.fluid[key]*PropsSI('H','T',T0,'P',p0, key)
                ssum+= conn.fluid[key]*PropsSI('S','T',T0,'P',p0, key)
        
            ex_nonreact= (fp.h_mix_pT([0, p0, 0, conn.fluid.val], T0)-hsum)
            -T0*(fp.s_mix_pT([0, p0, 0, conn.fluid.val], T0)-ssum)
    return ex_nonreact 
# In calc_Physical_exergy vielleicht mit einbauen, bzw. analog aufbauen
# conn.fluid.val von calc_physical_exergy in tools übernommen, idealerweise direkt darunter, einmal für non react und react
# erstmal nonreact da es einfacher ist. Ende der woche hoffmann anschreiben