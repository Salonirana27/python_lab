# Program to check if string is pangram

import string

sentence = input("Enter a sentence: ").lower()

alphabet = set(string.ascii_lowercase)

if alphabet.issubset(set(sentence)):
    print("Pangram")
else:
    print("Not a Pangram")

# Output:
# Enter a sentence: The quick brown fox jumps over the lazy dog
# Pangram