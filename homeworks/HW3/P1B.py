#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 23 14:44:16 2020

@author: andresparrado
"""

import Regressions as Reg #import regression classes
from sklearn import datasets
from sklearn.model_selection import train_test_split


dataset = datasets.load_diabetes()
X_train, X_test, y_train, y_test = train_test_split(dataset['data'], 
                                                    dataset['target'], 
                                                    test_size=0.2, 
                                                    random_state=42)




model = Reg.LineraRegression()
model.fit(X_train,y_train)
