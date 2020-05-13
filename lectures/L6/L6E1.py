#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 10 09:22:05 2020

@author: andresparrado
"""
import math

# Creating the class
class Circle():
    
    def __init__(self,xr,yr,x0,y0):
      self.xr = xr
      self.yr = yr
      self.x0 = x0
      self.y0= y0
      
      print("the radius of this circle is located at ({0},{1})".format(self.xr,self.yr))
      
    def radius(self):
        self.rad = math.sqrt((self.xr-self.x0)**2 + (self.yr-self.y0)**2)
        print("the radius is {}".format(self.rad))
        return self.rad
    
    def area(self):
        self.area = math.pi*self.rad**2
        print("the area is {}".format(self.area))
        return self.area
    
    def perimeter(self):
        self.per = 2*math.pi*self.rad
        print("the perimeter is {}".format(self.per))
        return self.per


# Testing that the class works
def test_circle():
    
    circ = Circle(1,1,3,3)
    print("instance creation test passed")
    
    circ.radius()
    print("radius test passed")
    
    circ.area()
    print("area test passed")
    
    circ.perimeter()
    print("perimeter test passed")
  
test_circle()