# -----------------------------------------------------------
# Problem 2: Count frequency of each character using dictionary
# -----------------------------------------------------------

def char_frequency(s):
    freq = {}  # Empty dictionary to store frequency

    # Loop through each character in string
    for ch in s:
        # Increase count if exists, else initialize to 1
        freq[ch] = freq.get(ch, 0) + 1

    return freq


# Input from user
s = input("Enter a string: ")

# Display result
print("Character Frequency:", char_frequency(s))

# Output:
# Enter a string: hello
# Character Frequency: {'h': 1, 'e': 1, 'l': 2, 'o': 1}