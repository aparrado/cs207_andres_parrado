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


# Printing all the functions/methods in the class 'Regression
print(dir(Reg.Regression))



model1 = Reg.LinearRegression()
model2 = Reg.RidgeRegression(alpha=0.8)


models = [model1, model2]

for model in models:
    model.fit(X_train, y_train)
    model.predict(X_test)
    model.score(y_test)