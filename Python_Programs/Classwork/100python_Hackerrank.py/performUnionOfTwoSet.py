# Perform union of two sets.


def union_sets(set1, set2):
    return set1 | set2

# Taking input
set1 = set(map(int, input("Enter first set elements: ").split()))
set2 = set(map(int, input("Enter second set elements: ").split()))

# Performing union
result = union_sets(set1, set2)

# Printing result
print("Union of sets is:", *result)

#output
# Enter first set elements: 1 2 3 4
# Enter second set elements: 3 4 5 6
# Union of sets is: 1 2 3 4 5 6