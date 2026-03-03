# Program to count digits in a number

num = int(input("Enter a number: "))
count = 0

temp = abs(num)

while temp > 0:
    count += 1
    temp //= 10

print("Number of digits:", count)

# Output:
# Enter a number: 12345
# Number of digits: 5