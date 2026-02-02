# Write a for loop that prints every item in a list along with its index number
# (e.g., "Index 0: Apple").
# Hint: Use enumerate() or range(len()).

nums = [10, 20, 30, 40, 50, 20, 60]
for index in range(len(nums)):
    print(f"Index {index}: {nums[index]}")

numsquare = [x**2 for x in nums]
print(numsquare)