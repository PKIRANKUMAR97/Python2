# print the largest of two numbers
a=int(input("Enter a : "))
b=int(input("Enter b : "))
if a>b:
    print("The number %d is largest" %a)
elif a<b:
    print("The number %d is largest" %b)
else:
    print("The number %d is equal to %d" %(a,b))