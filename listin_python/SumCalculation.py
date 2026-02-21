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

print(sum)