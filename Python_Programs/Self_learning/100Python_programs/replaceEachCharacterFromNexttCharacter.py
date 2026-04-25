# Program to replace each character with next ASCII character

string = input("Enter a string: ")
result = ""

for ch in string:
    result += chr(ord(ch) + 1)

print("Modified String:", result)

# Output:
# Enter a string: abc
# Modified String: bcd