"""
count number of times a class is called

count number of instances of  a class in python

"""
from symtable import Class


#### using class variable
class A:
    count = 0
    def __init__(self):
        A.count = A.count + 1
        print("class A is called")

aobj1 = A()
aobj2 = A()
aobj3 = A()
print(A.count)


### using global varuiable

count=0
class B:
    def __init__(self):
        global count
        count = count + 1
        print("class B is called")

bobj1 = B()
bobj2 = B()
bobj3 = B()
print(count)

