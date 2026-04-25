# Program to remove blank lines from file

filename = input("Enter file name: ")

with open(filename, "r") as file:
    lines = file.readlines()

with open("updated_" + filename, "w") as file:
    for line in lines:
        if line.strip() != "":
            file.write(line)

print("Blank lines removed. New file created.")

# Output:
# Enter file name: sample.txt
# Blank lines removed. New file created.