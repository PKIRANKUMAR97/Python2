# Q1. Create a Student class
#
# Create a class Student
#
# Constructor should accept: name, marks
#
# Create a method display() to print student details
#
# Create object and call method

class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def studentdetails(self):
        print(f"student name :{self.name}")
        print(f"student marks :{self.marks}")

student_object=Student("Kiran",78)
student_object.studentdetails()