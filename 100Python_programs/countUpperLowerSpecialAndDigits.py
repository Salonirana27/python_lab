# Program to count uppercase, lowercase, digits and special characters

string = input("Enter a string: ")

upper = lower = digit = special = 0

for ch in string:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1
    elif ch.isdigit():
        digit += 1
    elif not ch.isspace():
        special += 1

print("Uppercase letters:", upper)
print("Lowercase letters:", lower)
print("Digits:", digit)
print("Special characters:", special)

# Output:
# Enter a string: Hello@123
# Uppercase letters: 1
# Lowercase letters: 4
# Digits: 3
# Special characters: 1