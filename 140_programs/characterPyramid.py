# Program to print character pyramid

n = int(input("Enter number of rows: "))

for i in range(n):
    print(" " * (n - i - 1), end="")
    for j in range(2 * i + 1):
        print(chr(65 + i), end="")
    print()

#  Output:
# Enter number of rows: 3
#   A
#  BBB
# CCCCC