# Program to read pickle data

import pickle

with open("data.pkl", "rb") as file:
    data = pickle.load(file)

print("Loaded Data:", data)

# Output:
# Loaded Data: Hello Python