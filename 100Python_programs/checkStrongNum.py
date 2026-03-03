# Program to check whether a number is Strong Number

# Input from user
num = int(input("Enter a number: "))

# Store original number
original = num
sum_fact = 0

# Loop to calculate factorial of digits
while num > 0:
    digit = num % 10
    fact = 1
    
    # Finding factorial
    for i in range(1, digit + 1):
        fact *= i
        
    sum_fact += fact
    num //= 10

# Check condition
if sum_fact == original:
    print("Strong Number")
else:
    print("Not a Strong Number")

# Output:
# Enter a number: 145
# Strong Number