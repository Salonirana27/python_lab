#Accept numbers until 0 is entered and print sum
total = 0

while True:
    num = int(input("enter number: "))
    if num == 0:
        break
    total += num

print("the sum is :" ,total)

#output
"""enter number: 32
enter number: 45
enter number: 42
enter number: 87
enter number: 1
enter number: 0
the sum is : 207"""