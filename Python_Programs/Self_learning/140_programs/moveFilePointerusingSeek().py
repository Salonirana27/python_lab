# Program demonstrating seek() method

filename = input("Enter file name: ")

with open(filename, "r") as file:
    file.seek(3)
    content = file.read()
    print("Content after moving pointer:", content)

# Output:
# Enter file name: sample.txt
# Content after moving pointer: lo Java Welcome MCA