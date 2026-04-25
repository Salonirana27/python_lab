# -----------------------------------------------------------
# Problem 10: Flatten a nested list (using recursion)
# -----------------------------------------------------------

def flatten_list(nested):
    flat = []

    # Traverse each element
    for item in nested:
        if isinstance(item, list):
            # Recursively flatten sublist
            flat.extend(flatten_list(item))
        else:
            flat.append(item)

    return flat


# Input
nested = eval(input("Enter nested list: "))

#  display Output
print("Flattened List:", flatten_list(nested))

# Output:
# Enter nested list: [1, [2, 3], [4, [5, 6]]]
# Flattened List: [1, 2, 3, 4, 5, 6]