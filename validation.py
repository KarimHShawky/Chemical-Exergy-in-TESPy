#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd

coolprop = pd.read_csv("CGAM_combustion_CoolProp.csv", index_col=0)
kkh = pd.read_csv("CGAM_combustion_KKH.csv", index_col=0)

delta_abs = kkh - coolprop
delta_rel = (delta_abs / coolprop).fillna(0)

print(delta_rel)
print(delta_abs)

delta_abs.to_csv("delta-abs-kkh-coolprop.csv")
delta_rel.to_csv("delta-rel-kkh-coolprop.csv")

epsilon = pd.read_csv("cgam-tdo-ver-0-4-results.csv", index_col=0)
tespy = pd.read_csv("cgam-tespy-results.csv", index_col=0)

tespy = tespy.loc[
    epsilon.index, epsilon.columns
]

tespy.loc[:, ["h", "s"]] /= 1e3
tespy.loc[:, ["T"]] += 273.15
epsilon.loc[:, ["T"]] += 273.15

# set reference enthalpies and entropies

# air
air = ["1", "2", "3"]
tespy.loc[air, ["h", "s"]] -= tespy.loc[air[0], ["h", "s"]]
epsilon.loc[air, ["h", "s"]] -= epsilon.loc[air[0], ["h", "s"]]

# CH4
ch4 = ["10"]
tespy.loc[ch4, ["h", "s"]] -= tespy.loc[ch4[0], ["h", "s"]]
epsilon.loc[ch4, ["h", "s"]] -= epsilon.loc[ch4[0], ["h", "s"]]

# flue gas
fg = ["4", "5", "6", "6p", "7"]
tespy.loc[fg, ["h", "s"]] -= tespy.loc[fg[0], ["h", "s"]]
epsilon.loc[fg, ["h", "s"]] -= epsilon.loc[fg[0], ["h", "s"]]

delta_abs = (tespy - epsilon)
delta_rel = (delta_abs / epsilon).fillna(0)

print(delta_rel)
print(delta_abs)

delta_abs.to_csv("delta-abs-tespy-ebsilon.csv")
delta_rel.to_csv("delta-rel-tespy-ebsilon.csv")
