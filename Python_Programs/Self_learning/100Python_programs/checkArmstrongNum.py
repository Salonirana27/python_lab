# Program to check Armstrong number (any length)

num = int(input("Enter a number: "))
original = num
digits = len(str(num))
sum_power = 0

while num > 0:
    digit = num % 10
    sum_power += digit ** digits
    num //= 10

if sum_power == original:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")

#Output:
# Enter a number: 153
# Armstrong Number