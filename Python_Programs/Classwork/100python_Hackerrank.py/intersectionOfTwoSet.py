# Perform intersection of two sets.


def intersection_sets(set1, set2):
    return set1.intersection(set2)

# Taking input
set1 = set(map(int, input("Enter first set elements: ").split()))
set2 = set(map(int, input("Enter second set elements: ").split()))

# Performing intersection
result = intersection_sets(set1, set2)

# Printing result
print("Intersection of sets is:", *sorted(result))

# output
# Enter first set elements: 1 2 3 4
# Enter second set elements: 3 4 5 6
# Intersection of sets is: 3 4