#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 19 16:15:29 2020

@author: andresparrado
"""
import math

# Defining the first class
class RealExtensions:

    def __init__(self,a,b):
        self.real = a
        self.imag = b
        
        
# Defining the second class        
class Complex(RealExtensions):
    
    def _magnitude(self):
        self.r = math.sqrt(self.real**2 + self.imag**2)
        return self.r
    
    def _angle(self):
        self.theta = math.atan(self.imag/self.real)
        return self.theta    
    
    def polar_form(self):
        self._magnitude()
        self._angle()
        
        

# Defining the third class
class Dual(RealExtensions):
    def __init__(self,a,b):
        self.dual = b
        self.real = a
    
    def _magnitude(self):
        self.r = self.real
        return self.r
    
    def _angle(self):
        self.theta = self.dual/self.real
        self.theta   
    
    def polar_form(self):
        self._magnitude()
        self._angle()
        
    
    
