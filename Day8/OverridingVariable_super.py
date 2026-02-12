class Parent:
    name="Kiran"

class Child(Parent):
    name="Aisha"
    def test(self):
        print(super().name)

cobj=Child()
print(cobj.name)
cobj.test()