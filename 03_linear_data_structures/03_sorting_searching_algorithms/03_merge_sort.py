print("--- Merge Sort ---\n")

# left:  [1, 3, 7]    right: [2, 5, 9]    result: []
#         ↑                   ↑
#         compare 1 vs 2 → take 1

# left:  [1, 3, 7]    right: [2, 5, 9]    result: [1]
#            ↑                ↑
#            compare 3 vs 2 → take 2

# left:  [1, 3, 7]    right: [2, 5, 9]    result: [1, 2]
#            ↑                   ↑
#            compare 3 vs 5 → take 3

# left:  [1, 3, 7]    right: [2, 5, 9]    result: [1, 2, 3]
#               ↑                ↑
#               compare 7 vs 5 → take 5

# left:  [1, 3, 7]    right: [2, 5, 9]    result: [1, 2, 3, 5]
#               ↑                   ↑
#               compare 7 vs 9 → take 7

# left:  []           right: [9]          result: [1, 2, 3, 5, 7]
# left exhausted → append remaining right

# result: [1, 2, 3, 5, 7, 9]


def merge(left, right):
    result = []
    i = j = 0
    # compare front of each half, take the smaller
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])  # append any remaining elements
    result.extend(right[j:])
    return result


def merge_sort(arr):
    if len(arr) <= 1:
        return arr  # base case
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])  # sort left half
    right = merge_sort(arr[mid:])  # sort right half
    return merge(left, right)  # merge sorted halves


numbers = [38, 27, 43, 3, 9, 82, 10]
print("original:", numbers)
print("sorted:", merge_sort(numbers))
