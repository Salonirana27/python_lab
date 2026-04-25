# Program to sort dictionary by keys

dictionary = eval(input("Enter dictionary: "))

sorted_dict = dict(sorted(dictionary.items()))

print("Sorted Dictionary by Keys:", sorted_dict)

# Output:
# Enter dictionary: {'b':2,'a':1,'c':3}
# Sorted Dictionary by Keys: {'a':1,'b':2,'c':3}