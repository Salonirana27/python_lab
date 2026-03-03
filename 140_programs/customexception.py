# Program demonstrating custom exception

class NegativeNumberError(Exception):
    pass

num = int(input("Enter a positive number: "))

try:
    if num < 0:
        raise NegativeNumberError("Negative number not allowed")
    print("Valid number entered")

except NegativeNumberError as e:
    print("Error:", e)

# Output:
# Enter a positive number: -5
# Error: Negative number not allowed