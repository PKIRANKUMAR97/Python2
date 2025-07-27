s=str(input("enter string: "))
updated_s =""
for ch in s:
    if ch.isalnum():
        updated_s = updated_s + ch
print(updated_s)