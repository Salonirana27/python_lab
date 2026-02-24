#Find smallest element in a list.


def find_smallest(lst):
    smallest = lst[0]
    for num in lst:
        if num < smallest:
            smallest = num
    return smallest

# Taking input
numbers = list(map(int, input("Enter space-separated numbers: ").split()))

# Printing result
print(find_smallest(numbers))

# output
"""Enter space-separated numbers: 8 3 15 2 9
 2"""