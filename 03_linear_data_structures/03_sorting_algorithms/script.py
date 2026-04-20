print("--- Recursion ---\n")

# A function that calls itself with a smaller version of the problem, until it reaches a base case that stops the chain.


def countdown(n):
    if n == 0:
        return
    print(n)
    countdown(n - 1)


# countdown(3)

# What is a Call Stack?

# A call stack is a mechanism for an interpreter to keep track of its place in a script that calls multiple functions — what function is currently being run and what functions are called from within that function, etc. - MDN

# - Stores function calls, local variables, return addresses
# - Managed automatically, memory is freed when a function returns
# - Limited size (~1–8 MB depending on OS)
# - Stack overflow = you exceeded this limit


# countdown(3)
#   └── countdown(2)
#         └── countdown(1)
#               └── countdown(0)  ← base case, returns
#               ← returns
#         ← returns
#   ← returns


print("\n--- Quick Sort ---\n")


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

print("\n--- Merge Sort ---\n")

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
