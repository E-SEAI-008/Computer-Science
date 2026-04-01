print("--- Creating Tuples ---\n")

# Creating tuples
fruits = ("apple", "banana", "cherry")
numbers = (1, 2, 3, 4, 5)
mixed = (1, "hello", 3.14, True)

# Tuple without parentheses (packing)
coordinates = 10, 20, 30
print("type of coordinates:", type(coordinates))  # <class 'tuple'>

# Empty tuple
empty = ()
print("empty length:", len(empty))  # 0

# Using tuple() constructor
from_list = tuple([1, 2, 3])
from_string = tuple("hello")
print("from list:", from_list)  # (1, 2, 3)
print("from string:", from_string)  # ('h', 'e', 'l', 'l', 'o')

print("\n--- Accessing Tuple Elements ---\n")

colors = ("red", "green", "blue", "yellow", "purple")

# Positive indexing
print("first:", colors[0])  # red

# Negative indexing
print("last:", colors[-1])  # purple

# Length
print("length:", len(colors))  # 5

# Check membership
print("'green' in colors:", "green" in colors)  # True
print("'orange' not in colors:", "orange" not in colors)  # True

print("\n--- Slicing Tuples ---\n")

numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

# Basic slicing [start:end]
print("numbers[2:5]:", numbers[2:5])  # (2, 3, 4)

# Omitting start or end
print("numbers[:4]:", numbers[:4])  # (0, 1, 2, 3)
print("numbers[5:]:", numbers[5:])  # (5, 6, 7, 8, 9)

# Negative indices
print("last 3:", numbers[-3:])  # (7, 8, 9)
print("all except last 2:", numbers[:-2])  # (0, 1, 2, 3, 4, 5, 6, 7)

# Step parameter
print("every 2nd:", numbers[::2])  # (0, 2, 4, 6, 8)
print("every 2nd from 1:", numbers[1::2])  # (1, 3, 5, 7, 9)

print("\n--- Tuple Immutability ---\n")

# Tuples cannot be modified
# coordinates[0] = 15     # TypeError!
# coordinates.append(40)  # AtrributeError!

# You can reassign the entire variable
coordinates = (10, 20, 30)
coordinates = (20, "20", 40, "10")
print("reassigned:", coordinates)

print("\n--- Tuple Methods ---\n")

numbers = (1, 2, 3, 2, 4, 2, 5, 6, 2)

# count() - count occurrences
print("count of 2:", numbers.count(2))  # 4

# index() - find first occurrence
print("index of 3:", numbers.index(3))  # 2

# index() with start and end parameters
print("index of 2 after pos 2:", numbers.index(2, 2))  # 3
print("index of 2 between 4-8:", numbers.index(2, 4, 8))  # 5

print("\n--- Basic Tuple Unpacking ---\n")

# Unpacking into variables
point = (10, 20)
x, y = point
print(f"x = {x}, y = {y}")  # x = 10, y = 20

# RGB color
color = (255, 128, 0)
red, green, blue = color
print(f"R:{red} G:{green} B:{blue}")  # R:255 G:128 B:0

# Swapping variables
a = 5
b = 10
a, b = b, a
print(f"a = {a}, b = {b}")  # a = 10, b = 5

print("\n--- Unpacking with Asterisk (*) ---\n")

# Collect remaining items
numbers = (1, 2, 3, 4, 5)
first, *rest = numbers
print("first:", first)  # 1
print("rest:", rest)  # [2, 3, 4, 5] - Note: rest is a LIST!

# Asteriks in the middle
first, *middle, last = numbers
print("first:", first)  # 1
print("middle:", middle)  # [2, 3, 4]
print("last:", last)  # 5

# Asterisk at the beginning
*beginning, second_last, last = numbers
print("beginning:", beginning)  # [1, 2, 3]
print("second_last:", second_last)  # 4
print("last:", last)  # 5

# Practical example: parsing data
data = ("Alice", "Smith", 25, "Engineer", "New York")
first_name, last_name, *other_info = data
print("name:", f"{first_name} {last_name}")  # Alice Smith
print("other info:", other_info)  # [25, 'Engineer', 'New York']

print("\n--- Joining Tuples - Concatenation ---\n")

# Using + operator
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined = tuple1 + tuple2
print("combined:", combined)  # (1, 2, 3, 4, 5, 6)

# Original tuples unchanged
print("tuple1:", tuple1)  # (1, 2, 3)
print("tuple2:", tuple2)  # (4, 5, 6)

# Adding single item (must be tuple!)
fruits = ("apple", "banana")
more_fruits = fruits + ("cherry",)  # Note the comma!
print("more fruits:", more_fruits)  # ('apple', 'banana', 'cherry')

print("\n--- Joining Tuples - Multiplication ---\n")

# Repeat tuple multiple times
base = (1, 2, 3)
repeated = base * 3
print("repeated:", repeated)  # (1, 2, 3, 1, 2, 3, 1, 2, 3)

# Practical use: initialize with default values
zeros = (0,) * 5
print("zeros:", zeros)  # (0, 0, 0, 0, 0)

# Create pattern
pattern = ("X", "O") * 4
print("pattern:", pattern)  # ('X', 'O', 'X', 'O', 'X', 'O', 'X', 'O')

print("\n--- Looping Through Tuples ---\n")

colors = ("red", "green", "blue", "yellow")

# Basic for loop
for color in colors:
    print("color:", color)

# With enumerate() for index
for index, color in enumerate(colors):
    print(f"  {index + 1}: {color}")
