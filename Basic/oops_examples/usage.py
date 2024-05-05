from accounts import BankAccount

if __name__ == "__main__":
    account_1 = BankAccount(
        account_number = "A12345",
        name = "LT",
        initial_deposit = 100000
    )

    print(f"Initial Balance {account_1.balance}")
    account_1.deposit(100000)
    print(f"Balance after deposit {account_1.balance}")

    account_1.withdraw(100000)
    print(f"Balance after withdrwal {account_1.balance}")

    