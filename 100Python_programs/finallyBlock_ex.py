# Program demonstrating finally block

try:
    num = int(input("Enter a number: "))
    print("Square:", num * num)

except ValueError:
    print("Invalid input")

finally:
    print("Program execution completed")

# Output:
# Enter a number: 5
# Square: 25
# Program execution completed