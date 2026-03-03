# Program to print reverse continuous number triangle

n = int(input("Enter number of rows: "))
num = n * (n + 1) // 2   # total numbers in triangle

for i in range(n, 0, -1):
    for j in range(i):
        print(num, end=" ")
        num -= 1
    print()

# Output:
# Enter number of rows: 3
# 6 5 4
# 3 2
# 1