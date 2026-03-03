# Program to append data to file

data = input("Enter text to append: ")

file = open("sample.txt", "a")
file.write("\n" + data)
file.close()

print("Data appended successfully")

# Output:
# Enter text to append: MCA Student
# Data appended successfully