# Problem Statement: Find average of list elements.

def find_average(lst):
    total = 0
    for num in lst:
        total += num
    return total / len(lst) if len(lst) > 0 else 0

# Taking input
numbers = list(map(int, input("Enter list elements: ").split()))

# Printing result
print("Average of elements is:", find_average(numbers))

# output
""" Enter list elements: 10 20 30 40
Average of elements is: 25.0 """