# Program to find sum of diagonal elements

n = int(input("Enter order of square matrix: "))
matrix = []

print("Enter matrix elements row-wise:")
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

diagonal_sum = 0

for i in range(n):
    diagonal_sum += matrix[i][i]

print("Sum of diagonal elements:", diagonal_sum)

# Output:
# Enter order of square matrix: 2
# 1 2
# 3 4
# Sum of diagonal elements: 5