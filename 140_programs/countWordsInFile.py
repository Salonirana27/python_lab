# Program to count total words in file

filename = input("Enter file name: ")

with open(filename, "r") as file:
    content = file.read()
    words = content.split()

print("Total words in file:", len(words))

# Output:
# Enter file name: sample.txt
# Total words in file: 3