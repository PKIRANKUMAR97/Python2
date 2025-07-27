s=str(input())
r_s=""
for i in s:
    r_s=r_s+i
print(r_s)

# s= "abcde"
# step 1   i = last character in string  e , then r_s = e+""= "e"
# step 2   i = d , then r_s = "e"+"d"="ed"
# step 3   i = c ,  then r_s ="ed" + "c" ="edc"
# step 4   i = b ,  then r_s ="edc"+"b" = "edcb"
# step 5   i = a ,  then r_s ="edcb"+"a"= "edcba"
