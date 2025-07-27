s=str(input("enter the string : "))
num1="0123456789"
updated_s=""
for i in s:
    if i in num1:
        continue
    else :
        updated_s = updated_s + i

print(updated_s)

# s=str(input("enter string: "))
# updated_s =""
# for ch in s:
#     if ch.isdigit():
#         continue
#     else:
#         updated_s = updated_s + ch
# print(updated_s)
