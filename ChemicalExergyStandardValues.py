# -*- coding: utf-8 -*-
"""
@author: Karim
@author: Mathias Hofmann, TU Berlin
"""

import CoolProp.CoolProp as CP
import re

# Values of standard chemical exergies of the elements, adopted from
# Szargut et al. [QUELLE]
Chem_Ex_Elements = {'Ag': 70.2, 'Al': 988.2, 'Ar': 11.69, 'As': 494.6, 'Au': 50.5, 'B': 628.5, 'Ba': 775.1, 'Be': 604.4,
                  'Bi': 274.5, 'Br': 101.2, 'C': 410.26, 'Ca': 729.1, 'Cd': 293.8, 'Ce': 1054.6, 'Cl': 123.6, 'Co': 312,
                  'Cr': 584.3, 'Cs': 404.4, 'Cu': 134.2, 'D2': 263.8, 'Dy': 975.9, 'Er': 972.8, 'Eu': 1003.8,
                  'F2': 504.9, 'Fe': 374.3, 'Ga': 514.9, 'Gd': 969, 'Ge': 557.6, 'H2': 236.09, 'He': 30.37,
                  'Hf': 1062.9, 'Hg': 115.9, 'Ho': 978.6, 'I': 174.7, 'In': 436.8, 'Ir': 246.8, 'K': 366.6, 'Kr': 34.36,
                  'La': 994.6, 'Li': 393, 'Lu': 945.7, 'Mg': 626.1, 'Mn': 482, 'Mo': 730.3, 'N2': 0.72, 'Na': 336.6,
                  'Nb': 899.7, 'Nd': 970.1, 'Ne': 27.19, 'Ni': 232.7, 'O2': 3.97, 'Os': 368.1, 'P': 861.4, 'Pb': 232.8,
                  'Pd': 138.6, 'Pr': 963.8, 'Pt': 141, 'Pu': 1100, 'Ra': 823.9, 'Rb': 388.6, 'Re': 559.5, 'Rh': 179.7,
                  'Ru': 318.6, 'S': 609.6, 'Sb': 438.1, 'Sc': 925.2, 'Se': 346.5, 'Si': 854.9, 'Sm': 993.6, 'Sn': 551.9,
                  'Sr': 749.8, 'Ta': 974, 'Tb': 998.4, 'Te': 329.2, 'Th': 1202.6, 'Ti': 907.2, 'Tl': 194.9, 'Tm': 951.7,
                  'U': 1196.6, 'V': 720.4, 'W': 827.5, 'Xe': 40.33, 'Y': 965.5, 'Yb': 944.3, 'Zn': 339.2,
                    'Zr': 1083.4}  # kJ/mol

# Values of enthalpy of formation (HoF), Gibbs energy of formation (GoF), and entropy of formation (SoF), adopted from
# Perry's Chemical Engineers' Handbook, 9th Edition, pp. 2-167
#       --           -                    kg/mol    kJ/mol   kJ/mol kJ/Kmol
#                                                      e-1    e-1    e-1
#       Fluid                    CAS       Mol.wght   HoF     GoF    SoF
Formation_Values = {
    '1-Butene':           ['106-98-9',  56.10632,  -0.05,  7.041, 3.074],
    'Acetone':            ['67-64-1',   58.07914, -21.57, -15.13, 2.954],
    'Ammonia':            ['7664-41-7', 17.03052, -4.5898, -1.64, 1.927],
    'Benzene':            ['71-43-2',   78.11184,  8.288,  12.96, 2.693],
    'Carbon dioxide':     ['124-38-9',  44.0095, -39.351, -39.437, 2.137],
    'Carbon monoxide':    ['630-08-0',  28.0101, -11.053, -13.715, 1.976],
    'Cyclohexane':        ['110-82-7',  84.15948, -12.33,   3.191, 2.973],
    'Cyclopropane':       ['75-19-4',  42.07974,  5.33,   10.44,  2.374],
    'Cyclopentane':       ['287-92-3', 70.1329, -7.703,   3.885,  2.929],
    '1,2-Dichloroethane': ['107-06-2', 98.95916, -12.979, -7.3945, 3.0828],
    'Diethyl ether ':     ['60-29-7', 74.1216,   -25.21, -12.21,  3.423],
    'Dimethyl ether':     ['15-10-6', 46.06844, -18.41, -11.28, 2.667],
    'Ethane':             ['74-84-0',  30.069,  -8.382, -3.192, 2.2912],
    'Ethanol':            ['64-17-5', 46.06844, -23.495, -16.785, 2.8064],
    'Ethylbenzene':       ['100-41-4', 106.165,  2.992, 13.073, 3.6063],
    'Ethylene':           ['74-85-1', 28.05316,  5.251, 6.844, 2.192],
    'Ethylene oxide':     ['75-21-8', 44.05256, -5.263, -1.323, 2.4299],
    'Hydrogen chloride':  ['7647-01-0', 36.46094, -9.231, -9.53, 1.86786],
    'Hydrogen sulfide':   ['7783-06-4', 34.08088, -2.063, -3.344, 2.056],
    '2-Methylpropane':    ['75-28-5', 58.1222, -13.499, -2.144, 2.955],
    '2-Methyl propene':   ['115-11-7', 56.10632, -1.71, 5.808, 2.9309],
    '2-Methylpentane':    ['107-83-5', 86.17536, -17.455, -0.5338, 3.8089],
    '2-Methylbutane':     ['78-78-4', 72.14878, -15.37, -1.405, 3.4374],
    'Methane':            ['74-82-8', 16.0425, -7.452, -5.049, 1.8627],
    'Methanol':           ['67-56-1', 32.04186, -20.094, -16.232, 2.3988],
    'Nitrous oxide':      ['10024-97-2', 44.0128, 8.205, 10.416, 2.1985],
    'Propylene':          ['115-07-1', 42.07974, 2.023, 6.264, 2.67],
    'Methyl acetylene':   ['74-99-7', 40.06386, 18.49, 19.384, 2.4836], #R
    '1,1-Difluoroethane': ['75-37-6', 66.04997, -49.7, -43.9485, 2.824], #R
    'Fluoroethane':       ['353-36-6', 48.0595, -26.44, -21.23, 2.644], #R
    'Difluoromethane':    ['75-10-5', 52.02339, -45.23, -42.4747, 2.4658], #R
    'Chloromethane':      ['74-87-3', 50.4875, -8.57, -6.209, 2.341], #R
    'Fluoromethane':      ['593-53-3', 34.03292, -23.43, -21.03, 2.22734], #R41
    'Sulfur dioxide':     ['7446-09-5', 64.0638, -29.684, -30.012, 2.481],
    'Sulfur hexafluoride':['2551-62-4', 146.0554192, -122.047, -111.653, 2.91625],
    'Toluene':            ['108-88-3', 92.13842, 5.017, 12.22, 3.2099],
    'cis-2-Butene':       ['590-18-1', 56.10632, -0.74, 6.536, 3.012],
    'm-Xylene':           ['108-38-3', 106.165, 1.732, 11.876, 3.5854],
    'Butane':             ['106-97-8', 58.1222, -12.579,-1.67, 3.0991],
    'Decane':             ['124-18-5', 142.28168, -24.946,3.318, 5.457],
    'Dodecane':           ['112-40-3', 170.33484, -29.072,4.981, 6.2415],
    'Heptane':            ['142-82-5', 100.20194, -18.765, 0.8165, 4.2798],
    'Hexane':             ['110-54-3', 86.17536, -16.694, -0.006634, 3.8874],
    'Nonane':             ['111-84-2', 128.2551, -22.874, 2.498, 5.064],
    'Octane':             ['111-65-9', 114.22852, -20.875, 1.6, 4.6723],
    'Pentane':            ['109-66-0', 72.14878, -14.676, -0.8813, 3.4945],
    'Propane':            ['74-98-6', 44.09562, -10.468, -2.439, 2.702],
    'Undecane':           ['1120-21-4', 156.30826, -27.043, 4.116, 5.8493],
    'o-Xylene':           ['95-47-6', 106.165, 1.908, 12.2, 3.5383],
    'p-Xylene':           ['106-42-3', 106.165, 1.803, 12.14, 3.52165],
    'trans-2-Butene':     ['624-64-6', 56.10632, -1.1, 6.32, 2.965]
}

# Function to calculate mass/molar specific standard chemical exergy of fluid = fld
def chem_ex_calc(fld):
    fluid_elements = re.findall(r'(\w+)_{(\d+)', CP.get_fluid_param_string(fld, 'formula'))
    fluid_chem_ex = 0

    for i in fluid_elements:
        if i[0] in ['D', 'F', 'H', 'N', 'O']:
            fluid_chem_ex += Chem_Ex_Elements.get(i[0] + "2") * int(i[1]) / 2
        else:
            fluid_chem_ex += Chem_Ex_Elements.get(i[0]) * int(i[1])

    fluid_chem_ex += Formation_Values[fld][3] * 1e1

#    return fluid_chem_ex / CP.PropsSI('M', fld)
    return fluid_chem_ex

# Über alle Coolprop Stoffe iterieren
# Skippen für nicht Standard stoffe müsste noch gemacht werden
#for f in CP.FluidsList():
#    print(f, chem_ex_calc(f))

#for f in Formation_Values:
#    print(f, chem_ex_calc(f))

# einen bestimmten Stoff vorgeben
Fluid_Name = 'Methane'
print(Fluid_Name, chem_ex_calc(Fluid_Name))
Fluid_Name = 'Ethane'
print(Fluid_Name, chem_ex_calc(Fluid_Name))
Fluid_Name = 'Propane'
print(Fluid_Name, chem_ex_calc(Fluid_Name))


# einen bestimmten Stoff vorgeben
#Fluid_Name = 'methane'
#Fluid_Name_Refprop = CP.get_fluid_param_string(Fluid_Name, 'REFPROP_name')
#Fluid_Elements = re.findall(r'(\w+)_{(\d+)', CP.get_fluid_param_string(Fluid_Name, 'formula'))
#Fluid_Chem_Ex = 0

#for i in Fluid_Elements:
#    if i[0] in ['D', 'F', 'H', 'N', 'O']:
#        Fluid_Chem_Ex += Chem_Ex_Elements.get(i[0] + "2") * int(i[1]) / 2
#    else:
#        Fluid_Chem_Ex += Chem_Ex_Elements.get(i[0]) * int(i[1])
#
#print(Fluid_Name_Refprop, Fluid_Chem_Ex/(CP.PropsSI('M', Fluid_Name)))


# #GoF in kJ/mol
# #GoF manual input from the user
# def ChemExCalc (Ele1, Nr1, Ele2, Nr2, Ele3, Nr3, Ele4, Nr4, name, GoF) :
#
#              a=(GoF+
#               Nr1*szargut[Ele1]+
#               Nr2*szargut[Ele2]+
#               Nr3*szargut[Ele3]+
#               Nr4*szargut[Ele4])  /(CP.PropsSI('M',name) )
#
#           #Coolprop gibt Molmasse als kg/mol
#
#              return a
#
#
# i=ChemExCalc( 'H2', 4, 'O2', 0, 'C', 4, 'Xe',0, 'T2BUTENE', 63.2)
# print(i)
