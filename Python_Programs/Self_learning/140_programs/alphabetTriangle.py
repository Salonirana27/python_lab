# Program to print alphabet triangle

n = int(input("Enter number of rows: "))

for i in range(n):
    for j in range(i + 1):
        print(chr(65 + j), end=" ")
    print()

#  Output:
# Enter number of rows: 3
# A
# A B
# A B C