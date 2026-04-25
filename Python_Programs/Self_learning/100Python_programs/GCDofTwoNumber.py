# Program to find GCD using Euclidean Algorithm

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

while b != 0:
    a, b = b, a % b

print("GCD is:", a)

# Output:
# Enter first number: 48
# Enter second number: 18
# GCD is: 6