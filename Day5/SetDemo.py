## set is a collection which is unordered and unindexed, mutable
## {}
## ex1 : create set

# myset ={"Alice","bunny","cat",100,"elephant","finner","tingo"}
# print(myset) ## {'tingo', 100, 'bunny', 'Alice', 'cat', 'finner', 'elephant'} ## unordered

## ex 2: accessing items
## loop statement
# myset ={"Alice","bunny","cat",100,"elephant","finner","tingo"}
# for item in myset:
#     print(item)

## ex 3 : items exist in set or not -- in operator
# myset ={"Alice","bunny","cat",100,"elephant","finner","tingo"}
# print("cat" in myset)
# print("zebra" in myset)

## ex 4 : adding items to set

## add() -- single item at a time
# myset ={"Alice","bunny","cat",100,"elephant","finner","tingo"}
# myset.add("hyderabad")
# print(myset)

##update() -- multiple items at a time
# myset ={"Alice","bunny","cat",100,"elephant","finner","tingo"}
# myset.update(["hyderabad","chennai"])
# print(myset)

## ex 5 : length of set -- no of items in set
# myset ={"Alice","bunny","cat",100,"elephant","finner","tingo"}
# print(len(myset))

## ex 6 : remove items from set
## remove()
# myset ={"Alice","bunny","cat",100,"elephant","finner","tingo"}
# myset.remove(100)
# #myset.remove(10000)  ## key error
# print(myset)

## discard()
# myset ={"Alice","bunny","cat",100,"elephant","finner","tingo"}
# #myset.discard(100)
# myset.discard(10000)  ## no error if the item does not exist too
# print(myset)

## ex 7 : clear all items from set -- set variable is still available
# myset ={"Alice","bunny","cat",100,"elephant","finner","tingo"}
# myset.clear()
# print(myset)


# myset ={"Alice","bunny","cat",100,"elephant","finner","tingo"}
# del myset # delete the set along with variable
# print(myset)   # NameError: name 'myset' is not defined

## ex 8 : join / combine sets
# myset1 ={"Alice","bunny","cat",100,"elephant","finner","tingo"}
# myset2= {1,2,3,4,5}
# set3 = myset1.union(myset2)
# print(set3)


# myset1 ={"Alice","bunny","cat",100,"elephant","finner","tingo"}
# myset2= {1,2,3,4,5}
# myset1.update(myset2)
# print(myset1)

myset1 ={"Alice","bunny","cat",100,"elephant","finner","tingo"}
myset2= {1,2,3,4,5}
set3=myset1.update(myset2)
print(set3)      ## why is it showing None as o/p

## set.update() does not return a new set.
## Instead, it modifies the original set in-place and returns None.




