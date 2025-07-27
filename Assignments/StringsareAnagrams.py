s1=str(input("Enter first string: "))
s2=str(input("Enter second string: "))
if sorted(s1) == sorted(s2):
    print("anagram")
else:
    print("not anagram")