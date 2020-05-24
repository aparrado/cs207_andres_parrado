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

class AccountError(Exception):
    pass



# BankAccount class
class BankAccount():
    ''' This class creates a bank account. The main
        methods are withdraw and deposit. You cannot
        withdraw more than your balance. Also, you
        cannot withdraw or deposit a negative amount.
    '''
    
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
    
    
    def deposit(self, amount):
        if amount < 0:
            raise NegativeAmount('Cannot withdraw negative amount')
        else:
            self.balance += amount
    
    
    def __str__(self):
        return 'a Savings'
    
    
    def __len__(self):
        return self.balance
    


# BankUser class
class BankUser():
    def __init__(self,owner):
        self.owner = owner
        self.checking = None
        self.savings = None
    
    
    def addAccount(self,accountType):
        if accountType == AccountType.SAVINGS:
            if self.savings != None:
                raise AccountError('Bank account of this type already present')
            self.savings = BankAccount(self.owner,accountType)

        elif accountType == AccountType.CHECKING:
            if self.checking != None:
                raise AccountError('Bank account of this type already present')
            self.checking  = BankAccount(self.owner,accountType)
            
            
    def getBalance(self, accountType):
        if accountType == AccountType.SAVINGS:
            return self.savings.__len__()
        if accountType == AccountType.CHECKING:
            return self.checking.__len__()
        
        
    def deposit(self, accountType, amount):
        if accountType == AccountType.SAVINGS:
            return self.savings.deposit(amount)
        if accountType == AccountType.CHECKING:
            return self.checking.deposit(amount)
         
            
    def withdraw(self, accountType, amount):
        if accountType == AccountType.SAVINGS:
            return self.savings.withdraw(amount)
        if accountType == AccountType.CHECKING:
            return self.checking.withdraw(amount)
    
    def __str__(self):
        return 'User currently has {} and {} accounts'.format(self.checking,self.savings)
         
            


