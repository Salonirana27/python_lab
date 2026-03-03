# Program to convert decimal to binary manually

num = int(input("Enter a decimal number: "))
binary = ""

temp = num

while temp > 0:
    binary = str(temp % 2) + binary
    temp //= 2

print("Binary Equivalent:", binary)

#  Output:
# Enter a decimal number: 10
# Binary Equivalent: 1010