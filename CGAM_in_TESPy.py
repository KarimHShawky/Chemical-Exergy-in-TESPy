#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 14:13:28 2022

@author: karim
"""
#from kkh import kkh
#from CoolProp.CoolProp import PropsSI as CPSI
from tespy.networks import Network
from tespy.connections import Connection, Bus
from tespy.components import (
    Source, Sink, Compressor, HeatExchanger , 
    DiabaticCombustionChamber, Valve, Turbine, Drum )



nw= Network(fluids=['CO2', 'CH4','O2','N2' ,'H2O'], 
            T_unit='K', p_unit='bar', h_unit='kJ / kg' , m_unit='kg / s')


# In and output streams
air_in= Source('air in')
fuel_in= Source('fuel in')
out= Sink('fluegas out')

w_in= Source('water in')
w_out= Sink('water out')

## Components
ac= Compressor('air compressor')
aph= HeatExchanger('Air preheater')
cc= DiabaticCombustionChamber('Combustion Chamber')
va1= Valve('Valve1')
exp=Turbine('Turbine')
eva= HeatExchanger('Evaporator')
eco= HeatExchanger('Economizer')
dr= Drum('Drum')
 # to regulate the pressure difference between fuel inlet and cc inlet
## Connections

a_in_ac= Connection(air_in, 'out1', ac, 'in1')
ac_in_aph= Connection(ac, 'out1', aph, 'in2')

aph_in_cc=Connection(aph, 'out2', cc, 'in1')
fuel_in_va1=Connection(fuel_in, 'out1', va1, 'in1')
va1_in_cc=Connection(va1, 'out1', cc, 'in2')
cc_in_exp=Connection(cc, 'out1', exp, 'in1')
exp_in_aph=Connection(exp, 'out1', aph, 'in1')
aph_in_eva=Connection( aph, 'out1', eva, 'in1')



# Connections of the Heat Recovery Steam Generator
w_in_eco=Connection(w_in, 'out1',  eco, 'in2')
eco_in_dr=Connection(eco, 'out2', dr, 'in1')
dr_in_eva= Connection(dr, 'out1', eva, 'in2')
dr_w_out= Connection (dr, 'out2', w_out, 'in1')
eva_in_dr=Connection(eva, 'out2', dr, 'in2')
eva_in_eco=Connection(eva, 'out1', eco, 'in1')
eco_in_out=Connection(eco ,'out1', out, 'in1')


nw.add_conns(a_in_ac, ac_in_aph, aph_in_cc, fuel_in_va1, va1_in_cc,cc_in_exp,
             exp_in_aph, aph_in_eva,  dr_w_out, dr_in_eva, 
             eva_in_dr, w_in_eco,  eva_in_eco, eco_in_dr,eco_in_out
            )



power=Bus('power output')
power.add_comps({'comp':exp, 'char':1}, 
                {'comp':ac, 'char':1, 'base':'bus'})
nw.add_busses(power)


# Properties/Attributes of streams
a_in_ac.set_attr(m=91.28 ,T=298.15, p=1.013,  
                 fluid={'N2': 0.75767, 'H2O':0.0119,
                                    'CH4': 0, 'CO2': 0.00046, 'O2':  0.22997 })
fuel_in_va1.set_attr(T=298.15, p=12, 
                    fluid={'N2': 0, 'H2O': 0,
                                    'CH4': 1, 'CO2': 0, 'O2': 0})
aph_in_cc.set_attr(T=850)
cc_in_exp.set_attr(T=1520)

w_in_eco.set_attr(T=298.15, p=20, m=14, 
                   fluid={'N2': 0, 'H2O': 1,
                                   'CH4':0 , 'CO2': 0, 'O2': 0})

eco_in_dr.set_attr(Td_bp=-15)
eva_in_dr.set_attr(x=0.5)

eco_in_out.set_attr(p=1.013)


# Properties of Components
ac.set_attr(pr=10, eta_s=0.87)

aph.set_attr(pr1=0.97,pr2=0.95)   


cc.set_attr(pr=0.95, eta=0.98)

exp.set_attr(eta_s=0.86)

eva.set_attr(pr1=0.95)
eco.set_attr(pr1=0.95, pr2=1)


nw.solve('design')



power.set_attr(P=-30e6)

a_in_ac.set_attr(m=None)
nw.solve('design')
nw.print_results()

#Zusammensetzung des Rauchgases
# print(cc_in_exp.fluid.val)

#  #enthalpieberechnung mit dem KKH Modell mit der in TESPy vorliegenden Zusammensetzung
# h_fluegas=(0.761*kkh.enthalpy_mass('N2', 1520)+
#            0.049*kkh.enthalpy_mass('CO2', 1520)+
#            0.058*kkh.enthalpy_mass('H2Og', 1520)+
#            0.132*kkh.enthalpy_mass('O2', 1520))
    
# h_fluegas_0=(0.761*kkh.enthalpy_mass('N2', 298.15)+
#            0.049*kkh.enthalpy_mass('CO2', 298.15)+
#            0.058*kkh.enthalpy_mass('H2Og', 298.15)+
#            0.132*kkh.enthalpy_mass('O2', 298.15))
# # Enthalpie mit kkh im Vergleich, stimmt mit Penkuhn überein
# #print(kkh.enthalpy_mass('CH4', 298.15))

# #Enthalpie der Luft, Zusammensetztung aus TDO 
# h_air=(0.7748*kkh.enthalpy_mass('N2', 850)+
#            0.0003*kkh.enthalpy_mass('CO2', 850)+
#            0.019*kkh.enthalpy_mass('H2Og', 850)+
#            0.2059*kkh.enthalpy_mass('O2', 850))
# #print(h_air)

# #Vergleich der (h-h0) Werte der Unterschiedlichen Modelle (KKH und Coolprop)
# #bei gleicher Zusammenssetzung 
# print(h_fluegas-h_fluegas_0)

#h_fluegasCGAM0=(0.761*CPSI('H', 'T', 298.15, 'P', 101325, 'N2' )+
#                0.049*CPSI('H', 'T', 298.15, 'P', 101325,'CO2')+
#                 0.058*CPSI('H', 'T', 298.15, 'P', 101325,'H2O')+
#                 0.132*CPSI('H', 'T', 298.15, 'P', 101325,'O2'))

# h_fluegasCGAM=(0.761*CPSI('H', 'T', 1520, 'P', 914200, 'N2' )+
   #            0.049*CPSI('H', 'T', 1520, 'P', 914200,'CO2')+
    #           0.058*CPSI('H', 'T', 1520, 'P', 914200,'H2O')+
     #          0.132*CPSI('H', 'T', 1520, 'P', 914200,'O2'))
#print((h_fluegasCGAM-h_fluegasCGAM0)/1000)










