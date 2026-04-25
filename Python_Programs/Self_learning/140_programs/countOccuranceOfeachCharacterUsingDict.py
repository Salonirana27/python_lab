# Program to count character frequency using dictionary

text = input("Enter a string: ")

freq = {}

for char in text:
    freq[char] = freq.get(char, 0) + 1

print("Character Frequency:", freq)

#  Output:
# Enter a string: hello
# Character Frequency: {'h': 1, 'e': 1, 'l': 2, 'o': 1}