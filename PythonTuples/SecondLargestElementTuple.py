# Write a program to find the second-largest element in a tuple
tuple16=(111, 222, 333, 444, 555, 222, 888, 555,211,567,9860)
# sorted_tuple=tuple(sorted(tuple16))
# print(sorted_tuple)

def second_largest(tuple16):
    lar1=lar2=float('-inf')
    for item in tuple16:
        if item>lar1:
            lar2=lar1
            lar1=item
        elif item>lar2 and item!=lar1:
            lar2=item
    return lar2

print(second_largest(tuple16))




