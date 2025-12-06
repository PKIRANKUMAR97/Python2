# jumping statements --break , continue

# for i in range(1,10):
#     if i==5:
#         break
#     print(i)
# print("existed")

# for i in range(1,10):
#     if i==5:
#         continue    # it will skip 5
#     print(i)
# print("existed")

for i in range(1,10):
    if i==5 or i==8:
        continue    # it will skip 5 ,8
    print(i)
print("existed")
