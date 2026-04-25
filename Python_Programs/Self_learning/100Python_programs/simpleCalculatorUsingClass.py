# Simple calculator using class

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Division by zero not allowed"
        return a / b

calc = Calculator()

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Addition:", calc.add(a, b))
print("Subtraction:", calc.subtract(a, b))
print("Multiplication:", calc.multiply(a, b))
print("Division:", calc.divide(a, b))

# Output:
# Enter first number: 10
# Enter second number: 5
# Addition: 15
# Subtraction: 5
# Multiplication: 50
# Division: 2.0