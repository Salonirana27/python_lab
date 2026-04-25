# Program to find most repeated character

string = input("Enter a string: ")
frequency = {}

for ch in string:
    if ch != " ":
        frequency[ch] = frequency.get(ch, 0) + 1

max_char = max(frequency, key=frequency.get)

print("Most repeated character:", max_char)
print("Frequency:", frequency[max_char])

# Output:
# Enter a string: programming
# Most repeated character: r
# Frequency: 2