# Q5. Car class
# Requirements:
# Constructor → brand, speed
# Method → accelerate()
# Method → brake()
# Speed should not go below 0

class Car:
    def __init__(self,brand,speed):
        self.brand=brand
        self.speed=speed

    def accelerate(self,increment):
        self.speed=self.speed + increment
        print("the speed is ",self.speed)

    def brake(self, decrement):
        self.speed = self.speed - decrement

        if self.speed < 0 :
            self.speed = 0
        print("the speed is ",self.speed)

car_obj=Car("BMW",100)
car_obj.accelerate(2)
car_obj.brake(100)