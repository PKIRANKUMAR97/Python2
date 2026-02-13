# To access a private property, you can create a getter method:

class Bank:
    def __init__(self,name,salary):
        self.name=name
        self.__salary=salary

    def get_salary(self):
        return self.__salary

b1=Bank("Bank 1",100)
print(b1.name)
print(b1.get_salary())
