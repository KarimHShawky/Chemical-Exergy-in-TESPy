#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd

from CoolProp.CoolProp import PropsSI as CPSI

from tespy.networks import Network
from tespy.components import DiabaticCombustionChamber, Sink, Source
from tespy.connections import Connection

backend = 'HEOS::'
fluid_list = ['O2', 'H2O', 'N2', 'CO2', 'CH4']
nwk = Network(fluids=[backend + f for f in fluid_list], p_unit='bar', T_unit='C', h_range=[-1e9, 1e7])

air_molar = {
    'O2': 0.2059, 'N2': 0.7748, 'CO2': 0.0003, 'H2O': 0.019, 'CH4': 0
}
molar_masses = {key: CPSI('M', key) * 1000 for key in air_molar}
M_air = sum([air_molar[key] * molar_masses[key] for key in air_molar])

air = {key: value / M_air * molar_masses[key] for key, value in air_molar.items()}

water = {f: (0 if f != 'H2O' else 1) for f in air}
fuel = {f: (0 if f != 'CH4' else 1) for f in air}

amb = Source('ambient air')
ch4 = Source('methane')

ch = Sink('chimney')

cb = DiabaticCombustionChamber('combustion chamber')

c3 = Connection(amb, 'out1', cb, 'in1', label='3')
c10 = Connection(ch4, 'out1', cb, 'in2', label='10')
c4 = Connection(cb, 'out1', ch, 'in1', label='4')

nwk.add_conns(c3, c4, c10)

c3.set_attr(p=10.13 * 0.95, T=850 - 273.15, fluid=air, m=91.2757)
c4.set_attr(T=1520 - 273.15)
c10.set_attr(T=25, fluid=fuel, p=12)

cb.set_attr(eta=0.98, pr=0.95)

nwk.solve('design')
nwk.print_results()

for idx in nwk.results["Connection"].index:
    c = nwk.get_conn(idx)

    molarflow = {key: value / molar_masses[key] * c.m.val_SI * 1000 for key, value in c.fluid.val.items()}
    molar = {key: value / sum(molarflow.values()) for key, value in molarflow.items()}

    nwk.results["Connection"].loc[idx, molar.keys()] = molar

nwk.results["Connection"].to_csv('cgam-combustion-coolprop-results.csv')
