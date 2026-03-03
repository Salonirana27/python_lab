# Program to sort list based on length of strings

lst = input("Enter words: ").split()

lst.sort(key=len)

print("Sorted by Length:", lst)

# Output:
# Enter words: python is very powerful
# Sorted by Length: ['is', 'very', 'python', 'powerful']