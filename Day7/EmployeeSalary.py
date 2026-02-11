# Q4. Employee Salary
# Constructor → name, salary
# Method → annual_salary()
# Method → increment(percent)

class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def annual_salary(self):
        print("The annual salary of the employee is ",self.salary*12)

    def increment_salary(self,percent):
        self.salary = self.salary + self.salary * percent/100
        print("The annual salary of the employee after the increment is ",self.salary)

emp_obj=Employee("John",2000)
emp_obj.annual_salary()
emp_obj.increment_salary(10)





