print("--- Linear Search ---\n")

"""
How it works:
- Check each element one by one from left to right
- Return the index as soon as the target is found
- Return -1 if the target is not in the array
- Works on any data — sorted or unsorted
"""

"""
Complexity
| Case    | Time | Space |
|---------|------|-------|
| Best    | O(1) | O(1)  |
| Average | O(n) | O(1)  |
| Worst   | O(n) | O(1)  |

Best case: target is the first element
Worst case: target is the last element or not in the array at all
"""


def linear_search(arr, target):
    for i, value in enumerate(arr):
        if value == target:
            return i  # found — return index immediately
    return -1  # not found


numbers = [4, 2, 7, 1, 8]

index = linear_search(numbers, 7)
if index != -1:
    print("found number at index:", index)
else:
    print("result:", "number not found")

index = linear_search(numbers, 5)
if index != -1:
    print("found number at index:", index)
else:
    print("result:", "number not found")
