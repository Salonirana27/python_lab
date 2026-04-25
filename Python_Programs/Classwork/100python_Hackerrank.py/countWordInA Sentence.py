# Program to count words in a sentence

sentence = input("Enter a sentence: ")

words = sentence.split()
count = 0

for word in words:
    count = count + 1

print("Total words =", count)
#Output
#Enter a sentence: I love python programming
#Total words = 4