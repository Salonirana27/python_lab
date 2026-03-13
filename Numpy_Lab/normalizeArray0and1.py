
# Generate a NumPy array of 10 random numbers between 0 and 1
# and normalize the array between 0 and 1.

import numpy as np

arr = np.random.rand(10)

normalized = (arr - arr.min()) / (arr.max() - arr.min())

print("Original Array:")
print(arr)

print("Normalized Array:")
print(normalized)

#output
#Original Array:
#[0.54 0.21 0.87 0.12 0.63 0.44 0.78 0.33 0.95 0.67]

#Normalized Array:
#[0.50 0.11 0.89 0.00 0.61 0.38 0.78 0.25 1.00 0.66]