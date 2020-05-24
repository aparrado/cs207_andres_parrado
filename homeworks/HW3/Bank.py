#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 24 10:15:52 2020

@author: andresparrado
"""

from enum import Enum
class AccountType(Enum):
    SAVINGS = 1
    CHECKING = 2
    



class NotEnoughMoney(Exception):
    pass

class NegativeAmount(Exception):
    pass





class BankAccount():
    
    def __init__(self, owner, accountType): 
        self.owner = owner
        self.accountType = accountType
        self.balance = 0
        
    def withdraw(self, amount):
        if self.balance - amount < 0:
            raise NotEnoughMoney('Cannot withdraw more than balance')
            
        elif amount < 0:
            raise NegativeAmount('Cannot withdraw negative amount')
        
        else:
            self.balance -= amount

testaccount = BankAccount("Andrés", AccountType.SAVINGS)