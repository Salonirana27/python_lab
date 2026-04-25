# Program to copy content from one file to another

source = input("Enter source file name: ")
destination = input("Enter destination file name: ")

with open(source, "r") as file1:
    content = file1.read()

with open(destination, "w") as file2:
    file2.write(content)

print("File copied successfully.")

# Output:
# Enter source file name: sample.txt
# Enter destination file name: copy.txt
# File copied successfully.