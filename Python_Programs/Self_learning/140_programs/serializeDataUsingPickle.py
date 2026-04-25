# Program to save data using pickle

import pickle

data = input("Enter some text to store: ")

with open("data.pkl", "wb") as file:
    pickle.dump(data, file)

print("Data stored using pickle.")

# Output:
# Enter some text to store: Hello Python
# Data stored using pickle.