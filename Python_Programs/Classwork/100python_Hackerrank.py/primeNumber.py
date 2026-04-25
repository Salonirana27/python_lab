#print all prime number between  1 to N
n = int(input("enter the number: "))

for num in range(2, n + 1):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)
        
        #output
        """enter the number: 21
2
3
5
7
11
13
17
19"""