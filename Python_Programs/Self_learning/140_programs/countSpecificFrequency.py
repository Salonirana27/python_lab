# Program to count frequency of specific word in file

filename = input("Enter file name: ")
word = input("Enter word to count: ")

with open(filename, "r") as file:
    words = file.read().split()

count = words.count(word)

print("Frequency of word:", count)

# Output:
# Enter file name: sample.txt
# Enter word to count: Python
# Frequency of word: 2