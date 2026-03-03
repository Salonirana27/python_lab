# Program to print increasing number square

n = int(input("Enter size: "))

for i in range(n):
    for j in range(n):
        print(i + j + 1, end=" ")
    print()

# Output:
# Enter size: 3
# 1 2 3
# 2 3 4
# 3 4 5