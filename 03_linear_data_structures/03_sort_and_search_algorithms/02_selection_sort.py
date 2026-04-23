print("--- Selection Sort ---\n")

"""
How it works:
- Find the minimum element in the unsorted portion, swap it to the front
- Each pass places one element in its final position (the minimum)
- The sorted portion grows from the left
- No early exit — always scans the full unsorted portion regardless of input
"""

"""
Complexity
| Case    | Time | Space |
|---------|------|-------|
| Best    | O(n²)| O(1)  |
| Average | O(n²)| O(1)  |
| Worst   | O(n²)| O(1)  |

Best case: still O(n²) — no early exit, always scans the full unsorted portion
Worst case: same — performance never changes regardless of input order
"""


unsorted_arr = [5, 1, 4, 2, 8]
print("original:", unsorted_arr)  # original: [5, 1, 4, 2, 8]


def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i  # assume current position is the minimum
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j  # found a smaller element
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
        # print(f"      pass {i + 1}: {arr}")  # print for visualization of each step
    return arr


sorted_arr = selection_sort(unsorted_arr.copy())
print("sorted:", sorted_arr)  # sorted: [1, 2, 4, 5, 8]
