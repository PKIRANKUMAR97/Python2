# The Project Architecture
# Level 1 (Simple): Person (Grandparent) — Handles name.
# Level 2 (Multi-level): Employee (Parent) — Inherits from Person, adds employee_id.
# Level 3 (Multiple Inheritance): * Doctor — Inherits from Employee, adds specialty.
# Researcher — Inherits from Employee, adds lab_id.
# MedicalScientist — Inherits from both Doctor and Researcher.

class Person:
    def __init__(self,name,**kwargs):
        super().__init__(**kwargs)
        self.name=name
class Employee(Person):
    def __init__(self,employee_id,**kwargs):
        super().__init__(**kwargs)
        self.employee_id=employee_id

class Doctor(Employee):
    def __init__(self,speciality,**kwargs):
        super().__init__(**kwargs)
        self.speciality=speciality

    def perform_surgery(self):
        print(f"{self.name} performed surgery {self.speciality}")

class Researcher(Employee):
    def __init__(self,lab_id,**kwargs):
        super().__init__(**kwargs)
        self.lab_id=lab_id

    def conduct_study(self):
        print(f"{self.name} conducted study in lab {self.lab_id}")

class MedicalScientist(Doctor,Researcher):
    def __init__(self,name,employee_id,speciality,lab_id):
        super().__init__(name=name,employee_id=employee_id,speciality=speciality,lab_id=lab_id)

    def work_summary(self):
        print(f"{self.name} ")
        print(f"{self.employee_id}")
        self.perform_surgery()
        self.conduct_study()

scientist=MedicalScientist("Aisha",1,"Ortho",23)
scientist.work_summary()
print(MedicalScientist.mro())