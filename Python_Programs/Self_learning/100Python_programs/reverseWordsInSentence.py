# Program to reverse each word in sentence

sentence = input("Enter a sentence: ")
words = sentence.split()

reversed_words = [word[::-1] for word in words]

print("Modified sentence:", " ".join(reversed_words))

# Output:
# Enter a sentence: Hello World
# Modified sentence: olleH dlroW