import csv

with open("data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Marks"])
    writer.writerow(["Saloni", "85"])

print("data.csv file created successfully.")

#to read CSV file

import csv

file = open("data.csv", "r")
reader = csv.reader(file)

print("CSV File Content-------:")
for row in reader:
    print(row)

file.close()

# Output:
#data.csv file created successfully.
#CSV File Content-------:
#['Name', 'Marks']
#['Saloni', '85']