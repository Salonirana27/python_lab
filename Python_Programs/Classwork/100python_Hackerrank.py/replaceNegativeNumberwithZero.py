# Problem Statement: Replace negative numbers with zero.

def replace_negatives(lst):
    result = []
    for num in lst:
        if num < 0:
            result.append(0)
        else:
            result.append(num)
    return result

# Taking input
numbers = list(map(int, input("Enter list elements: ").split()))

# Printing result
updated_list = replace_negatives(numbers)
print("Updated list is:", *updated_list)

# output
""" Enter list elements: 5 -3 8 -1 4
 Updated list is: 5 0 8 0 4 """