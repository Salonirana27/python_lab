#: Check whether a character is digit or alphabet

ch = input("Enter the digit or alphabet: ").strip()

if len(ch) == 1:
    if ch.isdigit():
        print("Digit")
    elif ch.isalpha():
        print("Alphabet")
    else:
        print("Invalid Input")
else:
    print("Invalid Input")
    
    #output
    """Enter the digit or alphabet: a
Alphabet

Enter the digit or alphabet: 4
Digit
"""