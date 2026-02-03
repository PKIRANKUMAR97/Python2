# Write a program to remove duplicates from a tuple.

tuple14=(111, 222, 333, 444, 555, 222, 888, 555,211,567,9860)
list_r=[]

for item in tuple14:
    if item not in list_r:
        list_r.append(item)

tuple_r=tuple(list_r)

print(tuple_r)