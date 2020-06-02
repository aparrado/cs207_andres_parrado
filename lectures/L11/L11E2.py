#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 17:19:39 2020

@author: andresparrado
"""
# Class to do the forward pass of automatic differentation
class function_diff():
    
    def __init__(self, a,r):
        self.a = a
        self.r = r
        self.values = []
        
    def __pow__(self,a,c): # overloading the __pow__ method
        return a**c, (c)*(a**(c-1))
    
    def first_pass(self):
        x1 = self.r
        dx1 = 1
        self.values.append( [x1,dx1])
    
    def second_pass(self):
        x2, dx2 = self.__pow__(self.a,self.r)
        self.values.append ([x2,self.values[0][1]*dx2])
        
        
# Testing the class
test = function_diff(4, 3)
test.first_pass()
test.second_pass()
print(test.values)