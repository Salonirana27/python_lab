# Problem 13: Transpose a 2D matrix

import numpy as np

# Input
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix = []
for i in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)

arr = np.array(matrix)

# Transpose
transpose = arr.T

#  display Output
print("Transposed Matrix:\n", transpose)

# Output:
# Enter number of rows: 2
# Enter number of columns: 3
# 1 2 3
# 4 5 6
# Transposed Matrix:
# [[1 4]
#  [2 5]
#  [3 6]]