"""
take the below 2 lists  as input and print the expected out put
list1=['my','name']
list2=['is','Krishna']
expected o/p -- my name is Krishna
"""
list1=['my','name']
list2=['is','Krishna']
list3=list1+list2
print(list3) ## ['my', 'name', 'is', 'Krishna']
list1.extend(list2)
print(list1)  ## ['my', 'name', 'is', 'Krishna']
print((''.join(list1))) ## It joins all elements of list1 into a single string and prints it.All elements must be strings, not numbers. ## mynameisKrishna
print((' '.join(list1))) ## It joins all elements of list1 into a single string and prints it.All elements must be strings, not numbers.## my name is Krishna
print((','.join(list1))) ## It joins all elements of list1 into a single string and prints it.All elements must be strings, not numbers.## my,name,is,Krishna


