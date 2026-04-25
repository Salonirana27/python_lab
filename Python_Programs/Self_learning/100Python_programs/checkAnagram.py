# Program to check anagram without using sorted()

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

if len(str1) != len(str2):
    print("Not Anagrams")
else:
    freq = {}
    
    for ch in str1:
        freq[ch] = freq.get(ch, 0) + 1
    
    for ch in str2:
        if ch in freq:
            freq[ch] -= 1
        else:
            print("Not Anagrams")
            break
    else:
        if all(value == 0 for value in freq.values()):
            print("Anagrams")
        else:
            print("Not Anagrams")

# Output:
# Enter first string: listen
# Enter second string: silent
# Anagrams