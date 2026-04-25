# Program to search a word in file

filename = input("Enter file name: ")
word = input("Enter word to search: ")

with open(filename, "r") as file:
    content = file.read()

if word in content:
    print("Word found in file.")
else:
    print("Word not found in file.")

# Output:
# Enter file name: sample.txt
# Enter word to search: Python
# Word found in file.