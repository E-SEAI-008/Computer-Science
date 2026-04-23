print("--- Radix Sort ---\n")

"""
How it works:
- Sort digit by digit, from least significant (ones) to most significant (hundreds)
- Uses stable Counting Sort at each digit pass
- After all passes, the array is fully sorted
- Only works with non-negative integers (in this standard implementation)
- No comparisons — uses digit position as bucket index
"""

"""
Complexity
| Case    | Time     | Space    |
|---------|----------|----------|
| Best    | O(n × d) | O(n + k) |
| Average | O(n × d) | O(n + k) |
| Worst   | O(n × d) | O(n + k) |

n = number of elements, d = number of digits in max value, k = base (10)

All cases identical: always processes every digit of every element
Best when d is small — e.g. sorting phone numbers (all same length) or zip codes
Worst when d is large relative to n — e.g. sorting 5 numbers where one has 20 digits
"""


"""
digit = (num // exp) % 10  — extracts one digit at a time:
  170 // 1   = 170 → 170 % 10 = 0   (ones digit)
  170 // 10  = 17  →  17 % 10 = 7   (tens digit)
  170 // 100 = 1   →   1 % 10 = 1   (hundreds digit)
"""

unsorted_arr = [170, 45, 75, 90, 802, 24, 2, 66]
print("original:", unsorted_arr)  # original: [170, 45, 75, 90, 802, 24, 2, 66]


def radix_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10  # 10 buckets for digits 0-9

    # count occurrences of each digit at position exp
    for num in arr:
        digit = (num // exp) % 10  # extract the digit at this position
        count[digit] += 1

    # cumulative sum — needed for stable placement
    for i in range(1, 10):
        count[i] += count[i - 1]

    # place elements backwards for stability
    for num in reversed(arr):
        digit = (num // exp) % 10
        count[digit] -= 1
        output[count[digit]] = num

    return output


max_val = max(unsorted_arr)
exp = 1  # start with ones digit

arr = unsorted_arr.copy()

while max_val // exp > 0:
    arr = radix_sort(arr, exp)
    print(f"after pass (exp={exp}):", arr)
    exp *= 10  # move to next digit position

print("sorted:", arr)  # sorted: [1, 2, 2, 3, 3, 4, 8]


"""
original:           [170, 45, 75, 90, 802, 24, 2, 66]
after pass (exp=1): [170, 90, 802, 2, 24, 45, 75, 66]   ← sorted by ones digit
after pass (exp=10):[802, 2, 24, 45, 66, 170, 75, 90]   ← sorted by tens digit
after pass (exp=100):[2, 24, 45, 66, 75, 90, 170, 802]  ← sorted by hundreds digit

sorted: [2, 24, 45, 66, 75, 90, 170, 802]
"""
