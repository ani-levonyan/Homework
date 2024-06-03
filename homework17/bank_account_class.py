# Define a class named BankAccount with an __init__ method that initializes two
# instance variables: account_holder and balance.
# The class has methods like deposit and withdraw, each of which takes an amount as
# an argument and updates the account balance accordingly. These methods also
# include checks for valid input and available funds.
# The get_balance method allows you to retrieve the account balance.
# We create an Object of the BankAccount class called account1 with an initial balance
# of $1000.
# We deposit $500 and withdraw $200 from the account and print the account
# information.

class BankAccount:
   
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
    
    def deposit(self, inp_deposit_amount):
        if inp_deposit_amount <= 0:
            raise ValueError("Amount to be deposited should be positive.")
        self.balance += inp_deposit_amount
        return f"The current balance of the account is {self.balance}" 
    
    def withdraw(self, inp_withdrawal_amount):
        if inp_withdrawal_amount <= 0 or self.balance < inp_withdrawal_amount:
            raise ValueError("Amount to be withdrawn should be positive and should not exceed the current balance.")
        self.balance -= inp_withdrawal_amount
        return f"The current balance of the account is {self.balance}"
        
    def get_balance(self):
        return f"The current balance of the account is {self.balance}"
        
    
account1 = BankAccount('account_holder_1', 1000)

print(account1.get_balance())
account1.deposit(500)
print(account1.get_balance())
account1.withdraw(200)
print(account1.get_balance())
