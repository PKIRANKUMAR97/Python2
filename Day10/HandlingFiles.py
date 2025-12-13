### ex 1 : writing data into text file
# file=open("C:/Demofiles/myfiles.txt","w")
# file.write("this is my first statement....\n")
# file.write("this is my second statement....\n")
# file.write("this is my third statement....\n")
# file.write("this is my forth statement....\n")
# file.write("this is my fifth statement....\n")
# file.close()
# print(" completed ")

### ex 2 : reading data from text file
# file=open("C:/Demofiles/myfiles.txt","r")
# # print(file.read())
# print(file.readline())
# file.close()

### ex 3 : appending data into text file
file=open("C:/Demofiles/myfiles.txt","a")
file.write("this is sixth line ....")
file.write("this is seventh line ....")
file.close()
print("program completed")


