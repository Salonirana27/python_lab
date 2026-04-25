# Program to read data from CSV file

import csv

filename = input("Enter CSV file name: ")

with open(filename, "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)

# Output:
# Enter CSV file name: data.csv
# ['Name', 'Marks']
# ['Saloni', '90']