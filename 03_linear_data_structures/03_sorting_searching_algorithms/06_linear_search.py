print("--- Linear Search ---\n")


def linear_search(arr, target):
    for i, value in enumerate(arr):
        if value == target:
            return i
    return -1


numbers = [4, 2, 7, 1, 8]
index = linear_search(numbers, 7)

if index != -1:
    print(f"Found number at index {index}")
else:
    print("Number not found")
