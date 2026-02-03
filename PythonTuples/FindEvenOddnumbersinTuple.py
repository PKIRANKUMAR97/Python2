# Write a program to find even and odd numbers in a tuple.

tuple13=(111, 222, 333, 444, 555, 222, 888, 555,211,567,9860)

def count_even_odd(tuple13):
    even=0
    odd=0
    for item in tuple13:
        if item%2==0:
            even=even+1
        else:
            odd=odd+1

    print(f"even count: {even}")
    print(f"odd count: {odd}")
    return even, odd


count_even_odd(tuple13)