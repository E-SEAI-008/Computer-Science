print("--- Creating and Accessing Lists ---\n")

# Creating lists
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True, [1, 2, 3]]
empty = []

# Accessing by index (zero-based)
print("first item:", fruits[0])  # apple
print("third item:", fruits[2])  # cherry

# Negative indexing (count from end)
print("last item:", fruits[-1])  # elderberry
print("second to last:", fruits[-2])  # date

# Length of list
print("length:", len(fruits))  # 5

# Membership operators
print("apple in fruits:", "apple" in fruits)  # True
print("grape not in fruits:", "grape" not in fruits)  # True

print("\n--- Modifying List Items ---\n")

colors = ["red", "green", "blue", "yellow"]

# Change a single item
colors[1] = "purple"
print("after single change:", colors)  # ['red', 'purple', 'blue', 'yellow']

# Change multiple items using slice
colors[1:3] = ["orange", "pink"]
print("after slice change:", colors)  # ['red', 'orange', 'pink', 'yellow']

# Replace with different number of items
colors[1:3] = ["cyan", "magenta", "lime"]
print("after unequal replace:", colors)  # ['red', 'cyan', 'magenta', 'lime', 'yellow']

print("\n--- Slicing Lists ---\n")

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Basic slicing [start:end] - end is exclusive
print("numbers[2:5]:", numbers[2:5])  # [2, 3, 4]

# Omitting start or end
print("numbers[:4]:", numbers[:4])  # [0, 1, 2, 3]
print("numbers[5:]:", numbers[5:])  # [5, 6, 7, 8, 9]

# Negative indices in slicing
print("all except last 2:", numbers[:-2])  # [0, 1, 2, 3, 4, 5, 6, 7]
print("last 3:", numbers[-3:])  # [7, 8, 9]

# Step parameter [start:end:step]
print("every 2nd:", numbers[::2])  # [0, 2, 4, 6, 8]
print("every 2nd from 1:", numbers[1::2])  # [1, 3, 5, 7, 9]

print("\n--- Adding Items to Lists ---\n")

names = ["John", "Jane"]

# append() - add to end
names.append("Jim")
print("after append:", names)  # ['John', 'Jane', 'Jim']

# insert() - add at a specific position
names.insert(1, "Jan")
print("after insert:", names)  # ['John', 'Jan', 'Jane', 'Jim']

# extend() - add multiple items from another iterable
more_names = ["Jeremy", "James"]
names.extend(more_names)
print("after extend:", names)  # ['John', 'Jan', 'Jane', 'Jim', 'Jeremy', 'James']

print("\n--- Removing Items from Lists ---\n")

fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# remove() - removes first occurrence of value
fruits.remove("banana")
print("after remove:", fruits)  # ['apple', 'cherry', 'date', 'elderberry']

# pop() - removes and returns item at index (default: last)
popResult = fruits.pop()
print("after pop:", fruits)  # ['apple', 'cherry', 'date']
print(popResult)

# del keyword - delete by index
del fruits[1]
print("after del:", fruits)  # ['apple', 'date']

# clear() - remove all items
fruits.clear()
print("after clear:", fruits)  # []

print("\n--- Looping Through Lists ---\n")

numbers = [2, 4, 6, 1, 3, 9]

# Basic for loop
for number in numbers:
    print("number:", number)

# Loop that builds a new list
squared_numbers = []

for number in numbers:
    if number == 4:
        continue
    squared_numbers.append(number * number)

print("squared:", squared_numbers)

print("\n--- List Comprehension Basics ---\n")

# new_list = [expression for item in iterable if condition]

# Convert strings to uppercase
fruits = ["apple", "banana", "cherry"]

upper_fruits = [fruit.upper() for fruit in fruits]
print("uppercase:", upper_fruits)  # ['APPLE', 'BANANA', 'CHERRY']

# Squares of even number using comprehension
numbers = [2, 4, 6, 1, 3, 9]

new_squared_numbers = [number * number for number in numbers if number % 2 == 0]
print("squared evens:", new_squared_numbers)

print("\n--- List Methods ---\n")

numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]

# count() - count occurrences
print("count of 1:", numbers.count(1))  # 2

# index() - find first occurrence
print("index of 4:", numbers.index(4))  # 2

# copy() - copies the list
print("copy:", numbers.copy())  # [3, 1, 4, 1, 5, 9, 2, 6, 5]

# reverse() - reverse in place (modifies original)
numbers.reverse()
print("reversed:", numbers)  # [5, 6, 2, 9, 5, 1, 4, 1, 3]

# sort() - sorts in place (modifies original)
numbers.sort()
print("sorted asc:", numbers)  # [1, 1, 2, 3, 4, 5, 5, 6, 9]

# sort() in descending order
numbers.sort(reverse=True)
print("sorted desc:", numbers)  # [9, 6, 5, 5, 4, 3, 2, 1, 1]
