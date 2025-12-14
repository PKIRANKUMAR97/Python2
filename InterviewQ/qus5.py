"""
find duplicate characters in the below list
list=['india','is','my','country']
o/p =['i','n','y']

"""

list=['india','is','my','country']
str=''.join(list)
print(str)
duplicates=[]
for char in str:
    if str.count(char) > 1 and char not in duplicates:
        duplicates.append(char)
print(duplicates)
print(* duplicates)