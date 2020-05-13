#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 13 16:02:08 2020

@author: andresparrado
"""
import numpy as np

# First, defining the function Circle
class Circle:
    '''A class for circles
      Constructor is initialized with two tuples, one for the center of the circle
      and the other for a point on the circle.

      Methods include radius, area, and circum.  None of these methods accept any arguments.

      The user is not required to pre-compute the radius of the circle.  Exception testing is 
      done in area and circum to check for a circle radius.  If it doesn't exist, a radius is 
      computed.
    '''

    def __init__(self, center, point):
        self.xc = center[0]
        self.yc = center[1]
        self.x = point[0]
        self.y = point[1]

    def radius(self):
        x = self.x - self.xc
        y = self.y - self.yc
        self.R = np.sqrt(x * x + y * y)

    def area(self):
        try:
            self.A = np.pi * self.R* self.R
        except AttributeError:
            x = self.x - self.xc
            y = self.y - self.yc
            r = np.sqrt(x * x + y * y)
            self.R = r
            self.A = np.pi * r * r

    def circum(self):
        try:
            self.C =  2.0 * np.pi * self.R
        except AttributeError:
            x = self.x - self.xc
            y = self.y - self.yc
            r = np.sqrt(x * x + y * y)
            self.R = r
            self.C = 2.0 * np.pi * r
        

# Then, defining the function Rcircle that inherits from circle
class Rcircle(Circle):
    '''A class for circles
       This class inherits from the class Circle. It takes the argument r,
       which defines the radius of the circle.
    '''
    def __init__(self, r):
        self.R = float(r)
        
    def radius(self):
        pass
    
    def __eq__(self,other):
        other.radius()
        return self.R == other.R

circling = Rcircle(2)
circus = Circle((0,0),(1,0))
