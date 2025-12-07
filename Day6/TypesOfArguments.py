#ex 1 :
def function(i,j):
    print(i,j)
function(2,3)    # positional arguments
function(j=20,i=10)   # keyword arguments

# ex 2 : default values assigned to positional arguments

def function(i,j=10):
    print(i,j)
function(100,200) # 100 200 # j=10 is replaced
function(100)          # 100 10 # taken the default value of j =10

# ex 3 : keyword arguments
def greetings(name , greetmsg):
    print(greetmsg+" "+name)

greetings(name='kiran',greetmsg='Hello') # Hello kiran
greetings(greetmsg='Hello',name='kiran') # Hello kiran

# ex 4 :combination of keyword and positional arguments
def function(a,b,c):
    print(a,b,c)

function(10,20,30) # positional arguments
function(a=10,b=20,c=30) # keyword arguments
function(c=30,a=10,b=20) # keyword arguments
function(10,20,c=30) # 10 20 30
function(10,b=20,c=30)  #  10 20 30
#function(10,b=20,30)   # Positional argument after keyword argument
#function(10,30,b=20) # function() got multiple values for argument 'b'


#ex 5 : function can return multiple values

def largest(a,b):
    if a > b:
        return a,b
    else :
        return b,a

print(largest(10,20))




