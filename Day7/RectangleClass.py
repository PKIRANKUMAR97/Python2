# Q2. Rectangle class
# Constructor → length, width
# Method → area()
# Method → perimeter()

class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width

    def area(self):
        print("The area of the rectangle is ",self.length*self.width)

    def perimeter(self):
        print("The perimeter of the rectangle is ",(2*(self.length+self.width)))

rectangle_obj=Rectangle(10,20)
rectangle_obj.area()
rectangle_obj.perimeter()