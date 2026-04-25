# Program to remove a specific word from file

filename = input("Enter file name: ")
word = input("Enter word to remove: ")

with open(filename, "r") as file:
    content = file.read()

words = content.split()
words = [w for w in words if w != word]

with open(filename, "w") as file:
    file.write(" ".join(words))

print("Word removed successfully.")

#  Output:
# Enter file name: sample.txt
# Enter word to remove: Python
# Word removed successfully.