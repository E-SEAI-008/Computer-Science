print("--- Radix Sort ---\n")

arr = [170, 45, 75, 90, 802, 24, 2, 66]


def counting_sort_by_digit(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10  # 10 buckets for digits 0-9

    # count occurrences of each digit at position exp
    for num in arr:
        digit = (num // exp) % 10
        count[digit] += 1
        print(f"  {num} → digit: {digit}")

    print("  count:", count)

    # cumulative sum for stable placement
    for i in range(1, 10):
        count[i] += count[i - 1]

    # place elements backwards for stability
    for num in reversed(arr):
        digit = (num // exp) % 10
        count[digit] -= 1
        output[count[digit]] = num

    return output


max_val = max(arr)
exp = 1  # start with ones digit

print("original:", arr)

while max_val // exp > 0:
    print(f"\n--- sorting by digit position {exp} ---")
    arr = counting_sort_by_digit(arr, exp)
    print("after pass:", arr)
    exp *= 10  # move to next digit (tens, hundreds...)

print("\nsorted:", arr)


# original: [170, 45, 75, 90, 802, 24, 2, 66]

# --- sorting by digit position 1 (ones) ---
#   170 → digit: 0
#   45  → digit: 5
#   75  → digit: 5
#   90  → digit: 0
#   802 → digit: 2
#   24  → digit: 4
#   2   → digit: 2
#   66  → digit: 6
# after pass: [170, 90, 802, 2, 24, 45, 75, 66]

# --- sorting by digit position 10 (tens) ---
# after pass: [802, 2, 24, 45, 66, 170, 75, 90]

# --- sorting by digit position 100 (hundreds) ---
# after pass: [2, 24, 45, 66, 75, 90, 170, 802]

# sorted: [2, 24, 45, 66, 75, 90, 170, 802]
