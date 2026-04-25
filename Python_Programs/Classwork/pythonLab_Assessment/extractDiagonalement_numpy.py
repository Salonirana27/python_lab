# Problem 15: Extract diagonal elements

import numpy as np

# Input
n = int(input("Enter size of square matrix: "))

matrix = []
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

arr = np.array(matrix)

# Extract diagonal
diag = np.diag(arr)

#  display Output
print("Diagonal Elements:", diag)

# Output:
# Enter size of square matrix: 3
# 1 2 3
# 4 5 6
# 7 8 9
# Diagonal Elements: [1 5 9]