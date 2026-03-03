# Program to print binary pattern

n = int(input("Enter number of rows: "))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print((i + j) % 2, end=" ")
    print()

# Output:
# Enter number of rows: 4
# 0
# 1 0
# 0 1 0
# 1 0 1 0