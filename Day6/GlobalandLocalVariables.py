## ex 2:
# xy = 100 ## global variable
# def func():
#     xy = 200  ## local variable
#     print(xy)
# func()  ## 200

##ex 3: using global variable in local variable and update the value
# xy = 100 ## global variable
#
# def func():
#     global xy
#     xy = 200  ## global variable
#     print(xy)
#
# func()  ## 200
# print(xy) ##200

## ex 4 :
# x= 100
# def cool():
#      global x
#      x= 500
#      print(x)
# #cool()  # 500
# print(x) # 100

## ex 5 :
## there isd no need to declare global variables outside the function
## you can declare them global inside the function too -- need to use 'global' keyword
def cool():
    global x
    x = 100
    print(x)

cool()    # 100
print(x)  # 100 # able to access bcz it is global variable


