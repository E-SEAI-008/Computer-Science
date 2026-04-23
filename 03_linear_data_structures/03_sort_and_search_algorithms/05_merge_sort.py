print("--- Merge Sort ---\n")

"""
How it works:
- Split the array in half recursively until each piece has one element
- A single element is already sorted by definition (base case)
- Merge pairs of sorted halves back together by comparing front elements
- Work happens on the way back up — split blindly, merge smartly
"""

"""
Complexity
| Case    | Time       | Space |
|---------|------------|-------|
| Best    | O(n log n) | O(n)  |
| Average | O(n log n) | O(n)  |
| Worst   | O(n log n) | O(n)  |

All cases identical: always splits exactly in half regardless of input — no bad cases possible
Space O(n): extra arrays are created during the merge step to hold the two halves
"""


"""
Merge step visualized with [1, 3, 7] and [2, 5, 9]:

left:  [1, 3, 7]    right: [2, 5, 9]    result: []
        ↑                   ↑
        compare 1 vs 2 → take 1

left:  [1, 3, 7]    right: [2, 5, 9]    result: [1]
           ↑                ↑
           compare 3 vs 2 → take 2

left:  [1, 3, 7]    right: [2, 5, 9]    result: [1, 2]
           ↑                   ↑
           compare 3 vs 5 → take 3

left:  [1, 3, 7]    right: [2, 5, 9]    result: [1, 2, 3]
              ↑                ↑
              compare 7 vs 5 → take 5

left:  [1, 3, 7]    right: [2, 5, 9]    result: [1, 2, 3, 5]
              ↑                   ↑
              compare 7 vs 9 → take 7

left exhausted → append remaining right: [9]
result: [1, 2, 3, 5, 7, 9]
"""

unsorted_arr = [38, 27, 43, 3, 9, 82, 10]
print("original:", unsorted_arr)  # original: [38, 27, 43, 3, 9, 82, 10]


def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])  # append any remaining elements from left
    result.extend(right[j:])  # append any remaining elements from right
    return result


def merge_sort(arr):
    if len(arr) <= 1:
        return arr  # base case — single element is already sorted
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])  # sort left half recursively
    right = merge_sort(arr[mid:])  # sort right half recursively
    return merge(left, right)  # merge the two sorted halves


sorted_arr = merge_sort(unsorted_arr.copy())
print("sorted:", sorted_arr)  # sorted: [3, 9, 10, 27, 38, 43, 82]
