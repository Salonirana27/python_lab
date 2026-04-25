# Program to print zig-zag pattern

n = int(input("Enter number of rows: "))

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if j == i or j == n - i + 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# Output:
# Enter number of rows: 5
# *       *
#   *   *
#     *
#   *   *
# *       *