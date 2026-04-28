# Default solution: Time O(n²), Space O(1)
def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


# --- Test: two_sum ---
print("--- two_sum ---")
print(two_sum([2, 7, 11, 15], 9))  # [0, 1]
# i=0 (num=2), j=1 (num=7): 2+7=9 ✓ → return [0,1]

print(two_sum([3, 2, 4], 6))  # [1, 2]
# i=0 (num=3), j=1 (num=2): 3+2=5 ✗
# i=0 (num=3), j=2 (num=4): 3+4=7 ✗
# i=1 (num=2), j=2 (num=4): 2+4=6 ✓ → return [1,2]


# Alternative: enumerate + collect all results
def two_sum_enumerate(nums, target):
    results = []
    for i, num_i in enumerate(nums):
        for j, num_j in enumerate(nums[i + 1 :], start=i + 1):
            if num_i + num_j == target:
                results.append([i, j])
    return results


# --- Test: two_sum_enumerate ---
print("\n--- two_sum_enumerate ---")
print(two_sum_enumerate([2, 7, 11, 15], 9))  # [[0, 1]]
# i=0 (num=2), j=1 (num=7):  2+7=9  ✓ → append [0,1]
# i=0 (num=2), j=2 (num=11): 2+11=13 ✗
# i=0 (num=2), j=3 (num=15): 2+15=17 ✗
# i=1 (num=7), j=2 (num=11): 7+11=18 ✗
# i=1 (num=7), j=3 (num=15): 7+15=22 ✗
# i=2 (num=11),j=3 (num=15): 11+15=26 ✗
# → [[0, 1]]

print(two_sum_enumerate([2, 7, 2, 7], 9))  # [[0,1], [0,3], [1,2], [2,3]]
# i=0 (num=2), j=1 (num=7): 2+7=9 ✓ → append [0,1]
# i=0 (num=2), j=2 (num=2): 2+2=4 ✗
# i=0 (num=2), j=3 (num=7): 2+7=9 ✓ → append [0,3]
# i=1 (num=7), j=2 (num=2): 7+2=9 ✓ → append [1,2]
# i=1 (num=7), j=3 (num=7): 7+7=14 ✗
# i=2 (num=2), j=3 (num=7): 2+7=9 ✓ → append [2,3]
# → [[0,1], [0,3], [1,2], [2,3]]


# Efficient: hash table, single pass => Time O(n), Space O(n)
def two_sum_efficient(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i


# --- Test: two_sum_efficient ---
print("\n--- two_sum_efficient ---")
print(two_sum_efficient([2, 7, 11, 15], 9))  # [0, 1]
# i=0, num=2: complement=7, seen={}       → not found. seen={2:0}
# i=1, num=7: complement=2, seen={2:0}   → found! return [0,1]

print(two_sum_efficient([3, 2, 4], 6))  # [1, 2]
# i=0, num=3: complement=3, seen={}          → not found. seen={3:0}
# i=1, num=2: complement=4, seen={3:0}       → not found. seen={3:0, 2:1}
# i=2, num=4: complement=2, seen={3:0, 2:1} → found! return [1,2]

print(two_sum_efficient([3, 3], 6))  # [0, 1]
# i=0, num=3: complement=3, seen={}      → not found. seen={3:0}
# i=1, num=3: complement=3, seen={3:0}  → found! return [0,1]
