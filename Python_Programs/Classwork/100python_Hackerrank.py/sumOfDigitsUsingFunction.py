#sum of digits using function
# Function to find sum of digits
def sum_of_digits(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

# Read input
num = int(input("enter digit: "))

# Print result
print(sum_of_digits(num))

#output
"""enter digit: 3456789
42"""