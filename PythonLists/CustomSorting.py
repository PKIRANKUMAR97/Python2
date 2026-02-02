# Write a program that sorts a list of strings
# based on the length of the words (shortest to longest),
# rather than alphabetically.

fruits=['apple', 'bananas', 'carrot', 'dog', 'pineapple']

def f1(items):
    return len(items)

fruits.sort(key=f1)
print(fruits)

