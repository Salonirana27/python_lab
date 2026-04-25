# Program to count digits in a file

filename = input("Enter file name: ")

with open(filename, "r") as file:
    content = file.read()

digit_count = 0

for char in content:
    if char.isdigit():
        digit_count += 1

print("Total digits in file:", digit_count)

#  Output:
# Enter file name: sample.txt
# Total digits in file: 5