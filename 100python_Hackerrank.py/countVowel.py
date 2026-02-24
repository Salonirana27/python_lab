#count vowels in a string 
# Read input
text = input("enter value: ")

count = 0
vowels = "aeiouAEIOU"

# Count vowels
for ch in text:
    if ch in vowels:
        count += 1

# Print result
print(count)

#output
"""enter value: saloni
3"""