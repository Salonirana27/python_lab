# Program to remove duplicate words

sentence = input("Enter a sentence: ")
words = sentence.split()

unique_words = []

for word in words:
    if word not in unique_words:
        unique_words.append(word)

print("Sentence after removing duplicates:", " ".join(unique_words))

# Output:
# Enter a sentence: hello world hello python
# Sentence after removing duplicates: hello world python