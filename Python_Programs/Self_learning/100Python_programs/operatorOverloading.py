# Program demonstrating operator overloading

class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Number(self.value + other.value)

    def display(self):
        print("Value:", self.value)

a = Number(int(input("Enter first number: ")))
b = Number(int(input("Enter second number: ")))

result = a + b
result.display()

# Output:
# Enter first number: 5
# Enter second number: 7
# Value: 12