class Bank :
    def __init__(self,name,salary):
        self.name = name
        self.__salary=salary

b1=Bank("Bank 1",100)
print(b1.name)
print(b1.__salary)

