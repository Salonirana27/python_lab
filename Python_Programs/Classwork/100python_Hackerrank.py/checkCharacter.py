#Check whether a character is vowel or consonant
ch = input("Enter character: " ,).strip()

if len(ch) == 1 and ch.isalpha():
    if ch.lower() in 'aeiou':
        print("Character is Vowel")
    else:
        print("Character is Consonant")
else:
    print("Invalid Input")
    
    #output
    """Enter character: b
Character is Consonant

 Enter character: a
Character is Vowel 
 
Enter character: 2
Invalid Input
"""