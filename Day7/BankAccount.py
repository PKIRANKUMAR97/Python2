# Q3. Bank Account
# Constructor → account_holder, balance
# Methods:
# deposit(amount)
# withdraw(amount)
# display_balance()

class BankAccount():
    def __init__(self,account_holder,balance):
        self.account_holder=account_holder
        self.balance=balance

    def deposit(self,amount):
        self.balance= self.balance + amount
        print(f"The deposit amount is {amount} and the balance after deposit is {self.balance}")

    def withdraw(self,amount):
        if self.balance >= amount:

            self.balance=self.balance-amount
            print(f"the withdraw amount is {amount} and the balance after withdraw is {self.balance}")

        else:
            print("insufficient balance")

    def display_balance(self):
        print("The final balance of the bank account is ",self.balance)

bank_obj=BankAccount("Kiran",10000)
bank_obj.deposit(100)
bank_obj.withdraw(11000)
bank_obj.display_balance()


