#find factorial using for loop 
# Read input
n = int(input("enter the value: "))

fact = 1

# Calculate factorial
for i in range(1, n + 1):
    fact *= i

# Print result
print(fact)

#output
"""enter the value: 5
120"""