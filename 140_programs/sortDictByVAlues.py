# Program to sort dictionary by values

dictionary = eval(input("Enter dictionary: "))

sorted_dict = dict(sorted(dictionary.items(), key=lambda item: item[1]))

print("Sorted Dictionary by Values:", sorted_dict)

#  Output:
# Enter dictionary: {'a':3,'b':1,'c':2}
# Sorted Dictionary by Values: {'b':1,'c':2,'a':3}