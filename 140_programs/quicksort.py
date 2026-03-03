# Program to sort list using Quick Sort

def quick_sort(lst):
    if len(lst) <= 1:
        return lst
    pivot = lst[0]
    smaller = [x for x in lst[1:] if x <= pivot]
    greater = [x for x in lst[1:] if x > pivot]
    return quick_sort(smaller) + [pivot] + quick_sort(greater)

lst = list(map(int, input("Enter elements: ").split()))

sorted_list = quick_sort(lst)

print("Sorted List:", sorted_list)

# Output:
# Enter elements: 5 2 9 1
# Sorted List: [1, 2, 5, 9]