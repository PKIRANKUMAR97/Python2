s= "Indiansereloyal"
print(s[-1])
print(s[:-1])
print(s[::-1])
print(s[1:10:1])
print(s[1:10:2]) ## in the iteration it will take every second character
"""
start with character n -- index value 1 
since we gave step as 2 , it will take every second character i.e 1+2 = 3rd , 3+ 2 = 5th,5+2 =7th ,7+2= 9th
since the ending index is 10 and it should be excluded , it will print till the 9th index onlyy 
"""
print(s[1:10:3])
"""
start with character n -- index value 1 
since we gave step as 3 , it will take every third character i.e 1+3=4th index , 4+3 = 7th index ...
since the ending index is 10 and it should be excluded , it will print till the 9th index onlyy
"""