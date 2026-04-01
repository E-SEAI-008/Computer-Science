# Step 1: Create and Print a List
numbers = [1, 2, 3, 4, 5]
print("list:", numbers)

# Step 2: Access Elements by Index and Negative Index
print("first item:", numbers[0])
print("last item:", numbers[-1])

# Step: 3 Slice a List
print("index 1 to 3:", numbers[1:3])
print("start to index 2:", numbers[:2])
print("index 2 to end:", numbers[2:])

# Step 4: Check if an Item Exists
if 4 in numbers:
    print("Number 4 exists")

# print("4 is in numbers", 4 in numbers)

# Step 5: Add Items
numbers.append(6)
numbers.insert(6, 7)
print("after append and insert:", numbers)

# Step 6: Change Items
numbers[6] = 5
numbers[1:2] = [8, 9]
print("after changes:", numbers)

# Step 7: Remove items
numbers.remove(4)
numbers.pop()
print("after remove and pop:", numbers)

numbers_2 = [0, 1, 2]
numbers_2.clear()
print("after clear:", numbers_2)

# Step 8: Copy a list
numbers_copy = numbers.copy()
numbers.append(8)
print("original after modification:", numbers)
print("copy unchanged:", numbers_copy)

# Step 9: Concatenate and Extend
colors_a = ["red", "green"]
colors_b = ["blue", "yellow"]
print("concatenated:", colors_a + colors_b)
colors_a.extend(colors_b)
print("extended:", colors_a)

# Step 10: Sort and Reverse
numbers.sort()
print("sorted:", numbers)
numbers.reverse()
print("reversed:", numbers)
sorted_numbers = sorted(numbers)
print("sorted copy:", sorted_numbers)

# Count and Index
print("count of number 3:", numbers.count(3))
print("index of number 5:", numbers.index(5))

# List comprehension
numbers_3 = [1, 2, 3, 4, 5]
numbers_squared = [number * number for number in numbers_3 if number % 2 == 0]
print(numbers_squared)
