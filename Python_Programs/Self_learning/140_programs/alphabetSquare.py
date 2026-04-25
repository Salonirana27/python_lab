# Program to print alphabet square

n = int(input("Enter size: "))

for i in range(n):
    for j in range(n):
        print(chr(65 + i), end=" ")
    print()

# Output:
# Enter size: 3
# A A A
# B B B
# C C C