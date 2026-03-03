# Program using defaultdict

from collections import defaultdict

d = defaultdict(int)

text = input("Enter a string: ")

for char in text:
    d[char] += 1

print("Character Frequency:", dict(d))

# Output:
# Enter a string: hello
# Character Frequency: {'h':1, 'e':1, 'l':2, 'o':1}