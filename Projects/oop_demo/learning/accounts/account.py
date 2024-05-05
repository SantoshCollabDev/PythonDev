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

    def account_type(self):
      """
      This method will return the account_type
      """
      #  if self is SavingsAccount:
      if isinstance(self, SavingsAccount):
         return "Savings"
      #  elif self is CurrentAccount:
      elif isinstance(self, CurrentAccount)
         return "Current"
      return None
    
class SavingsAccount(BankAccount):
   """ This class represents the savings account structure
   """
   # Note: we dont need to repeat method as it is already 
   # happening at parent class
   def withdraw(self, amount):
      """ This method is overriden to implement non-negative balanaces
      """
      if self.balance - amount < 0:
         # dont allow withdrawl
         # fail this
         print("This transction is not allowed")
         return 
      return super().withdraw(amount)

   def deposit(self, amount):
      """
      This method stops user from depositing > 10 lakhs
      """
      if amount > 1000000:
         print("Not allowed")
         return
      return super().deposit(amount)
   
class CurrentAccount(BankAccount):
   """
   This represents the current account
   Sicne there is no restirctions on deposit
   and withdrwal there is nothing to oveeride
   in CurrentAccount child class
   """
   pass 


