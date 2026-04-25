# Create a 5×5 matrix with random integers between 1 and 100
# and find the minimum and maximum value.

import numpy as np

matrix = np.random.randint(1,101,(5,5))

print("Matrix:")
print(matrix)

print("Min =", np.min(matrix))
print("Max =", np.max(matrix))

#output
#Matrix:
#[[65 99 18 63 51]
# [64 48 17 52  7]
# [11 99 38 55 50]
# [80 44 32  7 42]
# [88 45 81 60 84]]
#Min = 7
#Max = 99