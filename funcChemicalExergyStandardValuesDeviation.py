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
    Chem_Ex_Deviation[f] = (Chem_Ex_Szargut[f][1] / Chem_Ex_Results[f][1] - 1) * 100

print(Chem_Ex_Deviation)
