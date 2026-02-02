# 4. The "Frequency Map" (Loops & Count)
# Question: Write a program that takes a list of items and prints a "frequency report."
# For every unique item in the list, print how many times it appears.
# Example Input: ["apple", "banana", "apple", "cherry", "banana", "apple"]
# Example Output: apple: 3, banana: 2, cherry: 1
# Hint: Use a set() to find unique items first, then loop and use .count().

l1=["apple", "banana", "apple", "cherry", "banana", "apple"]
uniq=set(l1)

for i in uniq:
    print(f"{i} --> {l1.count(i)}")