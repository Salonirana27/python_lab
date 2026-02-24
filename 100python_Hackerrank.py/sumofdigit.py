#Find the sum of digits of a number

num = int(input("enter the number: "))

# Make number positive (in case of negative input)
num = abs(num)

sum_digits = 0

# Loop until number becomes 0
while num > 0:
    digit = num % 10      # Get last digit
    sum_digits += digit   # Add digit to sum
    num //= 10            # Remove last digit

# Print result
print("the sum of all digit is :" ,sum_digits)

#output
"""enter the number: 2345
the sum of all digit is : 14"""