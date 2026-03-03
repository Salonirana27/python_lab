# Program to copy file content

source = input("Enter source filename: ")
destination = input("Enter destination filename: ")

with open(source, "r") as s:
    content = s.read()

with open(destination, "w") as d:
    d.write(content)

print("File copied successfully")

# Output:
# Enter source filename: file1.txt
# Enter destination filename: file2.txt
# File copied successfully