# Program to check if character is vowel, consonant, digit or special character

char = input("Enter a character: ")

if char.isalpha():
    if char.lower() in "aeiou":
        print("Vowel")
    else:
        print("Consonant")
else:
    if char.isdigit():
        print("Digit")
    else:
        print("Special Character")

#  Output:
# Enter a character: a
# Vowel