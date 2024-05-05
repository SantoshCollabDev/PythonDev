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
      if amount >     1000000:
         print("Not allowed")
         return
      return super().deposit(amount)