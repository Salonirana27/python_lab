# Program to print square number pattern

n = int(input("Enter size: "))

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(j, end=" ")
    print()

# Output:
# Enter size: 3
# 1 2 3
# 1 2 3
# 1 2 3