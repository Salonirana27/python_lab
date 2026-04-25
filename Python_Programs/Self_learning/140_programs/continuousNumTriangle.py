# Program to print continuous numbers in triangle

n = int(input("Enter number of rows: "))
num = 1

for i in range(1, n + 1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()

# Output:
# Enter number of rows: 3
# 1
# 2 3
# 4 5 6