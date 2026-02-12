# 2. Use parent constructor
# Create a class Person with constructor accepting name.
# Create child class Student that also accepts roll_no.
# Print both values.

class Person:
    def __init__(self,name):
        self.name = name


class Student(Person):
    def __init__(self,name,rollno):
        super().__init__(name)
        self.rollno = rollno
    def display(self):
        print(f"Student name is {self.name} and rollno is {self.rollno}")

s1=Student("JOHNN",1)
s1.display()



