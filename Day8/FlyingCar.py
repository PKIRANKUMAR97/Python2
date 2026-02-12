# The Challenge: The "Flying Car"
# In this scenario, we have a Car and a Plane. A FlyingCar should be able to do both.
#
# Parent 1: Car
# Method drive() prints "Driving on the road."
#
# Parent 2: Plane
# Method fly() prints "Flying in the sky."
#
# Child: FlyingCar
# Inherits from both Car and Plane.
# Method transform() prints "Transforming now!"

class Car:
    def drive(self):
        print("Driving on the road")

class Plane:
    def fly(self):
        print("flying in the sky")

class FlyingCar(Car,Plane):
    def track(self):
        print("we are building this ....")

fc=FlyingCar()
fc.drive()
fc.fly()
fc.track()