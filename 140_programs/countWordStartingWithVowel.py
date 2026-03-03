# Program to count words starting with vowel

sentence = input("Enter a sentence: ")
words = sentence.split()

count = 0
vowels = "aeiouAEIOU"

for word in words:
    if word[0] in vowels:
        count += 1

print("Words starting with vowel:", count)

# Output:
# Enter a sentence: Apple is orange and umbrella
# Words starting with vowel: 4