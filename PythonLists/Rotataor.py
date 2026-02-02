# 2. The "Rotator" (Slicing & Joining)
# Question: Write a function rotate_list(lst, k)
# that takes a list and an integer k,
# and rotates the list to the right by k steps.
# Example: If lst = [1, 2, 3, 4, 5] and k = 2, the result should be [4, 5, 1, 2, 3].
# Hint: Use slicing and the + operator.

# lst = [1, 2, 3, 4, 5]
# a=lst[-1]
# print(a)
# lst.pop()
# print(lst)
# lst.insert(0,"ADC")
# print(lst)

def funR(l,k):
    while k > 0:

        a=l[-1]
        l.pop()
        l.insert(0,a)

        k=k-1
    print(l)
l1=[1, 2, 3, 4, 5]
k=1
funR(l1,3)
#########################################################
def rotate_list(lst, k):
    if not lst:
        return lst

    k = k % len(lst)   # handle cases where k > length
    return lst[-k:] + lst[:-k]


# Example
lst = [1, 2, 3, 4, 5]
print(rotate_list(lst, 2))
