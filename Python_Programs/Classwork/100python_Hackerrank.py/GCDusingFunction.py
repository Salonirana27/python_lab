#Find GCD using function.

def find_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Taking input
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Printing result
print("GCD is:", find_gcd(a, b))

# output
# Enter first number: 12
# Enter second number: 18
# GCD is: 6