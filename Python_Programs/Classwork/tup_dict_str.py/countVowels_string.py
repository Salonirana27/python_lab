# count vowels in a string
s = "education"
vowels = "aeiou"
count = 0

for ch in s:
    if ch in vowels:
        count += 1

print("Number of vowels:", count)


#output
"""Number of vowels: 5"""