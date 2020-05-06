#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  6 12:38:32 2020

@author: andresparrado
"""

def make_withdrawal(balance):
    #init_balance = balance
    print("Your initial balance is",balance)
    
    def withdraw(withdrawal_amount):
        if balance - withdrawal_amount < 0:
            print('This exceeds your amount. Stop.')
            return None
        else:
            balance = balance - withdrawal_amount
            return print("Your new balance is:", balance)
        
    return withdraw
        
balance = 20

wd =  make_withdrawal(balance)
wd(30)