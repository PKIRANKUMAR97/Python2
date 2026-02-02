# Challenge: The "Sub-List Sum"
# Question: Given a list of numbers, find all the "even-indexed" items,
# double their values, and then find the sum of the entire list.
# Example: [10, 20, 30, 40].
# Even indices are 0 and 2 (values 10 and 30).
# Doubled: 20 and 60.
# List becomes [20, 20, 60, 40]. Total sum = 140.


numbers = [10, 20, 30, 40]
numbers[0::2] = [x * 2 for x in numbers[0::2]]

print(numbers)

print(sum(numbers))
