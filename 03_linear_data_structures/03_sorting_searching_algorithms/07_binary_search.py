print("--- Binary Search ---\n")


def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


# Example usage
sorted_numbers = [1, 3, 5, 7, 9, 11, 13, 15]
index = binary_search(sorted_numbers, 20)

if index != -1:
    print(f"Found number at index {index}")
else:
    print("Number not found")


print("--- Comparing Search Algorithms ---\n")
