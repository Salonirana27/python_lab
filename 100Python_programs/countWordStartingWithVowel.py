# Program to count words starting with vowel

sentence = input("Enter a sentence: ")
words = sentence.split()

count = 0

for word in words:
    if word[0].lower() in "aeiou":
        count += 1

print("Words starting with vowel:", count)

# Output:
# Enter a sentence: Apple is orange umbrella
# Words starting with vowel: 4