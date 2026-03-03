# Program using reduce to find product of list elements

from functools import reduce

numbers = list(map(int, input("Enter numbers: ").split()))

product = reduce(lambda x, y: x * y, numbers)

print("Product of elements:", product)

#  Output:
# Enter numbers: 2 3 4
# Product of elements: 24