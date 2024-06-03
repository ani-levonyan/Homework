# Exercise: Bank Account Hierarchy
# Create a hierarchy of classes representing different types of bank accounts. Start
# with a base class called BankAccount. Then, create two subclasses,
# SavingsAccount and CheckingAccount. Each subclass should inherit from the
# BankAccount class.
# ● The BankAccount class should have the following attributes and methods:
# ○ Attributes: account_number, balance
# ○ Methods: __init__ (constructor), deposit, withdraw, and get_balance
# ● The SavingsAccount class should inherit from BankAccount and have an
# additional attribute interest_rate. Override the deposit method to add
# interest to the balance when a deposit is made.
# ● The CheckingAccount class should inherit from BankAccount and have an
# additional attribute overdraft_fee. Override the withdraw method to deduct
# the overdraft fee if a withdrawal causes the balance to go below zero.

class BankAccount:
   
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
    
    def deposit(self, inp_deposit_amount):
        if inp_deposit_amount <= 0:
            raise ValueError("Amount to be deposited should be positive.")
        self.balance += inp_deposit_amount
        return f"The current balance of the account is {self.balance}" 
    
    def withdraw(self, inp_withdrawal_amount):
        if inp_withdrawal_amount <= 0 or self.balance < inp_withdrawal_amount:
            raise ValueError("Amount to be withdrawn should be positive.")
        self.balance -= inp_withdrawal_amount
        return f"The current balance of the account is {self.balance}"
        
    def get_balance(self):
        return f"The current balance of the account is {self.balance}"


class SavingsAccount(BankAccount):

    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def deposit(self, inp_deposit_amount):
        if inp_deposit_amount <= 0:
            raise ValueError("Amount to be deposited should be positive.")
        self.balance += inp_deposit_amount * (1 + self.interest_rate)
        return f"The current balance of the account is {self.balance}" 


class CheckingAccount(BankAccount):

    def __init__(self, account_number, balance, overdraft_fee):
        super().__init__(account_number, balance)
        self.overdraft_fee = overdraft_fee

    def withdraw(self, inp_withdrawal_amount):
        if inp_withdrawal_amount <= 0:
            raise ValueError("Amount to be withdrawn should be positive.")
        elif self.balance < inp_withdrawal_amount:
            self.balance -= self.overdraft_fee
            self.balance -= inp_withdrawal_amount
        return f"The current balance of the account is {self.balance}"
        

account1 = BankAccount('20500475090100', 1000)
print(account1.get_balance())

account1.withdraw(500)
print(account1.get_balance())

savings_account = SavingsAccount('20500475090101', 1000, 0.055)
print(savings_account.get_balance())

savings_account.deposit(500)
print(savings_account.get_balance())

checking_account = CheckingAccount('20500475090102', 1000, 500)
print(checking_account.get_balance())

checking_account.withdraw(1400)
print(checking_account.get_balance())
