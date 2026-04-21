print("--- Quick Sort ---\n")

# This example does create new lists (for simplicity reasons) which usually isn't the case for Quick Sort because it is an in-place algorithm
# The example provided in the LMS stays true to that principle


def quick_sort(arr):
    if len(arr) <= 1:
        return arr  # base case — nothing to sort
    pivot = arr[-1]  # pick last element as pivot
    left = [x for x in arr[:-1] if x <= pivot]  # smaller or equal → left
    right = [x for x in arr[:-1] if x > pivot]  # larger → right
    return quick_sort(left) + [pivot] + quick_sort(right)


numbers = [10, 7, 8, 9, 1, 5]
print("original:", numbers)
print("sorted:", quick_sort(numbers))
