# -*- coding: utf-8 -*-
"""
@author: Karim
@author: Mathias Hofmann, TU Berlin
"""

# Values of standard chemical exergies of selected substances, adopted from
# Bakshi, B. R.; Gutowksi, T. G.; Sekulic, D. P. (Ed.): Thermodynamics and the Destruction of Resources, Cambridge University Press, Cambridge, 2011
# Szargut, J.: Egzergia. Widawnictwo Politechniki Shlaskej, Gliwice, Poland, 2007.
# Szargut, J.; Morris, D. R.; Steward F. R.: Exergy Analysis of Thermal, Chemical, and Metallurgical Processes, Hemisphere, New york, 1988.
# [kJ/mol]
#                                                 Szargut2007    Szargut1988
#                                                 Bakshi2011
Chem_Ex_Szargut = {
    '1BUTENE':                      ['106-98-9',   'NaN',         2659.7],  # g
    'ACETONE':                      ['67-64-1',    1797.3,        1788.5],  # l
    'AMMONIA':                      ['7664-41-7',  337.9,         337.9],   # g
    'ARGON':                        ['7440-37-1',  11.69,         11.69],   # g
    'BENZENE':                      ['71-43-2',    3301.3,        3303 .6], # g
    'BENZENE(l)':                   ['71-43-2',    3296.2,        3298 .5], # l
    'CARBONDIOXIDE':                ['124-38-9',   19.48,         19.87],   # g
    'CARBONMONOXIDE':               ['630-08-0',   274.71,        275.10],  # g
    'CARBONYLSULFIDE':              ['463-58-1',   'NaN',         'NaN'],
    'CYCLOHEXANE':                  ['110-82-7',   'NaN',         3914.3],  # g
    'CYCLOHEXANE(l)':               ['110-82-7',   'NaN',         3909.2],  # l
    'CYCLOPROPANE':                 ['75-19-4',    'NaN',         2043 .2], # g
    'CYCLOPENTANE':                 ['287-92-3',   'NaN',         'NaN'],
    'OCTAMETHYLCYCLOTETRASILOXANE': ['556-67-2',   'NaN',         'NaN'],
    'DECAMETHYLCYCLOPENTASILOXANE': ['541-02-6',   'NaN',         'NaN'],
    'DODECAMETHYLCYCLOHEXASILOXANE':['540-97-6',   'NaN',         'NaN'],
    'DEUTERIUM':                    ['7782-39-0',  263.8,         263.8],   # g
    '1,2-DICHLOROETHANE':           ['107-06-2',   'NaN',         'NaN'],
    'DEE':                          ['60-29-7',    'NaN',         'NaN'],
    'DIMETHYLCARBONATE':            ['616-38-6',   'NaN',         'NaN'],
    'DIMETHYLETHER':                ['15-10-6',    'NaN',         1419.5],  # g
    'ETHANE':                       ['74-84-0',    1495.0,        1495.84], # g
    'ETHANOL':                      ['64-17-5',    'NaN',         1363.9],  # g
    'ETHANOL(l)':                   ['64-17-5',    1356.9,        1357.7],  # l
    'ETHYLBENZENE':                 ['100-41-4',   'NaN',         4598.8],  # g
    'ETHYLBENZENE(l)':              ['100-41-4',   4584.8,        4587.9],  # l
    'ETHYLENE':                     ['74-85-1',    1360.3,        1361.1],  # g
    'ETHYLENEOXIDE':                ['75-21-8',    'NaN',         1284.4],  # g
    'FLUORINE':                     ['7782-41-4',  504.9,         466.3],   # g
    'HFE143M':                      ['421-14-7',   'NaN',         'NaN'],
    'HEAVYWATER':                   ['7789-20-0',  31.2,          31.2],    # g
    'HEAVYWATER(l)':                ['7789-20-0',  22.3,          22.3],    # l
    'HELIUM':                       ['7440-59-7',  30.37,         30.37],   # g
    'HYDROGEN':                     ['1333-74-0',  236.09,        236.1],   # g
    'HYDROGENCHLORIDE':             ['7647-01-0',  84.5,          84.5],    # g
    'HYDROGENSULFIDE':              ['7783-06-4',  812.0,         812.0],   # g
    'ISOBUTAN':                     ['75-28-5',    'NaN',         'NaN'],
    'ISOBUTENE':                    ['115-11-7',   'NaN',         'NaN'],
    'ISOHEXANE':                    ['107-83-5',   'NaN',         'NaN'],
    'ISOPENTANE':                   ['78-78-4',    'NaN',         'NaN'],
    'KRYPTON':                      ['7439-90-9',  34.36,         34.36],   # g
    'DECAMETHYLTETRASILOXANE':      ['141-62-8',   'NaN',         'NaN'],
    'DODECAMETHYLPENTASILOXANE':    ['141-63-9',   'NaN',         'NaN'],
    'TETRADECAMETHYLHEXASILOXANE':  ['107-52-8',   'NaN',         'NaN'],
    'OCTAMETHYLTRISILOXANE':        ['107-51-7',   'NaN',         'NaN'],
    'HEXAMETHYLDISILOXANE':         ['107-46-0',   'NaN',         'NaN'],
    'METHANE':                      ['74-82-8',    831.2,         831.65],  # g
    'METHANOL':                     ['67-56-1',    'NaN',         718.0],   # l
    'METHYLLINOLEATE':              ['112-63-0',   'NaN',         'NaN'],
    'METHYLLINOLENATE':             ['301-00-8',   'NaN',         'NaN'],
    'METHYLOLEATE':                 ['112-62-9',   'NaN',         'NaN'],
    'METHYLPALMITATE':              ['112-39-0',   'NaN',         'NaN'],
    'METHYLSTEARATE':               ['112-61-8',   'NaN',         'NaN'],
    'NEON':                         ['7440-01-9',  27.19,         27.19],  # g
    'NEOPENTANE':                   ['463-82-1',   'NaN',         'NaN'],
    'NITROGEN':                     ['7727-37-9',  0.72,          0.72],   # g
    'NITROUSOXIDE':                 ['10024-97-2', 106.9,         106.9],  # g

#
#
'PROPYLENE': ['115-07-1', 42.07974, 2.023, 6.264, 2.67],
'PROPYNE': ['74-99-7', 40.06386, 18.49, 19.384, 2.4836]




}



#
# MJ/kg
# Chem_ex_mass={'1-Butene':47.34, '1BUTENE':47.34, '1-BUTENE':47.34 ,'Butene':47.34,
#               'acetone':30.82, 'ACETONE':30.82,  'air':0, 'AIR':0, 'R729':0,
#               'NH3':19.85, 'ammonia':19.85, 'R717':19.85, 'AMMONIA':19.85 ,
#               'argon':0.29, 'Ar':0.29, 'ARGON':0.29, 'R740': 0.29,
#               'benzene': 42.24, 'BENZENE':42.24, 'R744':0.45, 'co2':0.45, 'CO2':0.45,
#               'carbondioxide':0.45, 'CARBONDIOXIDE':0.45, 'CO':13.97,
#               'CARBONMONOXIDE': 13.97, 'COS': np.nan, 'Cyclohexane':46.46,
#               'CYCLOHEXANE':46.46, 'CYCLOHEX':46.46, 'cyclopropane':48.56,
#               'Cyclopropane':48.56, 'CYCLOPROPANE':48.56, 'CYCLOPRO':48.56,
#               'CycloPentane':77.72, 'cyclopentane':77.72, 'CYCLOPENTANE':77.72,
#               'CYCLOPEN':77.72,'D2':65.49, 'deuterium':65.49, 'DEUTERIUM':65.49,
#               '1,2-dichloroethane':14.81, '1,2-DICHLOROETHANE':14.81,
#               'DICHLOROETHANE':14.81, 'DEE':36.45,'DiethylEther':36.45,
#               'DIMETHYLETHER':30.78, 'DME':30.78, 'ethane':49.78, 'ETHANE':49.78,
#               'R170':49.78,'n-C2H6':49.78, 'C2H6O':29.58, 'ethanol':29.58,
#               'ETHANOL':29.58, 'ETHYLBENZENE':43.27, 'EBENZENE':43.27,
#               'ethylbenzene':43.27, 'ETHYLENE':48.52, 'ethylene':48.52, 'R1150':48.52,
#               'ETHYLENEOXIDE':29.09, 'FLUORINE': 13.29, 'fluorine':13.29,'D2O':1.56,
#               'HEAVYWATER':1.56, 'HELIUM':7.59, 'helium':7.59, 'He':7.59,'R704':7.59,
#               'hydrogen':117.12, 'HYDROGEN':117.12, 'H2':117.12, 'R702':117.12,
#               'HYDROGENCHLORIDE':4.01, 'HydrogenChloride':4.01, 'HCL':4.01,
#               'HCl':4.01, 'HYDROGENSULFIDE':23.83, 'H2S':23.83, 'Isobutane':48.18,
#               'isobutane':48.18, 'ISOBUTANE':48.18, 'ISOBUTAN':48.18, 'R600A':48.18,
#               'R600a':48.18, 'ISOBUTENE':45.48, 'IBUTENE':45.48, 'Isobutene':45.48,
#               'ISOHEXANE':47.68, 'ihexane':47.68, 'ISOPENTANE':47.87, 'IPENTANE':47.87,
#               'ipentane':47.87, 'R601a': 47.87, 'krypton':0.41, 'KRYPTON':0.41,
#               'CH4':51.86, 'methane':51.86, 'METHANE':51.86,'R50':81.86
#               ,'n-C1H4':51.86, 'methanol':22.54, 'METHANOL':22.54, 'neon':1.35,
#               'NEON':1.35, 'R720':1.35, 'N2':0.026, 'nitrogen':0.026, 'NITROGEN':0.026,
#               'R728':0.026, 'N2O':2.43, 'NITROUSOXIDE':2.43, 'O2':0.12, 'oxygen':0.12,
#               'OXYGEN':0.12, 'R732':0.12, 'propylene':47.57, 'PROPYLENE':47.57,
#               'PROPYLEN':47.57, 'R1270':47.57, 'propyne':47.35, 'PROPYNE':47.35,
#               'R152a':20.56, 'Fluoroethane':30.19, 'FLUOROETHANE':30.19, 'R32':13.96,
#               'R40':16.36, 'MethylChloride':16.36, 'R41':23.699, 'SO2':4.89,
#               'SULFURDIOXIDE':4.89, 'SF6':6.9, 'SULFURHEXAFLUORIDE':6.9,'TOLUENE':42.74,
#               'toluene':42.74, 'water':0.53, 'WATER':0.53, 'h2o':0.53, 'H2O':0.53,
#               'R718':0.53, 'Xe':0.31, 'xenon':0.31, 'XENON':0.31, 'C2BUTENE':47.25,
#               'CIS-2-BUTENE':47.25, 'Cis-2-Butene':47.25, 'mXylene':43.15, 'm-xylene':43.15,
#               'M-XYLENE':43.15, 'MC8H10':43.15, 'butane':48.26, 'nButane':48.26,
#               'Butane':48.26, 'BUTANE':48.26, 'N-BUTANE':48.26, 'R600':48.26,
#               'NC4H10':48.26, 'n-C4H10':48.26, 'Decane':47.32, 'decane':47.32,
#               'DECANE':47.32, 'N-DECANE':47.32, 'NC10H22':47.32, 'n-C10H22':47.32,
#               'Dodecane':47.21, 'nDodecane':47.21, 'DODECANE':47.21, 'N-DODECANE':47.21,
#               'C12':47.21, 'NC12H26':47.21, 'n-C12H26':47.21, 'nHeptane':47.59,
#               'Heptane':47.59, 'HEPTANE':47.59, 'N-HEPTANE':47.59, 'NC7H16':47.59,
#               'n-C7H16':47.59, 'nHexane':47.74, 'Hexane':47.74, 'HEXANE':47.74,
#               'N-HEXANE':47.74, 'NC6H14':47.74, 'n-C6H14':47.74, 'nonane':47.39,
#               'Nonane':47.39, 'NONANE':47.39, 'N-NONANE':47.39, 'NC9H20':47.39,
#               'n-C9H20':47.39, 'nOctane':47.47, 'Octane':47.47, 'OCTANE':47.47,
#               'N-OCTANE':47.47, 'NC8H18':47.47, 'n-C8H18':47.47, 'nPentane':47.94,
#               'Pentane':47.94, 'PENTANE':47.94, 'N-PENTANE':47.94,'R601':47.94,
#               'NC5H12':47.94, 'n-C5H12':47.94, 'Propane':48.77, 'propane':48.77,
#               'R290':48.77, 'C3H8':48.77, 'PROPANE':48.77, 'N-PROPANE':48.77,
#               'NC3H8':48.77, 'n-C3H8':48.77, 'Undecane':47.26, 'UNDECANE':47.26,
#               'N-UNDECANE':47.26, 'C11':47.26, 'NC11H24':47.26, 'n-C11H24':47.26,
#               'oXylene':43.18, 'o-xylene':43.18, 'O-XYLENE':43.18, 'OC8H10':43.18,
#               'pXylene':43.18, 'p-xylene':43.18,'P-XYLENE':43.18, 'PC8H10':43.18,
#               'T2BUTENE':47.21, 'Trans-2-Butene':47.21, 'TRANS-2-BUTENE':47.21
#
#
#               }
#print(Chem_ex_mass['CH4'])
#liste von nicht berechneten stoffen D4, D5, D6, Demethylcarbonat,HFE-143m,
# MD2M,MD3M, MD4M, MDM, MM, Methyllinoleate ,Methyllinolenate, Methyloleate,
#Methylpalmitate, Methylstearate, neopentane, Novec649, Orthodeuterium (keine Summenformel),
#Orthohydrogen (keine Summenformel und nicht Refprop), Paradeuterium (keine Summenformel
# und nicht in Refprop), Parahydrogen (siehe Paradeuterium), R11, R113, R114, R115, R116,
#R12,R123, R123zd(E), R1234yf, R1234ze(E), R1234ze(Z),R124, R1243zf, R125, R13, R134a, 
#R13I1, R14, R141b, R142b, R143b, R21, R218, R22, R227EA, R23, R236EA, R236FA, R245CA,
#R245FA, R365MFC, R404a, R407a, R410A, R507A, RC318, SES36, 
