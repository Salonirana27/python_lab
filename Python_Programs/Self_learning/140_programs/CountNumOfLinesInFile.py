# Program to count number of lines in a file

filename = input("Enter file name: ")

with open(filename, "r") as file:
    lines = file.readlines()

print("Total number of lines:", len(lines))

# Output:
# Enter file name: sample.txt
# Total number of lines: 2