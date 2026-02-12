# 2. The Bank Account ExtensionThe Goal: Create a class Account with an attribute balance.
# Create a child class SavingsAccount that adds an attribute interest_rate.
# Use super() to initialize the balance from the parent.
# Add a method show_interest() that calculates and prints: balance * times interest_rate
# Key concept: Using super() with numeric data.

class Account:
    def __init__(self,balance):
        self.balance = balance

class SavingsAccount(Account):
    def __init__(self,balance,interest_rate):
        super().__init__(balance)
        self.interest_rate = interest_rate


    def show_interest(self):
        print(f"Interest : {self.balance* self.interest_rate}")

sa1 = SavingsAccount(10000,0.2)
sa1.show_interest()
