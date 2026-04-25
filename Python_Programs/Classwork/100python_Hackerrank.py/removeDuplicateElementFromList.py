# Remove duplicate elements from list.


def remove_duplicates(lst):
    unique = []
    for num in lst:
        if num not in unique:
            unique.append(num)
    return unique

# Taking input
numbers = list(map(int, input("Enter space-separated numbers: ").split()))

# Printing result
result = remove_duplicates(numbers)
print(*result)

# output
"""Enter space-separated numbers: 1 2 2 3 4 4 5
 1 2 3 4 5"""