# 5. Use super()
# Parent class Employee has constructor with name.
# Child class Developer adds language.
# Use super() to initialize parent.

class Employee:
    def __init__(self,name):
        self.name = name

class Developer(Employee):
    def __init__(self,name,language):
        super().__init__(name)
        self.language = language

    def skill(self):
        print(f"employee name is {self.name}")
        print(f"Developer skill is {self.language}")

d1 = Developer("Kiran","Python")
d1.skill()