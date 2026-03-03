# Program to rename a file

import os

old_name = input("Enter existing file name: ")
new_name = input("Enter new file name: ")

os.rename(old_name, new_name)

print("File renamed successfully.")

#  Output:
# Enter existing file name: sample.txt
# Enter new file name: new.txt
# File renamed successfully.