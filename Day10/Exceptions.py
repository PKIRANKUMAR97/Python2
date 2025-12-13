## exception handling
## exception is an event which will cause program termination
##except -- executes only when exception occurred
## else --executes only when exceptions are not occurred
## finally -- always execute ....

## try , except , else
## ex 1:'

# print("this is the starting point of the program .....")
# print("this is the starting point of the program .....")
# print("this is the starting point of the program .....")
# try:
#     print(x)
# except:
#     print("exception occured")
#
# print("this is the end of the program .....")
# print("this is the end of the program .....")
# print("this is the end of the program .....")

## example 2 :
# print("this is the starting point of the program .....")
# print("program in progress")
# try:
#     print(10/5)
# except ZeroDivisionError:
#     print("exception occured and then handled ..")
# print("program completed succesfully at the end..")

## ex 3 : multiple except blocks -- try , except else , finally

# try :
#     n1, n2 = 10, 0
#     res = n1/n2
#     print("result is : ",res)
# except ZeroDivisionError :
#     print("division by zero")
# except SyntaxError :
#     print(" thrown SyntaxError exception")
# except :
#     print ("exception handled successfully")
# else :
#     print(" no exceptions found in the program")
# finally:
#     print("always execute this finally block ")

### ex 4 : raising our own exceptions
# def enterage(num):
#     if num < 0:
#         raise ValueError("only integers are allowed")
#     if num%2==0:
#         print("even")
#     else:
#         print("odd")
#
# print("checking the number is even or odd by calling the function enterage")
# num=int(input("enter the number"))
#
# try:
#     enterage(num)
# except ValueError :
#     print("value error exception occurred and handled successfuly")
#
# print("program completed ...")



