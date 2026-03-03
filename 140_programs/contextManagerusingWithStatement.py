# Program demonstrating context manager

filename = input("Enter file name: ")

with open(filename, "w") as file:
    file.write("This file is handled using context manager.")

print("File written successfully using with statement.")

# Output:
# Enter file name: test.txt
# File written successfully using with statement.