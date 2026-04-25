# Program to replace vowels with *

text = input("Enter a string: ")
result = ""

for ch in text:
    if ch in "aeiouAEIOU":
        result = result + "*"
    else:
        result = result + ch

print("Updated string:", result)

#Output
#Enter a string: education
#Updated string: *d*c*t**n