# Program to find largest word in a sentence

sentence = input("Enter a sentence: ")
words = sentence.split()

largest = max(words, key=len)

print("Largest word:", largest)

# Output:
# Enter a sentence: Python is very powerful language
# Largest word: powerful