# Program to find longest word in file

filename = input("Enter file name: ")

with open(filename, "r") as file:
    words = file.read().split()

longest = max(words, key=len)

print("Longest word:", longest)

# Output:
# Enter file name: sample.txt
# Longest word: Welcome