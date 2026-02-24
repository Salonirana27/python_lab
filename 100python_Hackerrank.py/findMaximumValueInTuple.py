# Problem Statement: Find maximum value in a tuple.

def find_maximum(tpl):
    maximum = tpl[0]
    for num in tpl:
        if num > maximum:
            maximum = num
    return maximum

# Taking input
numbers = tuple(map(int, input("Enter tuple elements: ").split()))

# Printing result
print("Maximum value is:", find_maximum(numbers))

# output
""" Enter tuple elements: 12 45 7 89 23
Maximum value is: 89 """