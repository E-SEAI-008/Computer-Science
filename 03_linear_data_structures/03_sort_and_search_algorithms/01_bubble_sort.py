print("--- Bubble Sort ---\n")

"""
How it works:
- Compare adjacent elements, swap if out of order
- Each full pass moves the largest unsorted element to its final position
- The sorted portion grows from the right — so the inner loop shrinks each pass
- Early exit: if no swaps happened in a pass, the array is already sorted → O(n) best case
"""

"""
Complexity
| Case    | Time | Space |
|---------|------|-------|
| Best    | O(n) | O(1)  |
| Average | O(n²)| O(1)  |
| Worst   | O(n²)| O(1)  |

Best case: array is already sorted — early exit triggers after one pass with no swaps
Worst case: array is reverse sorted — every element needs to bubble all the way to the end
"""


unsorted_arr = [5, 1, 4, 2, 8]
print("original:", unsorted_arr)  # original: [5, 1, 4, 2, 8]


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # print(f"      pass {i + 1}: {arr}") # print for visualization of each step
        if not swapped:  # no swaps this pass — already sorted, stop early
            break
    return arr


sorted_arr = bubble_sort(unsorted_arr.copy())
print("sorted:", sorted_arr)  # sorted: [1, 2, 4, 5, 8]
