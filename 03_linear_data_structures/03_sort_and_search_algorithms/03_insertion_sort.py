print("--- Insertion Sort ---\n")

"""
How it works:
- Build a sorted portion from left to right, one element at a time
- Pick the next unsorted element and shift larger elements right to make room
- Insert the element into its correct position in the sorted portion
- Best case O(n) — if already sorted, each element just stays in place
"""

"""
Complexity
| Case    | Time | Space |
|---------|------|-------|
| Best    | O(n) | O(1)  |
| Average | O(n²)| O(1)  |
| Worst   | O(n²)| O(1)  |

Best case: array is already sorted — each element is already in place, no shifts needed
Worst case: array is reverse sorted — every element must shift all the way to the front
"""


unsorted_arr = [5, 1, 4, 2, 8]
print("original:", unsorted_arr)  # original: [5, 1, 4, 2, 8]


def insertion_sort(arr):
    for i in range(1, len(arr)):
        current = arr[i]  # the element we're placing
        j = i - 1
        while j >= 0 and arr[j] > current:
            arr[j + 1] = arr[j]  # shift larger element one position right
            j -= 1
        arr[j + 1] = current  # drop into correct position
        # print(f"      pass {i}: {arr}")  # print for visualization of each step
    return arr


sorted_arr = insertion_sort(unsorted_arr.copy())
print("sorted:", sorted_arr)  # sorted: [1, 2, 4, 5, 8]
