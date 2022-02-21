#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd

from CoolProp.CoolProp import PropsSI as CPSI

from tespy.networks import Network
from tespy.components import DiabaticCombustionChamber, Sink, Source
from tespy.connections import Connection

from tespy.tools.kkh import enthalpy_mass, enthalpy
from tespy.tools.fluid_properties import molar_mass_flow

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

c3 = Connection(amb, 'out1', cb, 'in2', label='3')
c12 = Connection(ch4, 'out1', cb, 'in1', label='12')
c4 = Connection(cb, 'out1', ch, 'in1', label='4')

nwk.add_conns(c3, c4, c12)

c3.set_attr(p=10, T=850 - 273.15, fluid=air, m=91.2757)
c4.set_attr(T=1520 - 273.15)
c12.set_attr(T=25, fluid=fuel, p=12)

cb.set_attr(eta=0.98, pr=0.95)

nwk.solve('design')
nwk.print_results()

fluegas = c4.fluid.val

fluegas_molarflow = {key: value / molar_masses[key] * c4.m.val_SI * 1000 for key, value in fluegas.items()}

fluegas_molar = {key: value / sum(fluegas_molarflow.values()) for key, value in fluegas_molarflow.items()}
M_fluegas = sum([fluegas_molar[key] * molar_masses[key] for key in fluegas_molar])

result = pd.DataFrame(
    columns=[
        "air_molar", "air_mass", "air_massflow",
        "fuel_molar", "fuel_mass", "fuel_massflow",
        "fluegas_molar", "fluegas_mass", "fluegas_massflow"
    ],
    index=air.keys()
)

result["air_molar"] = pd.Series(air_molar)
result["air_mass"] = pd.Series(air)
result["air_massflow"] = result["air_mass"] * c3.m.val_SI

result["fuel_molar"] = pd.Series(fuel)
result["fuel_mass"] = pd.Series(fuel)
result["fuel_massflow"] = result["fuel_mass"] * c12.m.val_SI

result["fluegas_molar"] = pd.Series(fluegas_molar)
result["fluegas_mass"] = pd.Series(fluegas)
result["fluegas_massflow"] = result["fluegas_mass"] * c4.m.val_SI

result.loc["sum"] = result.sum()

result.to_csv('CGAM_combustion_CoolProp.csv')
