# Program to print reverse alphabet pyramid

n = int(input("Enter number of rows: "))

for i in range(n, 0, -1):
    print(" " * (n - i), end="")
    for j in range(i):
        print(chr(65 + j), end=" ")
    print()

# Output:
# Enter number of rows: 3
# A B C
#  A B
#   A