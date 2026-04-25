# Program to count lines, words and characters in file

filename = input("Enter filename: ")

with open(filename, "r") as file:
    content = file.read()

lines = content.split("\n")
words = content.split()

print("Lines:", len(lines))
print("Words:", len(words))
print("Characters:", len(content))

# Output:
# Enter filename: data.txt
# Lines: 2
# Words: 5
# Characters: 25