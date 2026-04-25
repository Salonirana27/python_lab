# Program to merge two files safely

import os

file1 = input("Enter first file name: ")
file2 = input("Enter second file name: ")
output = input("Enter output file name: ")

# Check if both files exist
if os.path.exists(file1) and os.path.exists(file2):

    with open(file1, "r") as f1:
        content1 = f1.read()

    with open(file2, "r") as f2:
        content2 = f2.read()

    with open(output, "w") as f3:
        f3.write(content1 + "\n" + content2)

    print("Files merged successfully.")

else:
    print("One or both files do not exist.")

# Example Output:
# Enter first file name: file1.txt
# Enter second file name: file2.txt
# Enter output file name: merged.txt
# One or both files do not exist.