# 3. Method inheritance
# Parent class Vehicle has method start().
# Child class Car should inherit and call it.



class Vehicle:
    def start(self):
        print("Starting")

class Car(Vehicle):
    def start_car(self):
        self.start()
        print("Car started")

c1= Car()
c1.start_car()
