print("--- Counting Sort ---\n")

# ------------------ Simple version ------------------

arr = [4, 2, 2, 8, 3, 3, 1]

# Step 1: Find the max to know how big the count array needs to be
max_val = max(arr)  # 8
print("max value:", max_val)

# Step 2: Create count array with a slot for every value 0 to max
count = [0] * (max_val + 1)  # [0, 0, 0, 0, 0, 0, 0, 0, 0]
print("empty count:", count)

# Step 3: Count each value
for num in arr:
    count[num] += 1

print("count array:", count)  # [0, 1, 2, 2, 1, 0, 0, 0, 1]

# Step 4: Reconstruct: for each index, repeat that value by its count
result = []
for i, freq in enumerate(count):
    result.extend([i] * freq)

print("sorted:", result)  # [1, 2, 2, 3, 3, 4, 8]


# Step 4 in simple version (no stability)
# index(i)  freq    [i] * freq     meaning
# 0         0       []             value 0 appeared 0 times
# 1         1       [1]            value 1 appeared 1 time
# 2         2       [2, 2]         value 2 appeared 2 times
# 3         2       [3, 3]         value 3 appeared 2 times
# 4         1       [4]            value 4 appeared 1 time
# 5         0       []             value 5 appeared 0 times
# 6         0       []             value 6 appeared 0 times
# 7         0       []             value 7 appeared 0 times
# 8         1       [8]            value 8 appeared 1 time


# ------------------ Default version ------------------

arr = [4, 2, 2, 8, 3, 3, 1]

# Step 1: Find max
max_val = max(arr)  # 8

# Step 2: Create count list
count = [0] * (max_val + 1)

# Step 3: Count each value
for num in arr:
    count[num] += 1

print("count:", count)  # [0, 1, 2, 2, 1, 0, 0, 0, 1]

# Step 4: Cumulative sum, each position now holds the last index for that value
for i in range(1, len(count)):
    count[i] += count[i - 1]

print("cumulative:", count)  # [0, 1, 3, 5, 6, 6, 6, 6, 7]

# Step 5: Place elements into output, iterate backwards for stability
output = [0] * len(arr)

for num in reversed(arr):  # go backwards through input
    count[num] -= 1  # decrement first to get 0-based index
    output[count[num]] = num  # place at the correct position

print("sorted:", output)  # [1, 2, 2, 3, 3, 4, 8]

# Step 5 in default version (with stability)
# Step 1: current = 1 (last element)
#   cumulative[1] = 1 → place at index 1-1 = 0
#   output: [1, _, _, _, _, _, _]
#   cumulative[1] becomes 0

# Step 2: current = 3
#   cumulative[3] = 5 → place at index 5-1 = 4
#   output: [1, _, _, _, 3, _, _]
#   cumulative[3] becomes 4

# Step 3: current = 3
#   cumulative[3] = 4 → place at index 4-1 = 3
#   output: [1, _, _, 3, 3, _, _]
#   cumulative[3] becomes 3

# Step 4: current = 8
#   cumulative[8] = 7 → place at index 7-1 = 6
#   output: [1, _, _, 3, 3, _, 8]
#   cumulative[8] becomes 6

# Step 5: current = 2
#   cumulative[2] = 3 → place at index 3-1 = 2
#   output: [1, _, 2, 3, 3, _, 8]
#   cumulative[2] becomes 2

# Step 6: current = 2
#   cumulative[2] = 2 → place at index 2-1 = 1
#   output: [1, 2, 2, 3, 3, _, 8]
#   cumulative[2] becomes 1

# Step 7: current = 4
#   cumulative[4] = 6 → place at index 6-1 = 5
#   output: [1, 2, 2, 3, 3, 4, 8]
#   cumulative[4] becomes 5
