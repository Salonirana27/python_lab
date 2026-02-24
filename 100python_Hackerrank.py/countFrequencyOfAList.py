# Count frequency of elements in list.


def count_frequency(lst):
    freq = {}
    for num in lst:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    return freq

# Taking input
numbers = list(map(int, input("Enter space-separated numbers: ").split()))

# Printing result
frequency = count_frequency(numbers)
for key in frequency:
    print(key, ":", frequency[key])

#output
"""Enter space-separated numbers: 1 2 2 3 3 3 4
1 : 1
2 : 2
3 : 3
4 : 1"""