# basic class, object

# class Myclass:
#     def myfunc1(self):
#         pass
#     def myfunc2(self):
#         print("myfunc2")
#
#     def myfunc3(self):
#
# mc1obj1=Myclass()
# mc1obj1.myfunc1()
# mc1obj1.myfunc2()


list=[1,2,3,4,5]

max=0
max2=0

for item in list:
    if item > max:
        max2 = max
        max=item

    if max2< max and item!=max :
        max2=item

print(max2)














