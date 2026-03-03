# Program to display file with line numbers

filename = input("Enter file name: ")

with open(filename, "r") as file:
    lines = file.readlines()

for i in range(len(lines)):
    print(f"{i+1}: {lines[i]}", end="")

# Output:
# Enter file name: sample.txt
# 1: Hello Python
# 2: Welcome MCA