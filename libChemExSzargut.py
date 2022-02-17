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
    'BENZENE':                      ['71-43-2',    3301.3,        3303.6], # g
    'BENZENE(l)':                   ['71-43-2',    3296.2,        3298.5], # l
    'CARBONDIOXIDE':                ['124-38-9',   19.48,         19.87],   # g
    'CARBONMONOXIDE':               ['630-08-0',   274.71,        275.10],  # g
    'CARBONYLSULFIDE':              ['463-58-1',   'NaN',         'NaN'],
    'CYCLOHEXANE':                  ['110-82-7',   'NaN',         3914.3],  # g
    'CYCLOHEXANE(l)':               ['110-82-7',   'NaN',         3909.2],  # l
    'CYCLOPROPANE':                 ['75-19-4',    'NaN',         2043.2], # g
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
    'NOVEC649':                     ['756-13-8',   'NaN',         'NaN'],
    'ORTHODEUTERIUM':               ['7782-39-0o', 'NaN',         'NaN'],
    'ORTHOHYDROGEN':                ['1333-74-0o', 'NaN',         'NaN'],
    'OXYGEN':                       ['7782-44-7',  3.97,          3.97],   # g
    'PARADEUTERIUM':                ['7782-39-0p', 'NaN',         'NaN'],
    'PARAHYDROGEN':                 ['1333-74-0p', 'NaN',         'NaN'],
    'PROPYLENE':                    ['115-07-1',   2002.7,        2003.9], # g
    'PROPYNE':                      ['74-99-7',    'NaN',         1899.5], # g
    'R11':                          ['75-69-4',    'NaN',         'NaN'],
# R ...
    'SULFURDIOXIDE':                ['7446-09-5',  313.4,         313.4],  # g
    'SULFURHEXAFLUORIDE':           ['2551-62-4',  'NaN',         'NaN'],
    'TOLUENE':                      ['108-88-3',   'NaN',         3943.4], # g
    'TOLUENE(l)':                   ['108-88-3',   3928.3,        3931.0], # l
    'WATER':                        ['7732-18-5',  9.5,           9.5],    # g
    'WATER(l)':                     ['7732-18-5',  0.9,           0.9],    # l
    'XENON':                        ['7440-63-3',  40.33,         40.33],  # g
    'C2BUTENE':                     ['590-18-1',  'NaN',         'NaN'],
    'M-XYLENE':                     ['108-38-3',  'NaN',         'NaN'],
    'N-BUTANE':                     ['106-97-8',  2804.2,        2805.8],  # g
    'N-DECANE':                     ['124-18-5',  'NaN',         6716.89], # l
    'N-DODECANE':                   ['112-40-3',  'NaN',         8029.4],  # l
    'N-HEPTANE':                    ['142-82-5',  'NaN',         4761.7],  # l
    'N-HEXANE':                     ['110-54-3',  'NaN',         4118.5],  # g
    'N-HEXANE(l)':                  ['110-54-3',  'NaN',         4114.5],  # l
    'N-NONANE':                     ['111-84-2',  'NaN',         6064.9],  # l
    'N-OCTANE':                     ['111-65-9',  'NaN',         5413.1],  # l
    'N-PENTANE':                    ['109-66-0',  3461.3,        3463.3],  # g
    'N-PENTANE(l)':                 ['109-66-0',  'NaN',         3461.8],  # l
    'N-PROPANE':                    ['74-98-6',   2152.8,        2154.0],  # g
    'N-UNDECANE':                   ['1120-21-4', 'NaN',         7376.9],  # l
    'O-XYLENE':                     ['95-47-6',   'NaN',         4513.1],  # l
    'P-XYLENE':                     ['106-42-3',  'NaN',         'NaN'],
    'T2BUTENE':                     ['624-64-6',  'NaN',         'NaN'],
}

"""
'1,1-Difluoroethane': ['75-37-6',
'Fluoroethane':       ['353-36-6',
'Difluoromethane': ['75-10-5',
'Chloromethane':      ['74-87-3',
'Fluoromethane': ['593-53-3',
"""