# Problem 11: Find mean, median, and standard deviation

import numpy as np

# Input
arr = np.array(list(map(int, input("Enter elements: ").split())))

# Calculations
mean_val = np.mean(arr)
median_val = np.median(arr)
std_val = np.std(arr)

# Output
print("Mean:", mean_val)
print("Median:", median_val)
print("Standard Deviation:", std_val)

# Output:
# Enter elements: 1 2 3 4 5
# Mean: 3.0
# Median: 3.0
# Standard Deviation: 1.4142135623730951