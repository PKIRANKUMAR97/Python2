# We will build a "Smart Employee" system where data is added at every step.
#
# The Challenge: The University Payroll
# Level 1 (Grandparent): Member
# __init__ accepts name and member_id.
# Method display_base() prints "ID: [member_id] | Name: [name]".

class Member:
    def __init__(self,name,member_id):
        self.name = name
        self.member_id = member_id

    def display_base(self):
        print(f"ID: {self.member_id} | Name: {self.name}")



# Level 2 (Parent): Staff (inherits from Member)
# __init__ accepts name, member_id, and department.
# Method display_staff() calls display_base() and then prints "Dept: [department]".

class Staff(Member):
    def __init__(self,name,member_id,department):
        super().__init__(name,member_id)
        self.department = department

    def display_staff(self):
        super().display_base()
        print("Department:",self.department)


# Level 3 (Child): Professor (inherits from Staff)
# __init__ accepts name, member_id, department, and subject.
# Method display_prof() calls display_staff() and then prints "Subject: [subject]".

class Professor(Staff):
    def __init__(self,name,member_id,department,subject):
        super().__init__(name,member_id,department)
        self.subject = subject

    def display_prof(self):
        super().display_staff()
        print("Subject: ",self.subject)
#
# Your Tasks:
# Ensure that Professor successfully passes all 4 pieces of data up the chain.
#
# Create an object: prof = Professor("Dr. Smith", "U789", "Science", "Physics").
prof = Professor("Dr. Smith", "U789", "Science", "Physics")
# Call only prof.display_prof() to see if all three lines of info print correctly.
prof.display_prof()
# Logic Check: When you call display_prof(), it should trigger display_staff(),
# which should trigger display_base(). It's like a row of dominoes!

