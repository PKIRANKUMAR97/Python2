# Write a program to find the maximum and minimum elements in a tuple.

tuple6=(12,56,23,1,45,89,45,56,234,890)
print(max(tuple6))
print(min(tuple6))




def max_min_tuple(tupl):
    max_val=tupl[0]
    min_val=tupl[0]

    for item in tupl:
        if item> max_val:
            max_val=item
        if item< min_val:
            min_val=item

    return max_val,min_val

maxp,minp=max_min_tuple(tuple6)


print(f"max value is :{maxp}")
print(f"min value is :{minp}")

