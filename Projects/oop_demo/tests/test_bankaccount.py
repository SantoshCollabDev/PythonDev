"""
This test cases will be around bank account
"""
from learning.accounts.account import BankAccount, SavingsAccount

def test_bankaccount_basics():
    """
    This method checks the 
      account creation
      depositing the amount
      withdrawing the amount
    """
    account_my = BankAccount(
        account_number="x12345",
        name="LT",
        initial_deposit=10000)
    # checking if the balance is same as initial deposit
    assert account_my.balance == 10000
    # deposit 1000 more and check balance
    account_my.deposit(1000)
    assert account_my.balance == 11000

    # withdrwa 5000 and check balance
    account_my.withdraw(5000)
    assert account_my.balance == 6000

def test_savings_account():
    """ this
    """
    my_savings_account = SavingsAccount(
        account_number = "x12345",
        name = "LT",
        initial_deposit = 5000
    )
    # assert my_savings_account.account_type() == "Savings"
    assert my_savings_account.balance == 5000

    # try withdrwawing > balance, 
    # the balance shouldnt change
    # todo: this operation should result in error
    my_savings_account.withdraw(6000)

    assert my_savings_account.balance == 5000

    my_savings_account.deposit(1000)
    assert my_savings_account.balance == 6000

    # now withdraw valida blaance it should be allowed
    my_savings_account.withdraw(6000)
    assert my_savings_account.balance == 0

    # try depositing > 10 lakhs which should not be allowed
    my_savings_account.deposit(1100000)
    assert my_savings_account.balance == 0