# Problem Statement: Count vowels using function.

def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for ch in text:
        if ch in vowels:
            count += 1
    return count

text = input("enter text: ")
print(count_vowels(text))

#output
"""enter text: hello
2"""