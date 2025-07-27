# create string variable
# s='hanacloud'
# s1=str('hanasap')

# creating empty strings
# name=str()
# name=""
# name=''

# mutable - can't change the value of variable
# immutable -- can change the value of variable
# string is immutable

# str1='SAP'
# print(id(str1))   #2124465320416
#
# str1=str1+'HANA'
# print(id(str1))   #2124469109648

# If the value is changed after updation then it is immutable

# ex 3 : + and *  with string

# str1='hana'
# print(str1+'cloud') # hanacloud
# print(str1*2) # hanahana

# ex4 : slicing
# starting index 0
# ending index 1
# str3='welcometosaphana'
# print(str3[1:3])       # el
# print(str3[:6])        # starting index is 0 # welcom
# print(str3[2:])        # lcometosaphana
# print(str3[1:-1])      # -1 : removes the last 1 character # elcometosaphan
# print(str3[1:-2])      # -2 : remove the last 2 characters # elcometosapha

#Ex5 : ord() and chr()
# ord() --- gives equalant ASCII character value
# chr() --- returns character represented by an ASCII number
# print(ord('A'))
# print(chr(65))

# ex 6 : max() , min(),len()
# print(max("existed"))  # x
# print(min("existad"))  # a
# print(len("existed"))  # 7

# ex 7 : in ,not_in operators returns boolean
# in -- returns true if part of string is present in main string
# not_in --
# s='saphanacloud'
# print('sap' in s) # True
# print('aap' in s) # False
# print('sap' not in s) # False
# print('aap' not in s) # True

#ex 8 -- string comparision
# print("tim"=="tie") # False
# print("hana"!="saphana") # True
# print("hana">"han") # True
# print("right">="left") # True
# print("hana"<"han") # False
# print("hana"<="hane") # True
# print("hana">"")    # True

#ex 9 : testing strings  True/False
# s="sap hana cloud"
# print(s.isalnum())    # False
# print("hana".isalpha())   #Trur
# print("2012".isdigit())   # True
# print("first Number".isidentifier()) # False -- check for keyword
# print(s.islower()) # True
# print("HANA".isupper())  # True
# print(" ".isspace()) # True
# print(s.isspace()) # False

# ex 10 : searching for Substrings
# s="sap hana sap cloud"
# print(s.endswith("oud"))  # True
# print(s.endswith("noud")) # False
# print(s.startswith("sap")) # True
# print(s.startswith("asap")) # False
# print(s.find("hana")) # 4   returns position
# print(s.find("haana"))  # -1   not found
# print(s.count("sap"))   # 2 no of occurrences

# ex 11 : Converting strings
# s = "String in PYTHON"
# s2 = s.title()   # every first character in the word converts to Upper Case
# print(s2)
# s3 = s.upper()    # every character is converted to uppercase
# print(s3)
# s4 = s.lower()    # every character is converted to lowercase
# print(s4)
# s5 = s.capitalize() # only first character of string is in uppercase
# print(s5)
# s6 = s.swapcase()   # lower to upper ,upper to lower case
# print(s6)
# s7 = s.replace("in","on")
# print(s7)

# EX --12 : reverse a string
# method 1 : looping statements
s ="welcome"
rev_str=""
for i in s:
    rev_str=i+rev_str
print(rev_str)

# method 2 : slicing
s ="welcome"
rev_str=s[::-1]
print(rev_str)