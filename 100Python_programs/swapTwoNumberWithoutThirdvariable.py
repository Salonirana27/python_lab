# Program to swap two numbers without third variable

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

a, b = b, a

print("After Swapping:")
print("a =", a)
print("b =", b)

# Output:
# Enter first number: 5
# Enter second number: 10
# After Swapping:
# a = 10
# b = 5