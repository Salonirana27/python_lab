#sum of even number upto n
n = int(input("enter number: "))

total = 0
i = 2

while i <= n:
    total += i
    i += 2

print("total even numbers are:" ,total)

#output
"""enter number: 30
total even numbers are: 240"""