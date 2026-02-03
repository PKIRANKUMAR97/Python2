# Write a program to sum all elements in a tuple.
tuple12=(111, 222, 333, 444, 555, 222, 888, 555)

def sum_all_elements(tuple12):
    sum=0
    for item in tuple12:
        sum=sum+item

    return sum

print(sum_all_elements(tuple12))