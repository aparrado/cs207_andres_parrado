#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  3 16:27:16 2020

@author: andresparrado
"""
import math
import numpy as np
import time

# Decorator
def timer(f):
    def inner(*args):
        t0 = time.time()
        output = f(*args)
        elapsed = time.time() - t0
        print("Time Elapsed", elapsed)
        return output
    return inner


# Importing the file
file_name = "circles.txt"
with open(file_name) as file:
    radii = [float(x.rstrip()) for x in file.readlines()]
    

# Defining the first function
def area_circle(radius):
    area = math.pi*(radius**2)
    return area


# Defining the second function
areas = [0.0]*len(radii)

@timer
def my_avg(radii_list, area_circle):
    for i in range(len(radii_list)):
        area = area_circle(radii_list[i])
        areas[i]=area
    final_average = sum(areas)/len(areas)
    
    print("My average was {}".format(final_average))


# Moving on to the numpy function
areas_np = np.zeros(len(radii))

@timer
def np_ave(radii_list, area_circle):
    for i in range(len(radii_list)):
        area = area_circle(radii_list[i])
        areas[i]=area
    final_average = sum(areas)/len(areas)
    print("My average was {}".format(final_average))


# Using the second function     
my_avg(radii,area_circle)
np_ave(radii,area_circle)
