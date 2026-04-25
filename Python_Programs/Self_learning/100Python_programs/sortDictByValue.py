# Program to sort dictionary by value

dictionary = eval(input("Enter dictionary: "))

sorted_dict = dict(sorted(dictionary.items(), key=lambda item: item[1]))

print("Sorted Dictionary:", sorted_dict)

# Output:
# Enter dictionary: {'a':3,'b':1,'c':2}
# Sorted Dictionary: {'b':1,'c':2,'a':3}