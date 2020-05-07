#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  3 16:27:16 2020

@author: andresparrado
"""
import math
#import numpy as np

# Importing the file
file_name = "circles.txt"
with open(file_name) as file:
    radii = [float(x.rstrip()) for x in file.readlines()]
    

# Defining the first function
def area_circle(radius):
    area = math.pi*(radius**2)
    return area

areas = [0.0]*len(radii)
# Defining the second function
def my_avg(radii_list, area_circle):
    for i in range(len(radii_list)):
        area = area_circle(radii_list[i])
        areas[i]=area
    final_average = sum(areas)/len(areas)
    
    print("My average was {}".format(final_average))

# Using the second function    
my_avg(radii,area_circle)
