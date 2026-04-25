# Program to count special characters in a string

string = input("Enter a string: ")

special_count = 0

for ch in string:
    if not ch.isalnum() and not ch.isspace():
        special_count += 1

print("Number of special characters:", special_count)

# Output:
# Enter a string: Hello@123!
# Number of special characters: 2