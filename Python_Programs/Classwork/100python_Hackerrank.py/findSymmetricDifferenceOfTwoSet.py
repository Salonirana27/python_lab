# Find symmetric difference of two sets.


def symmetric_difference_sets(set1, set2):
    return set1.symmetric_difference(set2)

# Taking input
set1 = set(map(int, input("Enter first set elements: ").split()))
set2 = set(map(int, input("Enter second set elements: ").split()))

# Finding symmetric difference
result = symmetric_difference_sets(set1, set2)

# Printing result
print("Symmetric difference of sets is:", *sorted(result))

# output
# Enter first set elements: 1 2 3 4
# Enter second set elements: 3 4 5 6
# Symmetric difference of sets is: 1 2 5 6