# Program to count number of lines in file

file = open("sample.txt", "r")
lines = file.readlines()
file.close()

print("Number of lines:", len(lines))

# Output:
# Number of lines: 2