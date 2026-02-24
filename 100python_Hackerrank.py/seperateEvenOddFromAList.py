# Problem Statement: Separate even and odd numbers from list.

def separate_even_odd(lst):
    even = []
    odd = []
    for num in lst:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
    return even, odd

numbers = list(map(int, input().split()))

even, odd = separate_even_odd(numbers)

print("Even numbers:", *even)
print("Odd numbers:", *odd)

 #output
""" 1 2 3 4 5 6
 Even numbers: 2 4 6
 Odd numbers: 1 3 5 """