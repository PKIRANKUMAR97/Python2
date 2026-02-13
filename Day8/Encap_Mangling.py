# Name mangling is how Python implements private properties and methods.
# When you use double underscores __, Python automatically renames it internally by adding _ClassName in front.
## not recommended at all


class Bank:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

b1=Bank("EMP1", 1000)
print(b1.name)
# print(b1.__salary)  ##AttributeError: 'Bank' object has no attribute '__salary' it is private

print(b1._Bank__salary)   ## 1000
