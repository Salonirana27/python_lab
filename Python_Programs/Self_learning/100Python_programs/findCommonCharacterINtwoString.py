# Program to find common characters

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

common = set(str1) & set(str2)

print("Common characters:", common)

# Output:
# Enter first string: apple
# Enter second string: people
# Common characters: {'p', 'e', 'l'}