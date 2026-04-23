print("--- Counting Sort ---\n")

"""
How it works:
- Count how many times each value appears (no comparisons needed)
- Reconstruct the sorted array directly from the counts
- Works with non-negative and negative integers within a known range
- Two versions: simple (fast to understand) and stable (needed for Radix Sort)
"""

"""
Complexity
| Case    | Time     | Space    |
|---------|----------|----------|
| Best    | O(n + k) | O(n + k) |
| Average | O(n + k) | O(n + k) |
| Worst   | O(n + k) | O(n + k) |

n = number of elements, k = range of values (max - min)

All cases identical: always counts every element and iterates the full range
Best when k is small relative to n — e.g. sorting 10,000 exam scores with range 0-100
Worst when k is large relative to n — e.g. [1, 2, 1000000] creates a million-slot count array for 3 values
"""


# ─────────────────────────────────────────
# Simple version (no stability guarantee)
# ─────────────────────────────────────────

unsorted_arr = [4, 2, 2, 8, 3, 3, 1]
print("original:", unsorted_arr)  # original: [4, 2, 2, 8, 3, 3, 1]


def counting_sort_simple(arr):
    # Step 1: find max AND min to determine the true range (k)
    max_val = max(arr)
    min_val = min(arr)
    k = max_val - min_val + 1  # This is the true 'k'

    # Step 2: create count array exactly the size of the range
    count = [0] * k

    # Step 3: count each value (subtract min_val to shift the index)
    for num in arr:
        count[num - min_val] += 1

    """
    index(i)  freq    [i + min_val] * freq     meaning
    0         1       [1]                      value 1 appeared 1 time
    1         2       [2, 2]                   value 2 appeared 2 times
    2         2       [3, 3]                   value 3 appeared 2 times
    3         1       [4]                      value 4 appeared 1 time
    4-6       0       []                       values 5-7 appeared 0 times
    7         1       [8]                      value 8 appeared 1 time
    """
    result = []

    # Step 4: reconstruct — add min_val back to 'i' to restore the original number
    for i, freq in enumerate(count):
        result.extend([i + min_val] * freq)

    return result


sorted_arr = counting_sort_simple(unsorted_arr.copy())
print("sorted:", sorted_arr)  # sorted: [1, 2, 2, 3, 3, 4, 8]

# ─────────────────────────────────────────
# Stable version (required for Radix Sort)
# ─────────────────────────────────────────

unsorted_arr = [4, 2, 2, 8, 3, 3, 1]
print("\noriginal:", unsorted_arr)  # original: [4, 2, 2, 8, 3, 3, 1]


def counting_sort_stable(arr):

    # Step 1: find max AND min to determine the true range (k)
    max_val = max(arr)
    min_val = min(arr)
    k = max_val - min_val + 1  # This is the true 'k'

    # Step 2: create count array exactly the size of the range
    count = [0] * k

    # Step 3: count each value (subtract min_val to shift the index)
    for num in arr:
        count[num - min_val] += 1
    # print("done count:", count)  # [0, 1, 2, 2, 1, 0, 0, 0, 1]

    # Step 4: cumulative sum — each position now holds the last index for that value
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    # print("cumulative:", count)  # [0, 1, 3, 5, 6, 6, 6, 6, 7]

    # Step 5: place elements into result, iterate backwards for stability
    result = [0] * len(arr)

    for num in reversed(arr):  # go backwards through input
        # Substep 1: apply the offset to find the right index in the count array
        count_index = num - min_val

        # Substep 2: decrement to get 0-based index
        count[count_index] -= 1

        # Substep 3: place at the correct position
        result[count[count_index]] = num

    return result


"""
Step 5: Trace using min_val offset (current - 1 = count_index):

current = 1  → count_idx=0 → cumulative[0]=1 (dec to 0) → result: [1, _, _, _, _, _, _]
current = 3  → count_idx=2 → cumulative[2]=5 (dec to 4) → result: [1, _, _, _, 3, _, _]
current = 3  → count_idx=2 → cumulative[2]=4 (dec to 3) → result: [1, _, _, 3, 3, _, _]
current = 8  → count_idx=7 → cumulative[7]=7 (dec to 6) → result: [1, _, _, 3, 3, _, 8]
current = 2  → count_idx=1 → cumulative[1]=3 (dec to 2) → result: [1, _, 2, 3, 3, _, 8]
current = 2  → count_idx=1 → cumulative[1]=2 (dec to 1) → result: [1, 2, 2, 3, 3, _, 8]
current = 4  → count_idx=3 → cumulative[3]=6 (dec to 5) → result: [1, 2, 2, 3, 3, 4, 8]
"""

sorted_arr = counting_sort_stable(unsorted_arr.copy())
print("sorted:", sorted_arr)  # sorted: [1, 2, 2, 3, 3, 4, 8]
