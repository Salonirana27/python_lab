# -----------------------------------------------------------
# Problem 4: Check whether a number is Armstrong or not
# -----------------------------------------------------------

def is_armstrong(n):
    # Convert number to string to access digits
    num_str = str(n)
    power = len(num_str)  # Number of digits
    total = 0

    # Calculate sum of digits raised to power
    for digit in num_str:
        total += int(digit) ** power

    # Check if equal to original number
    return total == n


# Input
n = int(input("Enter number: "))

# Output
print("Is Armstrong:", is_armstrong(n))

# Output:
# Enter number: 153
# Is Armstrong: True