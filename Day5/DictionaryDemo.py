## key and value pair
## unordered , changeable , mutable , indexed
## {} -- ite
"""
p1=100
p2=200
p3=300
"""

## ex1 : creating dictionary
# mydict={101:"x",102:"y",103:"z"}
# print(mydict)

## ex2 : access items from dict

# mydict={
#     "brand":"Ford",
#     "model":"Mustang",
#     "year":1964
# }
# print(mydict["brand"])
# print(mydict["model"])
## using get()
# x=mydict.get("model")
# print(x)

## ex 3 -- change values in dict
# mydict={
#     "brand":"Ford",
#     "model":"Mustang",
#     "year":1964
# }
# print(mydict)
# mydict["year"]=2002
# print(mydict)

## ex 4 : reading items from dict using loop
# mydict={
#     "brand":"Ford",
#     "model":"Mustang",
#     "year":1964
# }

# for i in mydict:
#     print(i)         ## prints only keys from dictionary
#
# for i in mydict:
#     print(mydict[i])  ## prints only values from dictionary

# for i in mydict.values():
#     print(i)
#
# for i in mydict.keys():
#     print(i)
#
# for key , value in mydict.items():
#     print(key,value)     ## print keys, values

## ex 5 :  key is existing in dict or not
# mydict={
#     "brand":"Ford",
#     "model":"Mustang",
#     "year":1964
# }

# if "brand2" in mydict:
#     print(" exists")
# else:
#     print(" not exists")
#
# print("model" in mydict)

## ex 6 : number of items in dict
# mydict={
#     "brand":"Ford",
#     "model":"Mustang",
#     "year":1964
# }

# print(len(mydict))

## ex 7 :adding items to dictionary
# mydict={
#     "brand":"Ford",
#     "model":"Mustang",
#     "year":1964
# }

# mydict["color"]="black"
# print(mydict)

## ex 8 : removing items from dictionary

# mydict={
#     "brand":"Ford",
#     "model":"Mustang",
#     "year":1964,
#     "color":"blue"
# }
#
# ## pop()
# mydict.pop("color")
# print(mydict)
#
# ## del
# del mydict["year"]
# print(mydict)        # delete specific items
#
# del mydict
# print(mydict)        # delete whole dict along with name variable # NameError: name 'mydict' is not defined. Did you mean: 'dict'?

## clear()

# mydict={
#     "brand":"Ford",
#     "model":"Mustang",
#     "year":1964,
#     "color":"blue"
# }

# mydict.clear()
# print(mydict)    # delete items , but dict variable is available with empty items

## ex 9 : copy dict
mydict={
    "brand":"Ford",
    "model":"Mustang",
    "year":1964,
    "color":"blue"
}
# using copy()
mydict2=mydict.copy()
print(mydict2)
# without using copy()
mydict3 = mydict
print(mydict3)








