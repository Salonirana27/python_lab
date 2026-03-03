# Program to find transpose of matrix

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix = []

print("Enter matrix elements row-wise:")
for i in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)

transpose = []

for j in range(cols):
    new_row = []
    for i in range(rows):
        new_row.append(matrix[i][j])
    transpose.append(new_row)

print("Transpose Matrix:")
for row in transpose:
    print(row)

# Output:
# 1 2
# 3 4
# Transpose:
# [1, 3]
# [2, 4]