#find the greatest of four numbers
a = float(input("enter number1: "))
b = float(input("enter number2: "))
c = float(input("enter number3: "))
d = float(input("enter number4: "))

greatest = a

if b > greatest:
    greatest = b
if c > greatest:
    greatest = c
if d > greatest:
    greatest = d

print("the highest number is :" ,greatest)

#output
"""enter number1: 3
enter number2: 7
enter number3: 9
enter number4: 2
the highest number is : 9.0"""