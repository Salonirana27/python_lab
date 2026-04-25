# -----------------------------------------------------------
# Problem 3: Find common elements between two lists (no set)
# -----------------------------------------------------------

def common_elements(lst1, lst2):
    result = []

    # Traverse first list
    for item in lst1:
        # Check if element is in second list and not already added
        if item in lst2 and item not in result:
            result.append(item)

    return result


# Input from user
lst1 = list(map(int, input("Enter first list: ").split()))
lst2 = list(map(int, input("Enter second list: ").split()))

# Display result
print("Common Elements:", common_elements(lst1, lst2))

# Output:
# Enter first list: 1 2 3 4
# Enter second list: 3 4 5 6
# Common Elements: [3, 4]