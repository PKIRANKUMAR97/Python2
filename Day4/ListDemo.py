#ex 1: create list --
##represent multiple value in a single entity
##ordered , changeable , mutable

mylist1=[10,20,30,40,50]
mylist2=["Alice","bunny","cat"]
mylist3=["KIRAn",10,"PARDHU",34]
mylist=list()   # empty list

print(mylist1)
print(mylist2)
print(mylist3)
print(mylist)

# ex 2 : accessing items from the list
mylist=["Alice","bunny","cat"]   # index starts from 0 # -1 means last item
print(mylist[0])
print(mylist[1])
print(mylist[2])
print(mylist[-1])

# ex3 : range of indexes --
mylist=["Alice","bunny","cat","dongly","elephant","finner","tingo"]
print(mylist[2:5])  # ['cat', 'dongly', 'elephant'] -- here nth element is discarded and it will print only n-1 element

print(mylist[-4:-1]) # ['dongly', 'elephant', 'finner']

# ex 4 : change item values in list
mylist=["Alice","bunny","cat","dongly","elephant","finner","tingo"]
print(mylist)
mylist[0]="Ais"
print(mylist)

# ex 5 :  read the list items using loop statements
mylist=["Alice","bunny","cat","dongly","elephant","finner","tingo"]
for i in mylist:
    print(i)

# ex 6 : check if the item exists in the list or not
mylist=["Alice","bunny","cat","dongly","elephant","finner","tingo"]
if "cattttt" in mylist:
    print(" cat is present")
else:
    print(" cat is not present")

# ex 7 : list length -- count number of items in the list
mylist=["Alice","bunny","cat","dongly","elephant","finner","tingo"]
print(len(mylist))

# ex 8 : add new items in list
##append -- new item will be added at the end of list
##insert -- new item will be added somewhere in the list

mylist=["Alice","bunny","cat","dongly","elephant","finner","tingo"]
mylist.append("zebra")
print(mylist)

mylist.insert(0,"ALAAA")
print(mylist)

# ex 9 :
##pop()

mylist=["Alice","bunny","cat","dongly","elephant","finner","tingo"]
mylist.pop(0) # we need to specify the index not the value
print(mylist)

##del # del command removes single item based on the index provided
mylist=["Alice","bunny","cat","dongly","elephant","finner","tingo"]
del mylist[2]   # cat will be removed from list
print(mylist)    # ['Alice', 'bunny', 'dongly', 'elephant', 'finner', 'tingo']

##clear()   # it will clear all items
mylist=["Alice","bunny","cat","dongly","elephant","finner","tingo"]
mylist.clear()
print(mylist)       # it will return empty list

# ex 10 : copy list into another list
# list()
mylist1=["Alice","bunny","cat","dongly","elephant","finner","tingo"]
# mylist2=list(mylist1)
mylist2=mylist1
print(mylist1)
print(mylist2)
print(type(mylist1))
print(type(mylist2))

###copy()
mylist1=["Alice","bunny","cat","dongly","elephant","finner","tingo"]
mylist2=mylist1.copy()
print(mylist2)

# example 11 : combine / join lists
##using + operator
mylist1=["a","b","c","d","e","f"]
mylist2=[1,2,3]
mylist3=mylist1+mylist2
print(mylist3)

##using loop statement
mylist1=["a","b","c","d","e","f"]
mylist2=[1,2,3]

for item in mylist1:
    mylist2.append(item)
print(mylist2)

for itemm in mylist2:
    mylist1.append(itemm)
print(mylist1)

##using extend()
mylist1=["a","b","c","d","e","f"]
mylist2=[1,2,3]
mylist1.extend(mylist2)
print(mylist1)    # ['a', 'b', 'c', 'd', 'e', 'f', [1, 2, 3]]

mylist2.extend(mylist1)
print(mylist2)

## ex 12 : compare lists
mylist1=["a","b","c","d","e","f"]
mylist2=[1,2,3]
if mylist1==mylist2:
    print(" both are equal ")
else :
    print(" both are not equal ")