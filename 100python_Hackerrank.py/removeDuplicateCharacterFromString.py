# Program to remove duplicate characters from string

text = input("Enter a string: ")
result = ""

for ch in text:
    if ch not in result:
        result = result + ch

print("String after removing duplicates:", result)

#Output
#Enter a string: programming
#String after removing duplicates: progamin