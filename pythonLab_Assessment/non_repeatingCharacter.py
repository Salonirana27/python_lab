# -----------------------------------------------------------
# Problem 6: Find first non-repeating character
# -----------------------------------------------------------

def first_non_repeating(s):
    freq = {}

    # Count frequency of characters
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    # Find first character with frequency 1
    for ch in s:
        if freq[ch] == 1:
            return ch

    return "No non-repeating character"


# Input
s = input("Enter string: ")

# display Output
print("First Non-Repeating Character:", first_non_repeating(s))

# Output:
# Enter string: aabbcde
# First Non-Repeating Character: c