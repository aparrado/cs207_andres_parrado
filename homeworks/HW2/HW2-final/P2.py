#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  3 09:49:55 2020

@author: andresparrado
"""
# Importing relevant libraries
import matplotlib.pyplot as plt
from collections import Counter


# Defining the key function
def languages(file_name):

    file = open(file_name,"r")
    languages = [x.rstrip() for x in file.readlines()]
    file.close()

    count_instances = dict(Counter(languages))
    for key, value in list(count_instances.items()):
        print("{1} students prefer {0}.".format(key,value))
    
    return count_instances

class_languages = languages("languages.txt")


# Plotting
labels = list(class_languages.keys())
values = list(class_languages.values())

plt.bar(range(len(class_languages)),values)
plt.xticks(range(len(class_languages)), labels)