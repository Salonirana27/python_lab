# Program to count substring occurrences manually

string = input("Enter main string: ")
substring = input("Enter substring: ")

count = 0

for i in range(len(string) - len(substring) + 1):
    if string[i:i+len(substring)] == substring:
        count += 1

print("Occurrences:", count)

# Output:
# Enter main string: banana
# Enter substring: ana
# Occurrences: 2