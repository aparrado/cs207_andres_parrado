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
        
    def fit(self):
        raise NotImplementedError("Not implementable in this class")
        
    def get_params(self):
        raise NotImplementedError("Not implementable in this class")
    
    def predict(self,X):
        raise NotImplementedError("Not implementable in this class")
    
    def score(self,y):
        raise NotImplementedError("Not implementable in this class")
        
    def set_params(self,**kwargs):
        raise NotImplementedError("Not implementable in this class")
        
        

# Linear regression 
class LineraRegression(Regression):
    ''' Fits a linear regression model
    '''
    def fit(self,X,y):
        
        X_t = np.transpose(X)
        x_tX_inv = np.linalg.pinv(np.dot(X_t,X))
        b = np.dot(x_tX_inv,np.dot(X_t,y))
        
        self.params['beta'] = b
        
    def get_params(self):
        print("Returning the betas")
        return self.params['beta']

