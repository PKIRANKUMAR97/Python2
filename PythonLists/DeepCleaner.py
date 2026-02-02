# 3. The "Deep Cleaner" (Loops & Removing)
# Question:
# Given a list that contains several duplicates of the number 0,
# such as nums = [0, 1, 0, 3, 12, 0, 5],
# write a script that moves all the 0s to the end of the list
# while maintaining the relative order of the non-zero elements.
#
# Constraint: Do this in-place (modify the original list) without creating a new list.

nums=[0, 1, 0, 3, 12, 0, 5]
count_zero = nums.count(0)

nums[:] = [n for n in nums if n != 0]
print(nums)
nums.extend([0] * count_zero)

print(nums)
