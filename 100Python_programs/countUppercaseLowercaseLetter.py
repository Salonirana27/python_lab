# Program to count uppercase and lowercase letters

text = input("Enter a string: ")

upper = lower = 0

for ch in text:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1

print("Uppercase letters:", upper)
print("Lowercase letters:", lower)

#  Output:
# Enter a string: PyThOn
# Uppercase letters: 3
# Lowercase letters: 3