"""
combine 2 lists and convert them into dictionary as shown below
list1=['a','b','c']
list2=['1','2','3']
exp o/p == {}
"""
list1=['a','b','c']
list2=[1,2,3]
# x=zip(list1,list2)
# print(dict(x))
#
# dic2={list1[i]:list2[i] for i in range(len(list1))}
# print(dic2)

dict3={}
for key in list1:
    for value in list2:
        dict3[key]=value
        list2.remove(value)
        break

print(dict3)