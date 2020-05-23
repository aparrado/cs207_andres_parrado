#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 23 14:24:41 2020

@author: andresparrado
"""

import numpy as np

# General regression class
class Regression():
    
    def __init__(self):
        self.params = {}
        
    def fit(self,X,y):
        raise NotImplementedError("Method not implementable")
        
    def get_params(self):
        raise NotImplementedError("Method not implementable")
    

# Linear regression 
class LineraRegression(Regression):
    

    def fit(self,X,y):
        
        X_t = np.transpose(X)
        x_tX_inv = np.linalg.pinv(X_t*X) 
        b = x_tX_inv*X_t*y
        
        self.params['beta'] = b
        
    def get_params(self):
        print("Returning the betas")
        return self.params['beta']
        