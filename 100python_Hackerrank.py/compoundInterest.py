#calculate compound interest 
# Read inputs
P = float(input("Enter principal: "))
R = float(input("Enter RAte  of interest: "))
T = float(input("Enter Time: "))

# Calculate final amount
A = P * (1 + R/100) ** T

# Calculate compound interest
CI = A - P

# Print result
print("The compund interest is : " ,CI)

#output
"""Enter principal: 1000
Enter RAte  of interest: 4
Enter Time: 3
The compund interest is :  124.86400000000003"""