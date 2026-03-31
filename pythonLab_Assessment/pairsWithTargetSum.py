# -----------------------------------------------------------
# Problem 9: Find all pairs whose sum equals target
# -----------------------------------------------------------

def find_pairs(lst, target):
    pairs = []
    seen = []

    # Traverse list
    for num in lst:
        complement = target - num

        # If complement already seen, pair exists
        if complement in seen:
            pairs.append((complement, num))

        seen.append(num)

    return pairs


# Input
lst = list(map(int, input("Enter list: ").split()))
target = int(input("Enter target: "))

# display  Output
print("Pairs:", find_pairs(lst, target))

# Output:
# Enter list: 1 2 3 4 5
# Enter target: 5
# Pairs: [(2, 3), (1, 4)]