#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 19 16:38:54 2020

@author: andresparrado
"""

import mynumbers as myn
zc = myn.Complex(2.0,1.0) # complex number
print(zc.real, zc.imag)

numb = myn.Complex(2,1)
numb.polar_form()
print('The radius is {} and the angle is {}'.format(numb.r,numb.theta))

zd = myn.Dual(2.0,2.0)
print(zd.real, zd.dual)

zd.polar_form()
print(zd.r, zd.theta)