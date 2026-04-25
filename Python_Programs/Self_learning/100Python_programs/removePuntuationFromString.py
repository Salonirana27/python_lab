# Program to remove punctuation

import string

text = input("Enter text: ")

result = ""

for ch in text:
    if ch not in string.punctuation:
        result += ch

print("Text without punctuation:", result)

# Output:
# Enter text: Hello, World!
# Text without punctuation: Hello World