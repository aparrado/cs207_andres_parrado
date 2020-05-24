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

class WrongTypeAccount(Exception):
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
        if self.accountType == AccountType.CHECKING:
            return 'a Checking'
        elif self.accountType == AccountType.SAVINGS:
            return 'a Savings'
        else:
            return 'No account'
    
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
        else:
            raise WrongTypeAccount('You cannot add this account')
            
            
    def getBalance(self, accountType):
        if accountType == AccountType.SAVINGS:
            return self.savings.__len__()
        if accountType == AccountType.CHECKING:
            return self.checking.__len__()
        
        
    def deposit(self, accountType, amount):
        if accountType == AccountType.SAVINGS:
            return self.savings.deposit(amount)
        elif accountType == AccountType.CHECKING:
            return self.checking.deposit(amount)
        else:
            raise WrongTypeAccount('You entered an invalid account type')
         
            
    def withdraw(self, accountType, amount):
        if accountType == AccountType.SAVINGS:
            return self.savings.withdraw(amount)
        elif accountType == AccountType.CHECKING:
            return self.checking.withdraw(amount)
        else:
            raise WrongTypeAccount('You entered an invalid account type')
         
    
    def __str__(self):
        return 'User currently has {} and {} accounts'.format(self.checking,self.savings)
         
            
def ATMsession(bankUser):
    
    def Interface():
        exit_status = 0
        user = bankUser
        while exit_status !=1:
            print('Hello, {}! What would you like to to today?'\
                  .format(bankUser.owner))
            beginning = input('''Enter option: 
                          \n1)Exit 
                          \n2)Create account 
                          \n3)Check balance
                          \n4)Deposit
                          \n5)Withdraw
                          \nThis is your input: ''')
                          
            if beginning == '1':
                print('Exiting. Good bye!')
                break
            
            
            # Options for the type of account
            typeaccount = input('''Enter option:
                            \n1)Checking
                            \n2)Savings
                            \nThis is your input: ''')
                        
            # Setting the type of bank account
            if typeaccount == '1':
                selected = AccountType.CHECKING
            elif typeaccount == '2':
                selected = AccountType.SAVINGS
            
            
            # Creating bank account    
            if beginning == '2':
                if typeaccount == '1':
                    try:
                        user.addAccount(selected)
                        print('Checking account created!')
                    except Exception as e:
                        print(e)
                elif typeaccount == '2':
                    try:
                        user.addAccount(selected)
                        print('Savings account created!')
                    except Exception as e:
                        print(e)
                else:
                    print('Wrong type of account')
                    
                    
            # Checking balance. Needs to create a bank account first  
            if beginning == '3':
                try:
                    print('Your balance in this account is {}'\
                          .format(user.getBalance(selected)))
                except:
                    print('Please go back and create a bank account first')
                    
            # Creating a deposit
            if beginning == '4':
                amount = input('Please enter your deposit amount: ')
                try:
                    amount = int(amount)
                    user.deposit(selected, amount)
                    print('Your amount of {} was succesfully deposited!'\
                          .format(amount))
                    print('Your balance in this account is {}'\
                          .format(user.getBalance(selected)))
                except Exception as e:
                    print(e)
            
            
            # Creating a withdrawal
            if beginning == '5':
                amount = input('Please enter your withdrawal amount: ')
                try:
                    amount = int(amount)
                    user.withdraw(selected, amount)
                    print('Your amount of {} was succesfully withdrawn!'\
                          .format(amount))
                    print('Your balance in this account is {}'\
                          .format(user.getBalance(selected)))
                except Exception as e:
                    print(e)
                    
        
    return Interface()

session = ATMsession(BankUser('Andrés'))