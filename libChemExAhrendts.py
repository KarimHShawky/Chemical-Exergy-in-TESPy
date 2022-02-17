# -*- coding: utf-8 -*-
"""
@author: Mathias Hofmann, TU Berlin
"""

# Values of standard chemical exergies of selected substances, adopted from
# Ahrendts, J.: Die Exergie chemisch reaktionsfähiger Systeme, Ruhr-Universität-Bochum, Dissertation, 1974
# Ahrendts, J.: Die Exergie chemisch reaktionsfähiger Systeme, VDI-Forschungsheft 579, VDI-Verlag, Düsseldorf, 1977
# Ahrendts, J.: Reference states, Energy (5), 1980, pp. 667-677
# [kJ/mol]
#
Chem_Ex_Ahrendts = {
    '1BUTENE':                      ['106-98-9',      'NaN'],  # g
    'ACETONE':                      ['67-64-1',       'NaN'],  # l
    'AMMONIA':                      ['7664-41-7',     336.684],   # g              
    'ARGON':                        ['7440-37-1',     11.627],   # g
    'BENZENE':                      ['71-43-2',       'NaN'], # g
    'BENZENE(l)':                   ['71-43-2',       'NaN'], # l
    'CARBONDIOXIDE':                ['124-38-9',      14.176],   # g
    'CARBONMONOXIDE':               ['630-08-0',      269.412],  # g
    'CARBONYLSULFIDE':              ['463-58-1',      'NaN'],
    'CYCLOHEXANE':                  ['110-82-7',      'NaN'],  # g
    'CYCLOHEXANE(l)':               ['110-82-7',      'NaN'],  # l
    'CYCLOPROPANE':                 ['75-19-4',       'NaN'], # g
    'CYCLOPENTANE':                 ['287-92-3',      'NaN'],
    'OCTAMETHYLCYCLOTETRASILOXANE': ['556-67-2',      'NaN'],
    'DECAMETHYLCYCLOPENTASILOXANE': ['541-02-6',      'NaN'],
    'DODECAMETHYLCYCLOHEXASILOXANE':['540-97-6',      'NaN'],
    'DEUTERIUM':                    ['7782-39-0',     3.951],   # g
    '1,2-DICHLOROETHANE':           ['107-06-2',      'NaN'],
    'DEE':                          ['60-29-7',       'NaN'],
    'DIMETHYLCARBONATE':            ['616-38-6',      'NaN'],
    'DIMETHYLETHER':                ['15-10-6',       'NaN'],  # g
    'ETHANE':                       ['74-84-0',       1482.033], # g
    'ETHANOL':                      ['64-17-5',       1348.328],  # g
    'ETHANOL(l)':                   ['64-17-5',       1342.086],  # l
    'ETHYLBENZENE':                 ['100-41-4',      'NaN'],  # g
    'ETHYLBENZENE(l)':              ['100-41-4',      'NaN'],  # l
    'ETHYLENE':                     ['74-85-1',       'NaN'],  # g
    'ETHYLENEOXIDE':                ['75-21-8',       'NaN'],  # g
    'FLUORINE':                     ['7782-41-4',     'NaN'],   # g
    'HFE143M':                      ['421-14-7',      'NaN'],
    'HEAVYWATER':                   ['7789-20-0',     'NaN'],    # g
    'HEAVYWATER(l)':                ['7789-20-0',     'NaN'],    # l
    'HELIUM':                       ['7440-59-7',     'NaN'],   # g
    'HYDROGEN':                     ['1333-74-0',     235.249],   # g
    'HYDROGENCHLORIDE':             ['7647-01-0',     79.759],    # g
    'HYDROGENSULFIDE':              ['7783-06-4',     799.890],   # g
    'ISOBUTAN':                     ['75-28-5',       'NaN'],
    'ISOBUTENE':                    ['115-11-7',      'NaN'],
    'ISOHEXANE':                    ['107-83-5',      'NaN'],
    'ISOPENTANE':                   ['78-78-4',       'NaN'],
    'KRYPTON':                      ['7439-90-9',     'NaN'],   # g
    'DECAMETHYLTETRASILOXANE':      ['141-62-8',      'NaN'],
    'DODECAMETHYLPENTASILOXANE':    ['141-63-9',      'NaN'],
    'TETRADECAMETHYLHEXASILOXANE':  ['107-52-8',      'NaN'],
    'OCTAMETHYLTRISILOXANE':        ['107-51-7',      'NaN'],
    'HEXAMETHYLDISILOXANE':         ['107-46-0',      'NaN'],
    'METHANE':                      ['74-82-8',       824.348],  # g
    'METHANOL':                     ['67-56-1',       710.747],  # g
    'METHANOL(l)':                  ['67-56-1',       715.069],  # l
    'METHYLLINOLEATE':              ['112-63-0',      'NaN'],
    'METHYLLINOLENATE':             ['301-00-8',      'NaN'],
    'METHYLOLEATE':                 ['112-62-9',      'NaN'],
    'METHYLPALMITATE':              ['112-39-0',      'NaN'],
    'METHYLSTEARATE':               ['112-61-8',      'NaN'],
    'NEON':                         ['7440-01-9',     'NaN'],  # g
    'NEOPENTANE':                   ['463-82-1',      'NaN'],
    'NITROGEN':                     ['7727-37-9',     0.639],   # g
    'NITROUSOXIDE':                 ['10024-97-2',    106.807],  # g
    'NOVEC649':                     ['756-13-8',      'NaN'],
    'ORTHODEUTERIUM':               ['7782-39-0o',    'NaN'],
    'ORTHOHYDROGEN':                ['1333-74-0o',    'NaN'],
    'OXYGEN':                       ['7782-44-7',     3.951],   # g
    'PARADEUTERIUM':                ['7782-39-0p',    'NaN'],
    'PARAHYDROGEN':                 ['1333-74-0p',    'NaN'],
    'PROPYLENE':                    ['115-07-1',      'NaN'], # g
    'PROPYNE':                      ['74-99-7',       'NaN'], # g
    'R11':                          ['75-69-4',       'NaN'],
# R ...
    'SULFURDIOXIDE':                ['7446-09-5',     301.939],  # g
    'SULFURHEXAFLUORIDE':           ['2551-62-4',     'NaN'],
    'TOLUENE':                      ['108-88-3',      'NaN'], # g
    'TOLUENE(l)':                   ['108-88-3',      'NaN'], # l
    'WATER':                        ['7732-18-5',     8.636],    # g
    'WATER(l)':                     ['7732-18-5',     0.045],    # l
    'XENON':                        ['7440-63-3',     'NaN'],  # g
    'C2BUTENE':                     ['590-18-1',      'NaN'],
    'M-XYLENE':                     ['108-38-3',      'NaN'],
    'N-BUTANE':                     ['106-97-8',      'NaN'],  # g
    'N-DECANE':                     ['124-18-5',      'NaN'], # l
    'N-DODECANE':                   ['112-40-3',      'NaN'],  # l
    'N-HEPTANE':                    ['142-82-5',      'NaN'],  # l
    'N-HEXANE':                     ['110-54-3',      'NaN'],  # g
    'N-HEXANE(l)':                  ['110-54-3',      'NaN'],  # l
    'N-NONANE':                     ['111-84-2',      'NaN'],  # l
    'N-OCTANE':                     ['111-65-9',      'NaN'],  # l
    'N-PENTANE':                    ['109-66-0',      'NaN'],  # g
    'N-PENTANE(l)':                 ['109-66-0',      'NaN'],  # l
    'N-PROPANE':                    ['74-98-6',       'NaN'],  # g
    'N-UNDECANE':                   ['1120-21-4',     'NaN'],  # l
    'O-XYLENE':                     ['95-47-6',       'NaN'],  # l
    'P-XYLENE':                     ['106-42-3',      'NaN'],
    'T2BUTENE':                     ['624-64-6',      'NaN'],
}

"""
'1,1-Difluoroethane': ['75-37-6',
'Fluoroethane':       ['353-36-6',
'Difluoromethane': ['75-10-5',
'Chloromethane':      ['74-87-3',
'Fluoromethane': ['593-53-3',
"""