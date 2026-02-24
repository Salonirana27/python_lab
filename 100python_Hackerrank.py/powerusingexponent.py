#calculate power without using exponent operator
# Read input
base = int(input("enter base: "))
exp = int(input("enter exponent: "))

result = 1

for i in range(exp):
    result *= base

print("result is :",result)

#output
"""enter base: 3
enter exponent: 7
result is : 2187"""