# Problem Statement: Rotate a list by K positions.

def rotate_list(lst, k):
    n = len(lst)
    k = k % n
    return lst[k:] + lst[:k]

# Taking input
numbers = list(map(int, input("Enter list elements: ").split()))
k = int(input("Enter number of positions to rotate: "))

# Printing result
result = rotate_list(numbers, k)
print("Rotated list is:", *result)

# output
""" list elements: 1 2 3 4 5
 Enter number of positions to rotate: 2
Rotated list is: 3 4 5 1 2"""