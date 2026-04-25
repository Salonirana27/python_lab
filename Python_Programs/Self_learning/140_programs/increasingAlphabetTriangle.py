# Program to print increasing alphabet triangle

n = int(input("Enter number of rows: "))

for i in range(1, n + 1):
    for j in range(i):
        print(chr(65 + i - 1), end=" ")
    print()

#  Output:
# Enter number of rows: 3
# A
# B B
# C C C