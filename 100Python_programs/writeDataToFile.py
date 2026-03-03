# Program to write data into a file

data = input("Enter text to write in file: ")

file = open("sample.txt", "w")
file.write(data)
file.close()

print("Data written successfully")

# Output:
# Enter text to write in file: Hello Python
# Data written successfully