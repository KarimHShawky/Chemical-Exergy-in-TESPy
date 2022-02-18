# -*- coding: utf-8 -*-
"""
@author: Karim
@author: Mathias Hofmann, TU Berlin
"""

# Values of standard chemical exergies of selected substances, adopted from
# Bakshi, B. R.; Gutowksi, T. G.; Sekulic, D. P. (Ed.): Thermodynamics and the Destruction of Resources, Cambridge University Press, Cambridge, 2011
# Szargut, J.: Egzergia. Widawnictwo Politechniki Shlaskej, Gliwice, Poland, 2007.
# [kJ/mol]
#
Chem_Ex = {                         # (0) CAS-No.     (1) solid     (2) liquid    (3) gaseous   (4) at T0,p0
    '1BUTENE':                      ['106-98-9',   'NaN',         # g
    'ACETONE':                      ['67-64-1',    1797.3,        # l
    'AMMONIA':                      ['7664-41-7',  337.9,         # g
    'ARGON':                        ['7440-37-1',  11.69,         # g
    'BENZENE':                      ['71-43-2',    3301.3,        # g
    'BENZENE(l)':                   ['71-43-2',    3296.2,        # l
    'CARBONDIOXIDE':                ['124-38-9',   19.48,         # g
    'CARBONMONOXIDE':               ['630-08-0',   274.71,        # g
    'CARBONYLSULFIDE':              ['463-58-1',   'NaN',
    'CYCLOHEXANE':                  ['110-82-7',   'NaN',         # g
    'CYCLOHEXANE(l)':               ['110-82-7',   'NaN',         # l
    'CYCLOPROPANE':                 ['75-19-4',    'NaN',         # g
    'CYCLOPENTANE':                 ['287-92-3',   'NaN',
    'OCTAMETHYLCYCLOTETRASILOXANE': ['556-67-2',   'NaN',
    'DECAMETHYLCYCLOPENTASILOXANE': ['541-02-6',   'NaN',
    'DODECAMETHYLCYCLOHEXASILOXANE':['540-97-6',   'NaN',
    'DEUTERIUM':                    ['7782-39-0',  263.8,         # g
    '1,2-DICHLOROETHANE':           ['107-06-2',   'NaN',
    'DEE':                          ['60-29-7',    'NaN',
    'DIMETHYLCARBONATE':            ['616-38-6',   'NaN',
    'DIMETHYLETHER':                ['15-10-6',    'NaN',         # g
    'ETHANE':                       ['74-84-0',    1495.0,        # g
    'ETHANOL':                      ['64-17-5',    'NaN',         # g
    'ETHANOL(l)':                   ['64-17-5',    1356.9,        # l
    'ETHYLBENZENE':                 ['100-41-4',   'NaN',         # g
    'ETHYLBENZENE(l)':              ['100-41-4',   4584.8,        # l
    'ETHYLENE':                     ['74-85-1',    1360.3,        # g
    'ETHYLENEOXIDE':                ['75-21-8',    'NaN',         # g
    'FLUORINE':                     ['7782-41-4',  504.9,         # g
    'HFE143M':                      ['421-14-7',   'NaN',
    'HEAVYWATER':                   ['7789-20-0',  31.2,          # g
    'HEAVYWATER(l)':                ['7789-20-0',  22.3,          # l
    'HELIUM':                       ['7440-59-7',  30.37,         # g
    'HYDROGEN':                     ['1333-74-0',  236.09,        # g
    'HYDROGENCHLORIDE':             ['7647-01-0',  84.5,          # g
    'HYDROGENSULFIDE':              ['7783-06-4',  812.0,         # g
    'ISOBUTAN':                     ['75-28-5',    'NaN',
    'ISOBUTENE':                    ['115-11-7',   'NaN',
    'ISOHEXANE':                    ['107-83-5',   'NaN',
    'ISOPENTANE':                   ['78-78-4',    'NaN',
    'KRYPTON':                      ['7439-90-9',  34.36,         # g
    'DECAMETHYLTETRASILOXANE':      ['141-62-8',   'NaN',
    'DODECAMETHYLPENTASILOXANE':    ['141-63-9',   'NaN',
    'TETRADECAMETHYLHEXASILOXANE':  ['107-52-8',   'NaN',
    'OCTAMETHYLTRISILOXANE':        ['107-51-7',   'NaN',
    'HEXAMETHYLDISILOXANE':         ['107-46-0',   'NaN',
    'METHANE':                      ['74-82-8',    831.2,         # g
    'METHANOL':                     ['67-56-1',    'NaN',         # g -> citated by Bejan1996 as Szargut1988
    'METHANOL(l)':                  ['67-56-1',    'NaN',         # l
    'METHYLLINOLEATE':              ['112-63-0',   'NaN',
    'METHYLLINOLENATE':             ['301-00-8',   'NaN',
    'METHYLOLEATE':                 ['112-62-9',   'NaN',
    'METHYLPALMITATE':              ['112-39-0',   'NaN',
    'METHYLSTEARATE':               ['112-61-8',   'NaN',
    'NEON':                         ['7440-01-9',  27.19,         # g
    'NEOPENTANE':                   ['463-82-1',   'NaN',
    'NITROGEN':                     ['7727-37-9',  0.72,          # g
    'NITROUSOXIDE':                 ['10024-97-2', 106.9,         # g
    'NOVEC649':                     ['756-13-8',   'NaN',
    'ORTHODEUTERIUM':               ['7782-39-0o', 'NaN',
    'ORTHOHYDROGEN':                ['1333-74-0o', 'NaN',
    'OXYGEN':                       ['7782-44-7',  3.97,          # g
    'PARADEUTERIUM':                ['7782-39-0p', 'NaN',
    'PARAHYDROGEN':                 ['1333-74-0p', 'NaN',
    'PROPYLENE':                    ['115-07-1',   2002.7,        # g
    'PROPYNE':                      ['74-99-7',    'NaN',         # g
    'R11':                          ['75-69-4',    'NaN',
# R ...
    'SULFURDIOXIDE':                ['7446-09-5',  313.4,         # g
    'SULFURHEXAFLUORIDE':           ['2551-62-4',  'NaN',
    'TOLUENE':                      ['108-88-3',   'NaN',         # g
    'TOLUENE(l)':                   ['108-88-3',   3928.3,        # l
    'WATER':                        ['7732-18-5',  9.5,           # g
    'WATER(l)':                     ['7732-18-5',  0.9,           # l
    'XENON':                        ['7440-63-3',  40.33,         # g
    'C2BUTENE':                     ['590-18-1',  'NaN',
    'M-XYLENE':                     ['108-38-3',  'NaN',
    'N-BUTANE':                     ['106-97-8',  2804.2,         # g
    'N-DECANE':                     ['124-18-5',  'NaN',          # l
    'N-DODECANE':                   ['112-40-3',  'NaN',          # l
    'N-HEPTANE':                    ['142-82-5',  'NaN',          # l
    'N-HEXANE':                     ['110-54-3',  'NaN',          # g
    'N-HEXANE(l)':                  ['110-54-3',  'NaN',          # l
    'N-NONANE':                     ['111-84-2',  'NaN',          # l
    'N-OCTANE':                     ['111-65-9',  'NaN',          # l
    'N-PENTANE':                    ['109-66-0',  3461.3,         # g
    'N-PENTANE(l)':                 ['109-66-0',  'NaN',          # l
    'N-PROPANE':                    ['74-98-6',   2152.8,         # g
    'N-UNDECANE':                   ['1120-21-4', 'NaN',          # l
    'O-XYLENE':                     ['95-47-6',   'NaN',          # l
    'P-XYLENE':                     ['106-42-3',  'NaN',
    'T2BUTENE':                     ['624-64-6',  'NaN',
}