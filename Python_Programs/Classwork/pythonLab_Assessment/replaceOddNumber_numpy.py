# Problem 14: Replace all odd numbers with -1

import numpy as np

# Input
arr = np.array(list(map(int, input("Enter elements: ").split())))

# Replace odd numbers
arr[arr % 2 != 0] = -1

#  display Output
print("Modified Array:", arr)

# Output:
# Enter elements: 1 2 3 4 5
# Modified Array: [-1  2 -1  4 -1]