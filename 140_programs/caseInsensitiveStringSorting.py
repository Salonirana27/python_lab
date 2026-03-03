# Program to sort words ignoring case sensitivity

words = input("Enter words: ").split()

sorted_words = sorted(words, key=str.lower)

print("Case-Insensitive Sorted List:", sorted_words)

# Output:
# Enter words: banana Apple mango
# Case-Insensitive Sorted List: ['Apple', 'banana', 'mango']