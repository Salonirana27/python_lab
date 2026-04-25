#Return unique elements from a list using function.

def unique_elements(lst):
    unique = []
    for item in lst:
        if item not in unique:
            unique.append(item)
    return unique

# Taking input
numbers = list(map(int, input("Enter space-separated numbers: ").split()))

# Printing result
result = unique_elements(numbers)
print("Unique elements are:", *result)

# output
# Enter space-separated numbers: 1 2 2 3 4 4 5
# Unique elements are: 1 2 3 4 5