#check frequency of elements in list
lst = [1, 2, 2, 3, 3, 3]
freq = {}

for i in lst:
    freq[i] = freq.get(i, 0) + 1

print("Frequency Dictionary:", freq)


#output
"""Frequency Dictionary: {1: 1, 2: 2, 3: 3}"""