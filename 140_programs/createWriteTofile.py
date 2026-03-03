# Program to create a file and write data into it

filename = input("Enter file name to create: ")

with open(filename, "w") as file:
    data = input("Enter text to write into file: ")
    file.write(data)

print("Data written successfully.")

# Output:
# Enter file name to create: sample.txt
# Enter text to write into file: Hello Python
# Data written successfully.