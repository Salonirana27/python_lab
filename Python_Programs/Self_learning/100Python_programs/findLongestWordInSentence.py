# Program to find longest word

sentence = input("Enter a sentence: ")
words = sentence.split()

longest = max(words, key=len)

print("Longest word:", longest)

# Output:
# Enter a sentence: Python programming language
# Longest word: programming