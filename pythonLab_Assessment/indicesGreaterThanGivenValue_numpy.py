# Problem 18: Find indices of elements greater than given value

import numpy as np

# Input
arr = np.array(list(map(int, input("Enter elements: ").split())))
value = int(input("Enter value: "))

# Find indices
indices = np.where(arr > value)

# display  Output
print("Indices:", indices)

# Output:
# Enter elements: 1 5 8 2 10
# Enter value: 5
# Indices: (array([2, 4]),)