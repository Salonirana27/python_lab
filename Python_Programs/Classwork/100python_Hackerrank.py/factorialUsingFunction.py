#calculate factorial using function
# Function to calculate factorial
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

# Read input
num = int(input("Enter number: "))

# Print result
print(factorial(num))

#output
"""Enter number: 6
720"""