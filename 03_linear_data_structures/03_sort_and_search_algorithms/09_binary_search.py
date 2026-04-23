print("--- Binary Search ---\n")

"""
How it works:
- Compare the target to the middle element
- If target is smaller → discard the right half, search left
- If target is larger → discard the left half, search right
- Repeat until found or search space is empty
- Requires a sorted array
"""

"""
Complexity
| Case    | Time     | Space |
|---------|----------|-------|
| Best    | O(1)     | O(1)  |
| Average | O(log n) | O(1)  |
| Worst   | O(log n) | O(1)  |

Best case: target is the middle element on the first check
Worst case: target is not in the array — search space halves until empty
Each step eliminates half the remaining elements → log n steps maximum
"""


def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2  # check the middle index
        if arr[mid] == target:
            return mid  # found — return index
        elif arr[mid] < target:
            left = mid + 1  # target is in the right half
        else:
            right = mid - 1  # target is in the left half
    return -1  # not found


sorted_numbers = [1, 3, 5, 7, 9, 11, 13, 15]

index = binary_search(sorted_numbers, 11)
if index != -1:
    print("found number at index:", index)
else:
    print("result:", "number not found")

index = binary_search(sorted_numbers, 20)
if index != -1:
    print("found number at index:", index)
else:
    print("result:", "number not found")
