# 6. The "Safety Index" (Methods & Error Handling)
# Question: Write a function safe_remove(my_list, target) that:
# Checks if the target exists in the list using count() or in.
# If it exists, removes it.
# If it doesn't exist, prints "Item not found" instead of crashing.

def safe_remove(my_list, target):
    if target in my_list:
        my_list.remove(target)     
    else:
        print("Item not found")


my_list=[1,2,3,4,5]
target = 4
safe_remove(my_list, target)
print(my_list)
