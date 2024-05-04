"""
This module will have Bank Account Class
"""

class BankAccount:
    """
    This class will have basic account functionality
    """
    def __init__(self,
                 account_number: str,
                 name: str,
                 initial_deposit: float = 0):
      """
      Set/Initialize object to initial values
      """
      self.account_number = account_number
      self.name = name
      self.balance = initial_deposit

    def withdraw(self, amount):
       """
       This method withdraw amount
       """
       self.balance -= amount

    def deposit(self, amount):
       """
       This method deposits amount
       """
       self.balance += amount
    
   