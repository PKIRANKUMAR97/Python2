# To modify a private property, you can create a setter method.
# The setter method can also validate the value before setting it:


class Bank:
    def __init__(self,name,salary):
        self.name=name
        self.__salary=salary

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        if salary > 0:
            self.__salary = salary
        else:
            print("salary must be positive")



b1=Bank("Bank 1",100)
print(b1.name)
print(b1.get_salary())
b1.set_salary(-1000)
print(b1.get_salary())


b1.set_salary(1000)
print(b1.get_salary())
