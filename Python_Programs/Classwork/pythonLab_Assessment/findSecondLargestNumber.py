
# -----------------------------------------------------------
# Problem 1: Find the second largest element (without using sort)
# -----------------------------------------------------------

def second_largest(lst):
    # Check if list has at least two elements
    if len(lst) < 2:
        return "List must have at least 2 elements"

    # Initialize largest and second largest with very small values
    largest = second = float('-inf')

    # Traverse each element in the list
    for num in lst:
        if num > largest:
            # Update both largest and second largest
            second = largest
            largest = num
        elif num > second and num != largest:
            # Update only second largest
            second = num

    # If second largest not found
    if second == float('-inf'):
        return "No second largest element"

    return second


# Taking input from user (space-separated integers)
lst = list(map(int, input("Enter numbers: ").split()))

# Display result
print("Second Largest:", second_largest(lst))

# Output:
# Enter numbers: 10 20 4 45 99
# Second Largest: 45