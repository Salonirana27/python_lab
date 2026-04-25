# Program to handle division by zero exception

try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
    result = a / b
    print("Result:", result)

except ZeroDivisionError:
    print("Error: Division by zero is not allowed")

except ValueError:
    print("Error: Invalid input")

# Output:
# Enter numerator: 10
# Enter denominator: 0
# Error: Division by zero is not allowed