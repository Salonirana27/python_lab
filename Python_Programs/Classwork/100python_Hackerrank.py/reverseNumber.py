#reverse number using while loop
num = int(input("Enter the value: "))

sign = -1 if num < 0 else 1
num = abs(num)

reverse = 0

while num > 0:
    reverse = reverse * 10 + (num % 10)
    num //= 10

print("the factorial is :",sign * reverse)

#output
"""Enter  the value: 1234
the factorial is : 4321 """