# Program to check whether key exists in dictionary

data = {"name": "Aman", "age": 20}

key = input("Enter key to check: ")

if key in data:
    print("Key exists")
else:
    print("Key does not exist")
#Output:
#Enter key to check: age
#Key exists