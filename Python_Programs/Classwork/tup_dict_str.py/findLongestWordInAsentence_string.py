#find longest word in a sentence 
s = "Python programming is interesting"

words = s.split()
longest = max(words, key=len)

print("Longest word:", longest)


#output
"""Longest word: programming"""
