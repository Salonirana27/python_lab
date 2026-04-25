# Program to count vowels in file

filename = input("Enter file name: ")

with open(filename, "r") as file:
    content = file.read().lower()

vowels = "aeiou"
count = 0

for char in content:
    if char in vowels:
        count += 1

print("Total vowels in file:", count)

# Output:
# Enter file name: sample.txt
# Total vowels in file: 6