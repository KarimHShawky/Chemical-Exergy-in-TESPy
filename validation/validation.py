#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd

tables = ["kkh", "coolprop"]

tdo = pd.read_csv("tdo/cgam-tdo-results.csv", decimal=",", sep=";", index_col=0)
tdo.index = tdo.index.astype(str)

for table_name in tables:
    table = pd.read_csv("combustion/cgam-combustion-" + table_name + "-results.csv", index_col=0)
    table.index = table.index.astype(str)
    table_mod = table.loc[
        [r for r in tdo.index.values if r in table.index.values],
        [c for c in tdo.columns.values if c in table.columns.values]
    ]

    table_mod["T"] += 273.15

    tdo_mod = tdo.loc[table_mod.index.values, table_mod.columns.values]

    delta_abs = table_mod - tdo_mod
    delta_rel = (delta_abs / tdo_mod).fillna(0)

    print(delta_rel)
    print(delta_abs)


tables = ["tespy", "ebsilon"]

for table_name in tables:
    if table_name == "ebsilon":
        table = pd.read_csv("ebsilon/cgam-" + table_name + "-results.csv", index_col=0)
    else:
        table = pd.read_csv("cgam-" + table_name + "-results.csv", index_col=0)
        table["T"] += 273.15

    table.index = table.index.astype(str)
    table_mod = table.loc[
        [r for r in tdo.index.values if r in table.index.values],
        [c for c in tdo.columns.values if c in table.columns.values]
    ]

    tdo_mod = tdo.loc[table_mod.index.values, table_mod.columns.values]

    delta_abs = table_mod - tdo_mod
    delta_rel = (delta_abs / tdo_mod).fillna(0)

    print(delta_rel)
    print(delta_abs)

tespy = pd.read_csv("cgam-tespy-results.csv", index_col=0)
ebsilon = pd.read_csv("ebsilon/cgam-ebsilon-results.csv", index_col=0)

tespy = tespy.loc[
    ebsilon.index, ebsilon.columns
]

tespy.loc[:, ["h", "s"]] /= 1e3
tespy.loc[:, ["T"]] += 273.15

# set reference enthalpies and entropies

# air
air = ["1", "2", "3"]
tespy.loc[air, ["h", "s"]] -= tespy.loc[air[0], ["h", "s"]]
ebsilon.loc[air, ["h", "s"]] -= ebsilon.loc[air[0], ["h", "s"]]

# CH4
ch4 = ["10"]
tespy.loc[ch4, ["h", "s"]] -= tespy.loc[ch4[0], ["h", "s"]]
ebsilon.loc[ch4, ["h", "s"]] -= ebsilon.loc[ch4[0], ["h", "s"]]

# flue gas
fg = ["4", "5", "6", "6p", "7"]
tespy.loc[fg, ["h", "s"]] -= tespy.loc[fg[0], ["h", "s"]]
ebsilon.loc[fg, ["h", "s"]] -= ebsilon.loc[fg[0], ["h", "s"]]

delta_abs = (tespy - ebsilon)
delta_rel = (delta_abs / ebsilon).fillna(0)

print(delta_rel)
print(delta_abs)
