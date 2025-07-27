s=str(input("enter the string : "))
Vowels="aeiouAEIOU"
v=c=0
for i in s:
    if i.isalpha():
        if i in Vowels:
            v=v+1
        else :
            c=c+1
print(v)
print(c)