# Program to read data from a file

file = open("sample.txt", "r")
content = file.read()
file.close()

print("File Content:")
print(content)

# Output:
# File Content:
# Hello Python