"""
class   object
Employee --------> John, Raj ,Sam
Animal   --------> Cat ,Dog ,Lion

class ---> collection of Variables(attributes) and methods (behaviour)

A class is a blue print
Logical entity
Does not occupy space in memory

object ---> an instance of class
physical entity
occupy certain amount of space in memory

For one class , we can create any number opf objects
Objects are independent

Function Vs Method
----------------------
Function ---> we can create without class
Method   ---> create inside the class

2 TYPES OF METHODS we can define within class
1.instance method -- we can call only through objects
2. static method  -- we can directly call using class

Global Variables
Class variables
Local Variables

Method     constructor

method : give any name
         return the values
         method can take arguments
         need to use objects to invoke the methods

Constructor : __init__(self)
             never returns the values
             constructor can also take arguments
             will be called at the time of object creation


"""

# ex 1 :

class Myclass:
    def myfunction(self):
        pass
    def display(self,name):
        print(name)

mc1=Myclass()   # create object
mc2=Myclass()

mc1.myfunction()
mc1.display("KIRAN")  # KIRAN

# EX 2 :
class MyClass:
    def m1(self):
        print("this is instance method")
    @staticmethod     # common for every object
    def m2(self,num):
        print(self,num)

o1=MyClass()
o1.m1()
o1.m2(1000,2000)

MyClass.m2(10,20) # calling static method through class

# ex 3 :
class MyClass:
    a,b=10,20  # class variables

    def add(self):
        print(self.a+self.b)

    def mul(self):
        print(self.a*self.b)
o1=MyClass()
o1.add()  # 30
o1.mul()  # 200

## ex 4 :

i,j = 15, 25  # global variables
class MyClass:
    a,b=10,20 # class variables
    def add(self,x,y):
        print(x+y)       # x,y local variables
        print(self.a+ self.b)   # a,b class variables
        print(i+j)       # i,j are global variables

o1=MyClass()
o1.add(100,200)

## ex 5 :

a,b = 15, 25                                      # global variables
class MyClass:
    a,b=10,20                                     # class variables
    def add(self,a,b):
        print(a+b)                                # local variables
        print(self.a+self.b)                      # class variables
        print(globals()['a']+globals()['b'])      ## global variables

o1=MyClass()
o1.add(100,200)

# ex 6 : one class multiple objects

class MyClass:
    def display(self,name):
        print("This is display method")
        print(name)

o1 = MyClass()
o1.display("DELHI")

o2 = MyClass()
o2.display("STARC")

## EX 7 : constructor

class MyClass:
    def __init__(self):
        print(" this is constructor")
    def m1(self):
        print(" this is method 1")
    def m2(self,x,y):
        return (x+y)

o1=MyClass()   # invoked the constructor automatically
o1.m1()        # we need to call explicitly
res=o1.m2(1,2)
print(res)

# ex 8 :




