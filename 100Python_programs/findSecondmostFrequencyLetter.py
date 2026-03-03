# Program to find second most frequent character

string = input("Enter a string: ")
freq = {}

for ch in string:
    if ch != " ":
        freq[ch] = freq.get(ch, 0) + 1

values = sorted(freq.values(), reverse=True)

if len(values) > 1:
    second_freq = values[1]
    for key in freq:
        if freq[key] == second_freq:
            print("Second most frequent character:", key)
            break
else:
    print("Not enough characters")

# Output:
# Enter a string: aabbccc
# Second most frequent character: a