#  Count character frequency using dictionary.


def count_char_frequency(text):
    freq = {}
    for ch in text:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1
    return freq

# Taking input
text = input("Enter a string: ")

# Counting frequency
result = count_char_frequency(text)

# Printing result
for key in result:
    print(key, ":", result[key])

#output
# Enter a string: hello
# h : 1
# e : 1
# l : 2
# o : 1