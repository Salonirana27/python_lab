# Program to toggle case without using swapcase()

string = input("Enter a string: ")
result = ""

for ch in string:
    if ch.isupper():
        result += ch.lower()
    elif ch.islower():
        result += ch.upper()
    else:
        result += ch

print("Toggled String:", result)

# Output:
# Enter a string: PyThOn
# Toggled String: pYtHoN