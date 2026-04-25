#Check whether tuple elements are unique.


def are_unique(tpl):
    for i in range(len(tpl)):
        for j in range(i + 1, len(tpl)):
            if tpl[i] == tpl[j]:
                return False
    return True

# Taking input
numbers = tuple(map(int, input("Enter tuple elements: ").split()))

# Printing result
if are_unique(numbers):
    print("All elements are unique")
else:
    print("Elements are not unique")

# output
# Enter tuple elements: 1 2 3 4 5
# All elements are unique