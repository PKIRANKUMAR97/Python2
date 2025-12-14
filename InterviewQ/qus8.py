"""
write one line for loop to print all the words in the below list which starts with character 'i'
list=['india','is','my','country']
o/p -- ['india','is']
"""

list1=['india','is','my','country']
list2=[word for word in list1 if word.startswith('i')]
print(list2)
