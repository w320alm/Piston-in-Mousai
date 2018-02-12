#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 14:21:24 2018

@author: austinmcdonnell
"""

import mousai as ms

def TestDummy(x, params):
    P_list=params['Pressure List']
    pos_list=params['Position List']
    times=params['Time']
    vel_list=params['Velocity List']
    moles_list=params['Moles List']
    a_list=params['Acceleration List']
    
    
P_list,pos_list,times,vel_list,moles_list,a_list = ms(TestDummy,numvariables=6, eqform='first_order', num_harmonics=5)

print('Displacement is ', pos_list[0])