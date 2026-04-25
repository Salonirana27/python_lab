# Problem 12: Perform element-wise multiplication

import numpy as np

# Input
arr1 = np.array(list(map(int, input("Enter first array: ").split())))
arr2 = np.array(list(map(int, input("Enter second array: ").split())))

# Multiplication
result = arr1 * arr2

#display Output
print("Result:", result)

# Output:
# Enter first array: 1 2 3
# Enter second array: 4 5 6
# Result: [ 4 10 18]