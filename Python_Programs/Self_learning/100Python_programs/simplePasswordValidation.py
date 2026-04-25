# Program to validate password
# Conditions:
# At least 8 characters
# At least 1 uppercase, 1 lowercase, 1 digit

password = input("Enter password: ")

if (len(password) >= 8 and
    any(ch.isupper() for ch in password) and
    any(ch.islower() for ch in password) and
    any(ch.isdigit() for ch in password)):
    print("Valid Password")
else:
    print("Invalid Password")

# Output:
# Enter password: Saloni123
# Valid Password