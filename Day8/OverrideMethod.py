# Parent class Shape → method area()
# Child class Circle overrides area().

class Shape:
    def area(self):
        print("Area of shape")

class Circle(Shape):
    def area(self, radius):

        print(f"Circle Area is {radius * radius}")

c1= Circle()
c1.area(5)