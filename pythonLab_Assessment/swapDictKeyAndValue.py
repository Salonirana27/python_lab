# -----------------------------------------------------------
# Problem 8: Swap keys and values in a dictionary
# -----------------------------------------------------------

def swap_dict(d):
    swapped = {}

    # Swap key and value
    for key, value in d.items():
        swapped[value] = key

    return swapped


# Input
n = int(input("Enter number of pairs: "))
d = {}

for i in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    d[key] = value

# display Output
print("Swapped Dictionary:", swap_dict(d))

# Output:
# Enter number of pairs: 2
# Enter key: a
# Enter value: 1
# Enter key: b
# Enter value: 2
# Swapped Dictionary: {'1': 'a', '2': 'b'}