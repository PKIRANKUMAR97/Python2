class Student:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks

    def get_marks(self):
        return self.__marks

    def get_status(self):
        if self.__marks >=60:
            print("Passed the exam")
        else:
            print("Failed the exam")

    def set_marks(self,marks):
        if 0<=marks<=100:
            self.__marks = marks
        else:
            print("Invalid marks")

s1 = Student("John", 8)
print(s1.get_marks())
s1.get_status()
s1.set_marks(90)
print(s1.get_marks())
s1.get_status()

