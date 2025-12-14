class A:
    def demo(self):
        print("in class A")

class B(A):
    def demo(self):
        print("in class B")

class C(A):
    def demo(self):
        print("in class C")

class D(B, C):
    pass

obj = D()
obj.demo()    ## due to Method resolution optimization property , claas B method is called -- when we are inheriting 2 classes , first inherited class  is called 