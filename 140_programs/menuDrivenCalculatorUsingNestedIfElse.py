# Program for simple calculator using nested if

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter choice: "))
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if choice == 1:
    result = a + b
else:
    if choice == 2:
        result = a - b
    else:
        if choice == 3:
            result = a * b
        else:
            if choice == 4:
                if b != 0:
                    result = a / b
                else:
                    result = "Division by zero not allowed"
            else:
                result = "Invalid Choice"

print("Result:", result)

#  Output:
# Enter choice: 1
# Enter first number: 5
# Enter second number: 3
# Result: 8