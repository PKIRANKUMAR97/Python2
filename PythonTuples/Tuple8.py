# Write a program to find the index of an element in a tuple.
tuple7=(111,222,333,444,555,222,888,555)
print(tuple7.index(888))

for index in range(len(tuple7)):
    print(f"index is :{index} and value is :{tuple7[index]}")