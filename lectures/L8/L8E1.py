#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 16 14:06:22 2020

@author: andresparrado
"""

# Defining the class 'Dog' with a class method 'beagle'
class Dog:
    def __init__(self, breed, colors, special=None):
        self.breed = breed
        self.colors = colors
        self.special = special
    
    @classmethod
    def beagle(cls):
        breed = 'beagle'
        colors = ['black', 'white', 'brown']
        special = 'hunting'
        return cls(breed, colors, special)

# Printing to make sure it works properly
if __name__ == "__main__":        
    my_dog = Dog.beagle()
    print((my_dog))
    print(vars(my_dog))