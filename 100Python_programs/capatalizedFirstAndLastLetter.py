# Program to capitalize first and last character

sentence = input("Enter a sentence: ")
words = sentence.split()
result = []

for word in words:
    if len(word) > 1:
        new_word = word[0].upper() + word[1:-1] + word[-1].upper()
    else:
        new_word = word.upper()
    result.append(new_word)

print("Modified Sentence:", " ".join(result))

# Output:
# Enter a sentence: hello world
# Modified Sentence: HellO WorlD