# Program to find all factors of a number

num = int(input("Enter a number: "))

print("Factors are:")
for i in range(1, num + 1):
    if num % i == 0:
        print(i, end=" ")

# Output:
# Enter a number: 12
# Factors are:
# 1 2 3 4 6 12