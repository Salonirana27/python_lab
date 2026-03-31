# Problem 16: Normalize values between 0 and 1

import numpy as np

# Input
arr = np.array(list(map(int, input("Enter elements: ").split())))

# Normalization formula
normalized = (arr - np.min(arr)) / (np.max(arr) - np.min(arr))

#  display Output
print("Normalized Array:", normalized)

# Output:
# Enter elements: 10 20 30
# Normalized Array: [0.  0.5 1. ]