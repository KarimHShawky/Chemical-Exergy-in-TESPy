# -*- coding: utf-8 -*-
"""
@author: Karim
@author: Mathias Hofmann, TU Berlin
"""

from libChemExElementsSzargut1989 import *
from libFormationValues import *
import CoolProp.CoolProp as CP
import re
from contextlib import redirect_stdout

# Function to calculate molar specific standard chemical exergy [kJ/mol] of fluid = fld
def chem_ex_calc(fld):
    fluid_elements = re.findall(r'(\w+)_{(\d+)', CP.get_fluid_param_string(fld, 'formula'))
    fluid_chem_ex = 0

    for i in fluid_elements:
        if i[0] in ['D', 'F', 'H', 'N', 'O']:
            fluid_chem_ex += Chem_Ex_Elements.get(i[0] + "2") * int(i[1]) / 2
        else:
            fluid_chem_ex += Chem_Ex_Elements.get(i[0]) * int(i[1])

    fluid_chem_ex += Formation_Values[fld][3] * 1e1

    return fluid_chem_ex

# Function call for every fluid with from Formation_Values (subset of CoolProp)
# Write results to file:
# Fluid,
# CAS-No.,
# molar specific standard chemical exergy [kJ/mol],
# mass specific standard chemical exergy [kJ/kg],

Chem_Ex_Results = {}

for f in Formation_Values:
    Chem_Ex_Results[f] = [Formation_Values[f][0], chem_ex_calc(f), chem_ex_calc(f) / CP.PropsSI('M', f) * 1E-3]

with open('libChemExResults.py', 'w') as f:
    with redirect_stdout(f):
        print('Chem_Ex_Results =', Chem_Ex_Results)