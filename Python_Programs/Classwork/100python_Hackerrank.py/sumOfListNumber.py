# Problem Statement: Find sum of list elements.

def find_sum(lst):
    total = 0
    for num in lst:
        total += num
    return total

# Taking input
numbers = list(map(int, input("Enter list elements: ").split()))

# Printing result
print("Sum of elements is:", find_sum(numbers))

#output
"""Enter list elements: 10 20 30 40
 Sum of elements is: 100 """