"""
Acquiring all the attributes(variables) & behavior (methods) from one class to another class is called as inheritance

Class A -- a,b,c  m1(),m2()   ---A is parent class /base class /Super class
Class B(A)-- x,y,z  m3()      ---B is child class  /derived class / base class

main purpose -- code reusability , avoid duplication

4 types of inheritance
1.single
2.multi level
3.Hierarchy
4. Multiple inheritance

"""
## ex 1:

# class A :
#     def m1(self):
#         print(" this is m1 method from class A")
#
# class B(A) :
#     def m2(self):
#         print(" this is m2 method from class B")
#
# bobj=B()
# bobj.m1()   # class A
# bobj.m2()   # class B

## ex 2 : single inheritance

# class A :
#     x,y = 10,20        # class variables
#     def m1(self):
#         print(self.x+self.y)
#
# class B(A) :
#     a,b= 200,100
#     def m2(self):
#         print(self.a-self.b)
#
# bobj = B()
# bobj.m1()    # 30
# bobj.m2()     # 100

###ex 3 : multilevel inheritance

# class A :
#     x,y = 10,20        # class variables
#     def m1(self):
#         print(self.x+self.y)
#
# class B(A) :
#     a,b= 200,100
#     def m2(self):
#         print(self.a-self.b)
#
# class C(B):
#     i,j = 5 , 2
#     def m3(self):
#         print(self.i*self.j)
#
# cobj=C()
# cobj.m1()  ## 30
# cobj.m2()  ## 300
# cobj.m3()  ## 7

### ex 4 : hierarchy inheritance
# class A :
#     x,y = 10,20        # class variables
#     def m1(self):
#         print(self.x+self.y)
#
# class B(A) :
#     a,b= 200,100
#     def m2(self):
#         print(self.a-self.b)
#
# class C(A):
#     i,j = 5 , 2
#     def m3(self):
#         print(self.i*self.j)

# bobj=B()
# bobj.m1() # 30
# bobj.m2()  # 100
#
# cobj=C()
# cobj.m1()   # 30
# cobj.m3()   #  10

### ex 5 : multiple inheritance -- 2 parent , 1 child
# class A :
#     x,y = 10,20        # class variables
#     def m1(self):
#         print(self.x+self.y)
#
# class B :
#     a,b= 200,100
#     def m2(self):
#         print(self.a-self.b)
#
# class C(A,B):
#     i,j = 5 , 2
#     def m3(self):
#         print(self.i*self.j)
#
# cobj=C()
# cobj.m1()  # 30
# cobj.m2()  # 100
# cobj.m3()  # 10

## ex 6 : calling parent class method using child class -- super ()-- method overiding

# class A :
#     def m1(self):
#         print("this is m1 method from class A")
#
# class B(A) :
#     def m1(self):
#         print("this is m1 method from class B")
#         super().m1()   # this will invoke parent class method m1
#
# bobj=B()
# bobj.m1()    ## this is m1 method from class B
#              ## this is m1 method from class A

### ex 7 :
# class A:
#     a,b= 10 , 20
#
# class B(A):
#     i, j = 100 , 200
#     def m1(self,x,y):
#         print(x+y)         ### local variables
#         print(self.i+ self.j)     ## class variables
#         print(self.a+self.b)      ## class variables
#
# bobj=B()
# bobj.m1(1000,2000)        ## 3000
#                                 ## 300
#                                 ## 30

### ex : override variables
class Parent:
    name="Scott"

class Child(Parent):
    name="johnny"  ## overriding the variable value
    def test(self):
        print(super().name)

cobj=Child()
print(cobj.name)     ## johnny
cobj.test()        # Scott


## ex 9 -- overriding methods









