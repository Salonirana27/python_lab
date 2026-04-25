# Program to append data into existing file

filename = input("Enter file name: ")

with open(filename, "a") as file:
    data = input("Enter text to append: ")
    file.write("\n" + data)

print("Data appended successfully.")

# Output:
# Enter file name: sample.txt
# Enter text to append: Welcome MCA
# Data appended successfully.