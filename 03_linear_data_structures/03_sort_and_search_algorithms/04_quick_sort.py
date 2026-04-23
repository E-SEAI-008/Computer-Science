print("--- Quick Sort ---\n")

"""
How it works:
- Pick a pivot (in our example using a random element), partition everything smaller to the left and larger to the right
- The pivot is now in its final sorted position
- Recursively sort the left and right portions in place
- No extra arrays created — elements are swapped within the original array
"""

"""
Complexity
| Case              | Time       | Space    |
|-------------------|------------|----------|
| Best              | O(n log n) | O(log n) |
| Average           | O(n log n) | O(log n) |
| Worst (bad pivot) | O(n²)      | O(n)     |

Best/Average case: pivot splits the array into roughly equal halves — log n levels of recursion, n work per level
Worst case: pivot is always the smallest or largest element — one side is empty every time, giving n levels instead of log n
Space is the recursion call stack — log n deep normally, n deep in worst case
"""


import random

unsorted_arr = [10, 7, 8, 9, 1, 5]
print("original:", unsorted_arr)  # original: [10, 7, 8, 9, 1, 5]


def partition(arr, left, right):
    pivot_index = random.randint(left, right)  # pick random pivot
    arr[pivot_index], arr[right] = arr[right], arr[pivot_index]  # swap to end
    pivot_value = arr[right]
    i = left - 1  # i tracks the boundary of the "smaller" region

    for j in range(left, right):
        if arr[j] <= pivot_value:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # swap smaller element into left region

    arr[i + 1], arr[right] = arr[right], arr[i + 1]  # place pivot in final position
    return i + 1  # return pivot's final index


def quick_sort(arr, left, right):
    if left < right:  # base case — single element or empty, nothing to sort
        pivot_index = partition(arr, left, right)  # partition and get pivot position
        quick_sort(arr, left, pivot_index - 1)  # sort left of pivot
        quick_sort(arr, pivot_index + 1, right)  # sort right of pivot
    return arr


sorted_arr = quick_sort(unsorted_arr.copy(), 0, len(unsorted_arr) - 1)
print("sorted:", sorted_arr)  # [1, 5, 7, 8, 9, 10]
