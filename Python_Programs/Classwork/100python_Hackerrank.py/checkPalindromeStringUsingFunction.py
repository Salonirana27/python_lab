#check palindrome string using function
# Function to check palindrome
def is_palindrome(text):
    return text == text[::-1]

# Read input
text = input("enter string: ")

# Print result
if is_palindrome(text):
    print("Palindrome")
else:
    print("Not Palindrome")
    
    #output
    """enter string: saloni
Not Palindrome

enter string: naman
Palindrome

"""