### 1 . Reverse a given string

# str = "Mahabharatam"
# print(str[::-1])    ## matarahbahaM

### 2 . Check if a string is a palindrome
# str1=input("Enter your string: ")
# str2=str1[::-1]
# if str1==str2:
#     print("it is a palindrome ")
# else:
#     print("not a palindrome")

## 3 . Count the number of characters in a string
# str1=input("Enter your string: ")
# print(len(str1))
#
# noofchar=0
# for i in range (0,len(str1)):
#     noofchar=noofchar+1
# print(noofchar)

## 4 . Count vowels and consonants in a string

# str1=input("Enter your string: ")
# nvowels=0
# nconsonants=0
# for char in str1:
#     if char in ['a','e','i','o','u']:
#         nvowels+=1
#     else:
#         nconsonants+=1
#
# print(nvowels)
# print(nconsonants)

## 5 . Remove duplicate characters from a string
# str1=input("Enter your string: ")
# str2=''
# for i in range(len(str1)):
#     if str1[i] not in str2:
#         str2+=str1[i]
# print(str2)

###6 . Find the length of a string without using len()

# str1=input("Enter your string: ")
# leng=0
# for char in str1:
#     leng=leng+1
#
# print(leng)


### 7 . Convert all characters in a string to uppercase without using upper()

# str1=input("Enter your string: ")
# str2=''
# for char in str1:
#     if 'a' <= char <= 'z':
#         char_code=ord(char)
#         upper_char_code=char_code-32
#         str2=str2+chr(upper_char_code)
#     else:
#         str2=str2+char
#
# print(str2)

### 8 . Check whether a string contains only alphabets
# str1=input("Enter your string: ")
# str2=''
# str3=''
#
# for char in str1:
#     if ('a' <= char <= 'z') or ('A' <= char <= 'Z'):
#         str2= str2+char
#
#     else:
#         str3=str3+char
#
# if len(str3) >0:
#     print("mixed of characters and others")
# else:
#     print(" only charcters")

### 9 . Find the first non-repeating character in a string

str1=input("Enter your string: ")






