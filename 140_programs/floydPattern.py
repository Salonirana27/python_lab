# Program to print Floyd's triangle

n = int(input("Enter number of rows: "))
num = 1

for i in range(1, n + 1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()

#  Output:
# Enter number of rows: 4
# 1
# 2 3
# 4 5 6
# 7 8 9 10