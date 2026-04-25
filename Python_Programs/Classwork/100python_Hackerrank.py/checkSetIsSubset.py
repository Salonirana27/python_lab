# Check whether one set is subset of another.


def is_subset(set1, set2):
    return set1.issubset(set2)

# Taking input
set1 = set(map(int, input("Enter first set elements: ").split()))
set2 = set(map(int, input("Enter second set elements: ").split()))

# Checking subset
if is_subset(set1, set2):
    print("First set is a subset of second set")
else:
    print("First set is not a subset of second set")

# output
# Enter first set elements: 1 2
# Enter second set elements: 1 2 3 4
# First set is a subset of second set