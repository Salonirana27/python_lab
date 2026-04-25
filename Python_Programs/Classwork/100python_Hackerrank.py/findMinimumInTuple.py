# Problem Statement: Find minimum value in a tuple.

def find_minimum(tpl):
    minimum = tpl[0]
    for num in tpl:
        if num < minimum:
            minimum = num
    return minimum

# Taking input
numbers = tuple(map(int, input("Enter tuple elements: ").split()))

# Printing result
print("Minimum value is:", find_minimum(numbers))

# output
""" Enter tuple elements: 12 45 7 89 23
 Minimum value is: 7 """