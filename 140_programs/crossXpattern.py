# Program to print X pattern

n = int(input("Enter size (odd number preferred): "))

for i in range(n):
    for j in range(n):
        if i == j or i + j == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

#  Output:
# Enter size: 5
# *       *
#   *   *
#     *
#   *   *
# *       *