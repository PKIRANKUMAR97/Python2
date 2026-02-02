# Adding Items: Start with an empty list called squad.
# Use .append() to add one name,
# .insert() to add a name at the second position,
# and .extend() to add a list of three more names at once.



squad=[]
squad.append("apple")
squad.insert(1,"banana")
squad2=["carrot","dog","pineapple"]
squad.extend(squad2)
print(squad)

# Removing Items: Given nums = [10, 20, 30, 40, 50, 20, 60]:
# Remove the first occurrence of 20.
# Remove the item at index 3.
# Clear the entire list so it becomes [].

nums = [10, 20, 30, 40, 50, 20, 60]
nums.remove(20)
print(nums)
nums.pop(3)
print(nums)
nums.clear()
print(nums)



