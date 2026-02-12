# 1. Simple inheritance
# Create a class Animal with method sound().
# Create a child class Dog that prints "Barks".

class Animal:
    def sound(self):
        print("Animal's sound")

class Dog(Animal):
    def sound(self):
        print("Barks")

dobj = Dog()
dobj.sound()