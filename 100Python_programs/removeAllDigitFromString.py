# Program to remove digits from string

string = input("Enter a string: ")
result = ""

for ch in string:
    if not ch.isdigit():
        result += ch

print("String after removing digits:", result)

#Output:
# Enter a string: abc123xyz
# String after removing digits: abcxyz