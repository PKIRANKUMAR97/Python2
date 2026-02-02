# 1. The "List Filter" (List Comprehension & Methods)
# Question:
# Given a list of strings names = ["Anna", "Bob", "Alexander", "Ed", "Christopher", "Al"]
# create a new list that contains
# only the names that start with the letter "A" and have more than 3 characters.
# Bonus: Sort this new list by the last character of each name.

names = ["Anna", "Bob", "Alexander", "Ed", "Christopher", "Al"]
newnames=[]
for i in names:
    if "A" in i and len(i)>3:
        newnames.append(i)
print(newnames)

# def func1(l):
#     for j in l:
#
#         l.sort(key=j[-1])
#     print(l)
#
# func1(newnames)

