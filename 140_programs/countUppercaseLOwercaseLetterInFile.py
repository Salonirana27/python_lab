# Program to count uppercase and lowercase letters in a file

filename = input("Enter file name: ")

with open(filename, "r") as file:
    content = file.read()

upper = 0
lower = 0

for char in content:
    if char.isupper():
        upper += 1
    elif char.islower():
        lower += 1

print("Uppercase letters:", upper)
print("Lowercase letters:", lower)

# Output:
# Enter file name: sample.txt
# Uppercase letters: 2
# Lowercase letters: 15