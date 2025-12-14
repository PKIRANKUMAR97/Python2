## EX1 :
# s='Indiaismycountry'
# print(s[0])
# print(s[6])
# print(s[16])  ### IndexError: string index out of range
# print(s[6.0])   ### TypeError: string indices must be integers, not 'float'

# ## string slicing
# s = "GeeksforGeeksinIndia"
# print(s[1:4])    # characters from index 1 to 3
# print(s[:3])     # from start to index 2
# print(s[3:])     # from index 3 to end
# print(s[::-1])   # reverse string

### string iteration
# s = "Pythonfortesteing"
# for char in s:
#     print(char)

### string replacing
# s = "hello geeks"
# s1 = "H" + s[1:]                   # update first character
# s2 = s.replace("geeks", "Indians")  # replace word
# print(s1)
# print(s2)

### strip
s = "   Indians             "
print(s.strip())

s = "Python is fun"
print(s.replace("fun", "awesome"))