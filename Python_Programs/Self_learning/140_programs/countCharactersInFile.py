# Program to count total characters in file

filename = input("Enter file name: ")

with open(filename, "r") as file:
    content = file.read()

print("Total characters in file:", len(content))

# Output:
# Enter file name: sample.txt
# Total characters in file: 24