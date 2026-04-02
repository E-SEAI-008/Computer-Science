print("--- Creating Sets ---\n")

# Creating sets with curly braces
fruits = {"apple", "banana", "cherry"}
numbers = {1, 2, 3, 4, 5}
mixed = {True, 1, "hello", 3.14}

# Empty set - must use set(), not {}
empty_set = set()
# empty_dict = {}
print(type(empty_set))
# print(type(empty_dict))

# Using set() constructor
from_string = set("hello")
print("from_string:", from_string)  # random order & duplicates removed

print("\n--- Set Properties ---\n")

# Sets are unordered - order may vary
my_set = {5, 2, 8, 1, 9}
print("my_set:", my_set)  # Order not guaranteed

# Duplicates are automatically removed
numbers = {1, 2, 3, 2, 1, 4, 3, 5}
print("numbers:", numbers)  # {1, 2, 3, 4, 5}

# Cannot index or slice
colors = {"red", "green", "blue", "red"}
# colors[0]  # TypeError: 'set' object is not subscriptable

# But can check membership (very fast!)
print("'red' in colors:", "red" in colors)  # True
print("'yellow' in colors:", "yellow" in colors)  # False

# Length works
print("len(colors):", len(colors))  # 3

print("\n--- Adding Items ---\n")

fruits = {"apple", "banana"}

# add() - add single item
fruits.add("cherry")
print("after add:", fruits)  # {'apple', 'banana', 'cherry'}

# Adding duplicate has no effect
fruits.add("apple")
print("after duplicate add:", fruits)  # unchanged

# update() - add multiple items from iterable
fruits.update(["date", "elderberry"])
print("after update:", fruits)

# update() with multiple iterables
fruits.update(["fig"], ("grape",), {"honeydew"})
print("after multi-update:", fruits)

print("\n--- Removing Items ---\n")

colors = {"red", "green", "blue", "yellow", "purple"}

# remove() - removes item, raises KeyError if not found
colors.remove("blue")
print("after remove:", colors)

# discard() - removes item, NO error if not found
colors.discard("gray")
print("after discard:", colors)

# pop() - removes and returns arbitrary item
removed = colors.pop()
print("popped:", removed)
print("after pop:", colors)

# clear() - remove all items
colors.clear()
print("after clear:", colors)  # set()

print("\n--- Looping Through Sets ---\n")

fruits = {"apple", "banana", "cherry", "date"}

# Basic for loop (order not guaranteed)
for fruit in fruits:
    print("fruit:", fruit)

print("\n--- Set Union ---\n")

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# union() method => non-mutating
result = set_a.union(set_b)
print("union():", result)  # {1, 2, 3, 4, 5, 6}

# | operator (shorthand)
result = set_a | set_b
print("a | b:", result)  # {1, 2, 3, 4, 5, 6}

# Union with multiple sets
set_c = {7, 8}
result = set_a | set_b | set_c
print("a | b | c:", result)

# |= operator (in-place union) => mutating
set_x = {1, 2, 3, 4}
set_y = {3, 4, 5, 6}
set_x |= set_y
print("x |= y:", set_x)

print("\n--- Set Intersection ---\n")

set_a = {1, 2, 3, 4, 5}
set_b = {3, 4, 5, 6, 7}

# intersection() method
common = set_a.intersection(set_b)
print("intersection():", common)  # {3, 4, 5}

# & operator (shorthand)
print("a & b:", set_a & set_b)  # {3, 4, 5}

# Intersection with multiple sets
set_c = {4, 5, 8, 9}
print("a & b & c:", set_a.intersection(set_b, set_c))  # {4, 5}

# &= operator (in-place intersection)
set_x = {1, 2, 3, 4}
set_y = {3, 4, 5, 6}
set_x &= set_y
print("x &= y:", set_x)  # {3, 4}

print("\n--- Set Difference ---\n")

set_a = {1, 2, 3, 4, 5}
set_b = {3, 4, 5, 6, 7}

# difference() method
different = set_a.difference(set_b)
print("difference():", different)  # {1, 2}

# - operator (shorthand)
print("a - b:", set_a - set_b)  # {1, 2}

# Difference with multiple sets
set_c = {2, 5, 8}
print("a - b - c:", set_a.difference(set_b, set_c))  # {1}

# -= operator (in-place difference)
set_x = {1, 2, 3, 4, 5}
set_y = {3, 4, 5}
set_x -= set_y
print("x -= y:", set_x)  # {1, 2}

print("\n--- Set Relationships ---\n")

set_a = {1, 2, 3}
set_b = {1, 2, 3, 4, 5}
set_c = {6, 7, 8}

# a.issubset(b) -> "Is everything in a also in b?"
print("a subset of b:", set_a.issubset(set_b))  # True
print("b subset of a:", set_b.issubset(set_a))  # False

# a <= b → same as issubset — is a inside b (or equal to it)?
print("a <= b:", set_a <= set_b)  # True

# a < b → "strict subset" — is a inside b AND not equal to b?
print("a < b (proper):", set_a < set_b)  # True
print("a < a:", set_a < set_a)  # False

# a.issuperset(b) → "Is everything in b also in a?"
print("a superset of b:", set_a.issuperset(set_b))  # False
print("b >= a:", set_b >= set_a)  # True

# a.isdisjoint(c) → "Do these two sets share nothing?"
print("a disjoint c:", set_a.isdisjoint(set_c))  # True
print("a disjoint b:", set_a.isdisjoint(set_b))  # False
