# Program to count word frequency

sentence = input("Enter a sentence: ")
words = sentence.split()

frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

print("Word Frequency:", frequency)

# Output:
# Enter a sentence: apple mango apple
# Word Frequency: {'apple':2, 'mango':1}