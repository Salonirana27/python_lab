# Program demonstrating file pointer using tell()

filename = input("Enter file name: ")

with open(filename, "r") as file:
    file.read(5)
    position = file.tell()
    print("Current File Pointer Position:", position)

# Output:
# Enter file name: sample.txt
# Current File Pointer Position: 5