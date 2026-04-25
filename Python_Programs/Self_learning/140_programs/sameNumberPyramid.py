# Program to print number pyramid (same number per row)

n = int(input("Enter number of rows: "))

for i in range(1, n + 1):
    print(" " * (n - i), end="")
    for j in range(i):
        print(i, end=" ")
    print()

# Output:
# Enter number of rows: 4
#    1
#   2 2
#  3 3 3
# 4 4 4 4