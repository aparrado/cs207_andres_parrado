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
        for key in kwargs:
            self.params[key] = kwargs[key]
       

# Linear regression 
class LinearRegression(Regression):
    ''' Fits a linear regression model
    '''
    def fit(self,X,y):
        ones = np.ones(X.shape[0])
        X = np.c_[ones,X]
        X_t = np.transpose(X)
        x_tX_inv = np.linalg.pinv(np.dot(X_t,X))
        b = np.dot(x_tX_inv,np.dot(X_t,y))
        
        self.params['beta'] = b
        
        
    def get_params(self):
        print("Returning the betas")
        return self.params['beta']


    def predict(self,X):
        ones = np.ones(X.shape[0])
        X = np.c_[ones,X]
        beta =  self.params['beta']
        self.predictions = np.dot(X,beta)
        print("Returning the predictions")
        return self.predictions


    def score(self,y):
        y_mean = np.average(y)
        SST = np.dot(y - y_mean,y - y_mean)
        SSE = np.dot(y - self.predictions, y - self.predictions)
        self.r_squared = 1-(SSE/SST)
        print("The R^2 is {:.2f}".format(self.r_squared))
        return self.r_squared
        
    
# RidgeRegression class. Inherets from LinearRegression
class RidgeRegression(LinearRegression):
    
    def __init__(self, alpha=0.1):
        super(RidgeRegression, self).__init__()
        self.params['alpha'] = alpha

    
    def fit(self,X,y):
        ones = np.ones(X.shape[0])
        X = np.c_[ones,X]
        X_t = np.transpose(X)
        
        gamma = self.params['alpha']*np.identity(X.shape[1])
        gamma_t = np.transpose(gamma)
        
        # Finding the inverse of a long matrix 
        x_tX_inv = np.linalg.pinv(np.dot(X_t,X)+ np.dot(gamma_t,gamma))
        
        # Finding the betas
        b = np.dot(x_tX_inv,np.dot(X_t,y))
        
        self.params['beta'] = b
        
    