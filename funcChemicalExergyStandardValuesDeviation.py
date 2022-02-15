# -*- coding: utf-8 -*-
"""
@author: Karim
@author: Mathias Hofmann, TU Berlin
"""

from libChemExSzargut import *
from libChemExResults import *


# Calculate relative deviation of standard chemical exergies calculated based on this approach
Chem_Ex_Deviation = {}

for f in Chem_Ex_Szargut:
    if type(Chem_Ex_Szargut[f][2]) == float:
        Chem_Ex_Deviation[f] = (Chem_Ex_Szargut[f][2] / Chem_Ex_Results[f][1] - 1) * 100
    else:
        Chem_Ex_Deviation[f] = 'Nan'

print(Chem_Ex_Deviation)
