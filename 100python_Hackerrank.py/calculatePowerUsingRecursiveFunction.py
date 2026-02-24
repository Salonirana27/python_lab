#  Calculate power using recursive function.


def power(base, exp):
    if exp == 0:
        return 1
    else:
        return base * power(base, exp - 1)

# Taking input
base = int(input("Enter base: "))
exp = int(input("Enter exponent: "))

# Printing result
print("Result is:", power(base, exp))

# output
""" Enter base: 2
 Enter exponent: 5
 Result is: 32"""