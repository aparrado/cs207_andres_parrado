#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  3 16:27:16 2020

@author: andresparrado
"""
import math

# Importing the file
file_name = "circles.txt"
with open(file_name) as file:
    radii = [float(x.rstrip()) for x in file.readlines()]
    

# Defining the first function
def area_circle(radius):
    area = math.pi*(radius**2)
    return area

# Defining the second function
def my_avg(radii_list, area_circle):
    averages = []
    for radius in radii_list:
        area = area_circle(radius)
        averages.append(area)
    final_average = sum(averages)/len(averages)
    
    print("My average was {}".format(final_average))

# Using the second function    
my_avg(radii,area_circle)