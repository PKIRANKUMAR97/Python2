# 1. The "Pet" Hierarchy
# The Goal: Create a base class Pet with an __init__ method that takes a name.
# Create a child class Cat that inherits from Pet.
# Add a method in Cat called meow() that prints "Name says Meow!".
# Key concept: Accessing parent attributes in child methods.


class Pet:
    def __init__(self,name):
        self.name = name   ## parent attributes

class Cat(Pet):
    def meow(self):
        print(f"{self.name} says Meow!")   ## accessing parent attributes in child method

c1=Cat("Billy")
c1.meow()            ## Billy says Meow!