# -*- coding: utf-8 -*-
"""
@author: karim
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

#delta G Werte hier listen


# Function to calculate mass specific standard chemical exergy of fluid = fld
def chem_ex_calc(fld):
    fluid_elements = re.findall(r'(\w+)_{(\d+)', CP.get_fluid_param_string(fld, 'formula'))
    fluid_chem_ex = 0

    for i in fluid_elements:
        if i[0] in ['D', 'F', 'H', 'N', 'O']:
            fluid_chem_ex += Chem_Ex_Elements.get(i[0] + "2") * int(i[1]) / 2
        else:
            fluid_chem_ex += Chem_Ex_Elements.get(i[0]) * int(i[1])

    return fluid_chem_ex / CP.PropsSI('M', fld)


# Über alle Coolprop Stoffe iterieren
# Skippen für nicht Standard stoffe müsste noch gemacht werden
for f in CP.FluidsList():
    print(f, chem_ex_calc(f))

# einen bestimmten Stoff vorgeben
Fluid_Name = 'methane'
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
#              a=(-(GoF)+
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
# i=ChemExCalc( 'H2', 4, 'O2', 0, 'C', 4, 'Xe',0, 'T2BUTENE', -63.2)
# print(i)