# Program using Counter

from collections import Counter

text = input("Enter a string: ")

count = Counter(text)

print("Character Count:", count)

# Output:
# Enter a string: banana
# Character Count: Counter({'a':3, 'n':2, 'b':1})