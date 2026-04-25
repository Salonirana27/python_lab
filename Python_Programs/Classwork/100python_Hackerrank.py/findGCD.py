#find GCD using while loop
a = int(input("Enter number: "))
b = int(input("enter number: "))

a = abs(a)
b = abs(b)

while b != 0:
    temp = b
    b = a % b
    a = temp

print("GCD is :" ,a)

#output
"""Enter number: 12
enter number: 18
GCD is : 6 """