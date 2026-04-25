#  Reverse a given number
num = int(input("Enter the number to be reverse: "))

# Store sign for negative numbers
sign = -1 if num < 0 else 1
num = abs(num)

reverse = 0

# Reverse the number
while num > 0:
    reverse = reverse * 10 + (num % 10)
    num //= 10

# Apply original sign
print("the reverse number is :" ,sign * reverse)

#output
"""Enter the number to be reverse: 1234
the reverse number is : 4321"""