#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  5 21:34:21 2020

@author: andresparrado
"""

stringy = "atggttacca"

def dna_complement(string):
    dictionary = {"A":"T","T":"A","G":"C","C":"G"}
    running_string = ""
    
    for char in string:
        char = char.upper()
        if char not in "ATGC":
            print("Bad string. Done")
            return None
        else:
            print("Good letter")
            to_append = dictionary[char]
            running_string += to_append
    
    return running_string

final = dna_complement(stringy)