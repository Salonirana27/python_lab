# Program to write data into CSV file

import csv

filename = input("Enter CSV file name: ")

with open(filename, "w", newline="") as file:
    writer = csv.writer(file)

    name = input("Enter name: ")
    marks = input("Enter marks: ")

    writer.writerow(["Name", "Marks"])
    writer.writerow([name, marks])

print("Data written to CSV successfully.")

# Example Output:
# Enter CSV file name: data.csv
# Enter name: Saloni
# Enter marks: 90
# Data written to CSV successfully.