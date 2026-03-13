
# Create a NumPy array from 1 to 25 and reshape it into 5×5 matrix.
# Extract the middle 3×3 sub-matrix.

import numpy as np

arr = np.arange(1,26).reshape(5,5)

print("Original Matrix:")
print(arr)

sub_matrix = arr[1:4,1:4]

print("Middle 3x3 Matrix:")
print(sub_matrix)

#output
#Original Matrix:
#[[ 1  2  3  4  5]
# [ 6  7  8  9 10]
# [11 12 13 14 15]
# [16 17 18 19 20]
# [21 22 23 24 25]]
#Middle 3x3 Matrix:
#[[ 7  8  9]
# [12 13 14]
# [17 18 19]]