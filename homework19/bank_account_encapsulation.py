# Create a class called BankAccount to represent a basic bank account. The class should
# have the following attributes:
# 1. owner: The name of the account owner.
# 2. balance: The current balance of the account.

# Implement the following methods:
# 1. __init__(self, owner, balance): Initializes the BankAccount object with the
# owner's name and initial balance. Ensure that the balance is a non-negative
# integer.
# 2. get_balance(self): Returns the current balance of the account.
# 3. deposit(self, amount): Adds the specified amount to the account balance.
# Ensure that the amount is a positive integer.
# 4. withdraw(self, amount): Subtracts the specified amount from the account
# balance. Ensure that the amount is a positive integer and does not exceed the
# current balance.

# Additionally, use @property and @attribute.setter to encapsulate the balance
# attribute and enforce validation rules.

class BankAccount:
   
    def __init__(self, owner, balance):
        self.owner = owner
        if not isinstance(balance, int):
            raise Exception("Invalid balance.")
        if balance < 0:
            raise Exception("Balance can not be negative.")
        else:
            self.__balance = balance
    
    @property
    def balance(self):
        return self.__balance
        
    @balance.setter
    def balance(self, new_balance):
        if isinstance(new_balance, int) and new_balance >= 0:
            self.__balance = new_balance
        else:
            raise ValueError("Balance must be a positive integer.")
            
    def deposit(self, deposit):
        if deposit <= 0:
            raise ValueError("Amount to be deposited should be positive.")
        self.__balance += deposit
        return f"The current balance of the account is {self.__balance}" 
    
    def withdraw(self, withdrawal):
        if withdrawal <= 0 or self.__balance < withdrawal:
            raise ValueError("Amount to be withdrawn should be positive.")
        self.__balance -= withdrawal
        return f"The current balance of the account is {self.__balance}"


account1 = BankAccount('account_holder_1', 1000)

print(account1.balance)
account1.deposit(500)
print(account1.balance)
account1.withdraw(200)
print(account1.balance)
