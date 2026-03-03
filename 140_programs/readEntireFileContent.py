# Program to read entire file content

filename = input("Enter file name to read: ")

with open(filename, "r") as file:
    content = file.read()

print("File Content:")
print(content)

#  Output:
# Enter file name to read: sample.txt
# File Content:
# Hello Python