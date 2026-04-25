# Program demonstrating custom exception

class NegativeNumberError(Exception):
    pass

try:
    num = int(input("Enter a positive number: "))
    
    if num < 0:
        raise NegativeNumberError("Negative number entered")
    
    print("You entered:", num)

except NegativeNumberError as e:
    print("Custom Exception:", e)

# Output:
# Enter a positive number: -5
# Custom Exception: Negative number entered