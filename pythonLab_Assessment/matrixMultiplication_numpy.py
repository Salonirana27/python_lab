# Problem 17: Perform matrix multiplication

import numpy as np

# Input for first matrix
r1 = int(input("Enter rows of first matrix: "))
c1 = int(input("Enter columns of first matrix: "))

matrix1 = []
for i in range(r1):
    row = list(map(int, input().split()))
    matrix1.append(row)

# Input for second matrix
r2 = int(input("Enter rows of second matrix: "))
c2 = int(input("Enter columns of second matrix: "))

matrix2 = []
for i in range(r2):
    row = list(map(int, input().split()))
    matrix2.append(row)

arr1 = np.array(matrix1)
arr2 = np.array(matrix2)

# Matrix multiplication
result = np.dot(arr1, arr2)

#  display Output
print("Result Matrix:\n", result)

# Output:
# Enter rows of first matrix: 2
# Enter columns of first matrix: 2
# 1 2
# 3 4
# Enter rows of second matrix: 2
# Enter columns of second matrix: 2
# 5 6
# 7 8
# Result Matrix:
# [[19 22]
#  [43 50]]