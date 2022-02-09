# -*- coding: utf-8 -*-
"""
@author: Mathias Hofmann
Technische Universitaet Berlin, Fachgebiet Energietechnik und Umweltschutz
Berechnung Heizwert aus Standardbildungsenthalpien
"""

import CoolProp.CoolProp as CP

# https://webbook.nist.gov/chemistry/name-ser/
# ΔfH°gas or ΔfH°liquid
# (0) Chase, 1998
# (1) CODATA, 1984
# (2) Manion, 2002
# (3) Pittam and Pilcher, 1972
# (4) Prosen and Rossini, 1945 or Prosen, Maron, et al., 1951
# (5) Prosen and Rossini, 1945, 2 (Heat of formation derived by Cox and Pilcher, 1970)

# (6) CRC Handbook, Vol. 97, pp. 5-3, ΔfH°(g), ΔfH°(l)

# ΔfH°gas or ΔfH°liquid
# kJ/mol
# Sources              (0)       (1)       (2)    (3)     (4)     (5)     (6)
hf = {'hydrogen':      [0.0,     0.0,      'NaN', 'NaN',  'NaN',  'NaN',  0.0],
      'oxygen':        [0.0,     0.0,      'NaN', 'NaN',  'NaN',  'NaN',  0.0],
      'water(g)':      [-241.83, -241.826, 'NaN', 'NaN',  'NaN',  'NaN',  -241.8],
      'water(l)':      [-285.83, -285.830, 'NaN', 'NaN',  'NaN',  'NaN',  -285.8],
      'carbon':        [0.0,     0.0,      'NaN', 'NaN',  'NaN',  'NaN',  0.0],
      'carbondioxide': [-393.52, -393.51,  'NaN', 'NaN',  'NaN',  'NaN',  -393.5],
      'methane':       [-74.87,  'NaN',    -74.6, -74.5,  -74.85, 'NaN',  -74.6],
      'ethane':        ['NaN',   'NaN',    -84.0, -83.8,  -84.67, 'NaN',  -84.0],
      'propane':       ['NaN',   'NaN',    'NaN', -104.7, -103.8, 'NaN',  -103.8],
      'butane':        ['NaN',   'NaN',    'NaN', -125.6, -127.1, 'NaN',  -125.7],
      'dodecane':      ['NaN',   'NaN',    'NaN', 'NaN',  -290.9, -288.1, -289.4]}

# C_k0 H_k1 + (k0+(k1)/4) O2 --> k0 CO2 + (k1)/2 H2O
#                0   1
k = {'methane': [1,  4],
     'ethane':  [2,  6],
     'propane': [3,  8],
     'butane':  [4,  10],
     'dodecane':[12, 26]}

# Calculation of mass specific lower heating value, LHV in kJ/kg
# Oxygen not in equation cause hf['oxygen'] = 0.0
def lower_hv_mass(s,q):
    lhv = -(-1 * hf[s][q] + k[s][0] * hf['carbondioxide'][1] + k[s][1] / 2 * hf['water(g)'][1])
    lhv_mass = lhv / CP.PropsSI('M', s)
    return lhv_mass

# Give Substance name and source number of hf-value
print(lower_hv_mass('methane',2))