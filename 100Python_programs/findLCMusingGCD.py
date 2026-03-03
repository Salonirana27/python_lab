# Program to find LCM using GCD

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

x, y = a, b

while y != 0:
    x, y = y, x % y

gcd = x
lcm = (a * b) // gcd

print("LCM is:", lcm)

# Output:
# Enter first number: 4
# Enter second number: 6
# LCM is: 12