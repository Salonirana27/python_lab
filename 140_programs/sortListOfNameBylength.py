# Program to sort dictionary by keys

data = {"b": 2, "a": 1, "c": 3}

sorted_dict = dict(sorted(data.items()))

print("Sorted Dictionary by Keys:", sorted_dict)

# Output:
# Sorted Dictionary by Keys: {'a': 1, 'b': 2, 'c': 3}