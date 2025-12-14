"""
print unique characters in string
str='test'
o/p -- e,s
"""
str=input("Enter a string: ")
unique=[]
for char in str:
    if str.count(char) ==1 and char not in unique:
        unique.append(char)
print(unique)
print(','.join(unique))
