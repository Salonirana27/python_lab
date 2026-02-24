# Program to find frequency of each character

text = input("Enter a string: ")
freq = {}

for ch in text:
    if ch in freq:
        freq[ch] = freq[ch] + 1
    else:
        freq[ch] = 1

for key in freq:
    print(key, "->", freq[key])
    
#Output
#Enter a string: apple
#a -> 1
#p -> 2
#l -> 1
#e -> 1