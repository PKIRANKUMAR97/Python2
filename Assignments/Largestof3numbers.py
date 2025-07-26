# print the largest of three numbers
a=int(input("Enter a : "))
b=int(input("Enter b : "))
c=int(input("Enter c : "))
if (a>b and a>c):
    print("The number %d is largest" %a)
elif (b>a and b>c):
    print("The number %d is largest" %b)
else:
    print("The number %d is largest" %c)

