# Perform difference of two sets.


def difference_sets(set1, set2):
    return set1.difference(set2)

# Taking input
set1 = set(map(int, input("Enter first set elements: ").split()))
set2 = set(map(int, input("Enter second set elements: ").split()))

# Performing difference (set1 - set2)
result = difference_sets(set1, set2)

# Printing result
print("Difference of sets is:", *sorted(result))

# output
# Enter first set elements: 1 2 3 4
# Enter second set elements: 3 4 5 6
# Difference of sets is: 1 2