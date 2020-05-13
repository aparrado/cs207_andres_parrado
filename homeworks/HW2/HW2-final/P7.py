#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  8 16:07:06 2020

@author: andresparrado
"""
# Decorator
def is_positive(f):
    """This decorator ensures that functions return a 
    positive value in every situatin."""
    
    def inner(*args):
        result = f(*args)
        if result <= 0:
            print("Value is {0}. I will stop now. ".format(result))
            raise Exception("Not a positive value")

        else:
            print("Great! This is positive. You got {0}".format(result))
            return result
    return inner
    

# Other functions
@is_positive
def discriminant(a,b,c):
    return b*b - 4*a*c

@is_positive
def absolute_value(x):
    if x < 0:
        return -x
    else: 
        return x

@is_positive
def convert_one(y):
    if y == 1:
        return y
    else:
        return 1
    

# Testing the functions
d = discriminant(1,8,3)
h = absolute_value(-9)
u = convert_one(-10000)