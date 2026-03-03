# Program to print descending number triangle

n = int(input("Enter number of rows: "))

for i in range(n, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()

# Output:
# Enter number of rows: 4
# 4 3 2 1
# 3 2 1
# 2 1
# 1