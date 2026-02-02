# Take two lists of integers. Join them into one list,
# remove any duplicates,
# and print the final result in descending order.

nums1 = [10, 20, 30, 40, 50, 20, 60]
nums2 = [100, 200, 300, 40, 500, 20, 600]
nums=nums1+nums2
print(nums)
uniq=set(nums)
l2=list(uniq)
l2.sort(reverse=True)
print(l2)
