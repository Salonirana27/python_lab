# creating a blank list
numbers = []

# take number of elements
n = int(input("enter number of elements: "))

# input elements
for i in range(n):
    num = int(input("enter a number: "))
    numbers.append(num)

print("numbers are:", numbers)

# sum calculation
sum = 0
for num in numbers:
    sum += num

print("summ of numbers:",sum)

#output
"""enter number of elements: 4
enter a number: 3
enter a number: 5
enter a number: 7
enter a number: 9
numbers are: [3, 5, 7, 9]
summ of numbers: 24"""