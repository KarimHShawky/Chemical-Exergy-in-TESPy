# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 10:50:48 2021

@author: kshaw
"""

from tespy.components import Subsystem, HeatExchanger, Drum
from tespy.connections import Connection


class HeatRecoverySteamGenerationSYS(Subsystem):
  #defenierung der Klasse

    def create_comps(self):
        #Erstellung der Komponenten 
        self.comps['eco'] = HeatExchanger('economizer')
        self.comps['eva'] = HeatExchanger('evaporator')
        self.comps['sup'] = HeatExchanger('superheater')
        self.comps['drum'] = Drum('drum')
        
    def create_conns(self):
        # Erstellung der Verbindungen
        self.conns['eco_dr'] = Connection(self.comps['eco'],'out2',
                                           self.comps['drum'], 'in1')
        
        self.conns['dr_eva'] = Connection(self.comps['drum'], 'out1',
                                           self.comps['eva'], 'in2')
        
        self.conns['eva_dr'] = Connection(self.comps['eva'], 'out2',
                                           self.comps['drum'], 'in2')
        
        self.conns['dr_sup'] = Connection(self.comps['drum'], 'out2', 
                                           self.comps['sup'], 'in2')
        
        self.conns['sup_eva']= Connection(self.comps['sup'], 'out1',
                                           self.comps['eva'], 'in1')
        
        self.conns['eva_eco']= Connection(self.comps['eva'], 'out1',
                                           self.comps['eco'], 'in1')
        

