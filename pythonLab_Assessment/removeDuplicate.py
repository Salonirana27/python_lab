# -----------------------------------------------------------
# Problem 7: Remove duplicates while keeping original order
# -----------------------------------------------------------

def remove_duplicates(lst):
    result = []

    # Traverse list and add only unique elements
    for item in lst:
        if item not in result:
            result.append(item)

    return result


# Input
lst = list(map(int, input("Enter list: ").split()))

#  display Output
print("List without duplicates:", remove_duplicates(lst))

# Output:
# Enter list: 1 2 2 3 4 3
# List without duplicates: [1, 2, 3, 4]