# ordered and unchangeable
# immutable -- cannot change
# ()

# ex 1 : creating tuple
# mytuple=()     # empty tuple
# mytuple1 = ("alisa","balram","cunner")
# print(mytuple1)

# ex 2 : accessing tuple items
# mytuple = ("alisa","balram","cunner")
# print(mytuple[2])    # index starts with 0 # cunner
# print(mytuple[-2])

## ex 3 : range of indexes

# mytuple =("a","b","c","d","e","f")
# print(mytuple[2:5])
# print(mytuple[-5:-1])

# ex 4 : changing tuple values --- by default we cannot change -- immutable
# we cannot modify existing value
# we cannot append new value
# we cannot insert a new value
# we cannot remove a value

# tuple are more secure than list due to immutable property

## convert to list and then to tuple
# mytuple=("Alice","bunny","cat",100,"elephant","finner","tingo")
# mylist=list(mytuple)
# mylist[0]="Annible"
# mytuple=tuple(mylist)
# print(mytuple) # ('Annible', 'bunny', 'cat', 100, 'elephant', 'finner', 'tingo')

# ex 5 : reading items using loop
# mytuple=("Alice","bunny","cat",100,"elephant","finner","tingo")
# for item in mytuple:
#     print(item)

# ex 6 : check if item exists in tuple
# mytuple=("Alice","bunny","cat",100,"elephant","finner","tingo")
# if "finnerertyu" in mytuple:
#     print("yes , it is present ")
# else :
#     print("no, it is not available  ")

# ex 7 : tuple length -- counting items in a tuple
# mytuple=("Alice","bunny","cat",100,"elephant","finner","tingo")
# print(len(mytuple))

## ex 8 : add items to tuple -- not possible due to immutable
# mytuple=("Alice","bunny","cat",100,"elephant","finner","tingo")
# mytuple[0]="KIRAN"
# print(mytuple)      # TypeError: 'tuple' object does not support item assignment

## EX 9 : copy tuple
# mytuple=("Alice","bunny","cat",100,"elephant","finner","tingo")
# mytuple2=mytuple
# print(mytuple)
# print(mytuple2)

## ex 10 : removing items -- not possible -- immutable

## ex 11 : join/ combine tuple : always possible
# tuple1 = (10,20,30,40,50)
# tuple2 = ("a","b","c","d")
# tuple3 = tuple1 + tuple2
# print(tuple3) # (10, 20, 30, 40, 50, 'a', 'b', 'c', 'd')

## ex 11 : compare tuple
tuple1 = (10,20,30,40,50)
tuple2 = ("a","b","c","d")
if tuple1 == tuple2:
    print("tuple1 is equal to tuple2")
else:
    print("tuple1 is not equal to tuple2")
