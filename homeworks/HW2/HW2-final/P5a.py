#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  6 12:38:32 2020

@author: andresparrado
"""

def make_withdrawal(balance):
    init_balance = balance
    print("Your initial balance is",init_balance)
    
    def withdraw(withdrawal_amount):
        if init_balance - withdrawal_amount < 0:
            print('This exceeds your amount. Stop.')
            return None
        else:
            new_balance = init_balance - withdrawal_amount
            return print("Your new balance is:", new_balance)
        
    return withdraw
        
balance = 50

wd =  make_withdrawal(balance)
wd(60)