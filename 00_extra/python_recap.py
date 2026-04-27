# ─────────────────────────────────────────
# Iterating Collections
# ─────────────────────────────────────────

print("\n--- List Iteration ---\n")

fruits = ["apple", "banana", "cherry", "orange", "strawberry", "mango"]

# basic — just the value
for fruit in fruits:
    print("fruit:", fruit)

print()

# need the index too? use enumerate
for i, fruit in enumerate(fruits):
    print(f"index {i}:", fruit)

print()

# enumerate with custom start and slicing beforehand
print("slice [1:4] with start=1:")
for i, fruit in enumerate(fruits[1:4], start=1):
    print(f"index {i}:", fruit)

print()

# avoid this — range(len()) is unpythonic
print("range(len()) — unpythonic, avoid unless modifying by index:")
for i in range(len(fruits)):
    print(f"index {i}:", fruits[i])

print("\n--- Tuple Iteration ---\n")

point = (10, 20, 30)

for value in point:
    print("value:", value)

print()

for i, value in enumerate(point):
    print(f"index {i}:", value)

print("\n--- Set Iteration ---\n")

subjects = {"Math", "English", "Science"}

print("iterating set (order not guaranteed):")
for subject in subjects:
    print("subject:", subject)

print()

# membership check is the main use case — O(1)
if "Math" in subjects:
    print("membership check: enrolled in Math")

print("\n--- Dictionary Iteration ---\n")

students = {"Alice": 92, "Bob": 75, "John": 80}

print("keys only:")
for key in students:
    print("key:", key)

print()

print("values only:")
for value in students.values():
    print("value:", value)

print()

print("keys and values:")
for key, value in students.items():
    print(f"{key}: {value}")

print()

print("with index (enumerate on dict):")
for i, (key, value) in enumerate(students.items()):
    print(f"{i}. {key}: {value}")

print()

print("nested dicts:")
students = {
    "S001": {"name": "Alice", "avg": 91},
    "S002": {"name": "Bob", "avg": 75},
}
for student_id, info in students.items():
    print(f"{student_id} — {info['name']}: avg={info['avg']}")

# ─────────────────────────────────────────
# Unpacking
# ─────────────────────────────────────────

print("\n--- Basic Unpacking ---\n")

point = (10, 20, 30)
x, y, z = point
print("x, y, z:", x, y, z)

numbers = [1, 2, 3]
first, second, third = numbers
print("first, second, third:", first, second, third)

print("\n--- Asterisk Unpacking ---\n")

numbers = [1, 2, 3, 4, 5]

first, *rest = numbers
print("first:", first)
print("rest:", rest)

first, *middle, last = numbers
print("first:", first)
print("middle:", middle)
print("last:", last)

first, *_, last = numbers
print("first and last (ignoring middle):", first, last)

print("\n--- Unpacking in a Loop ---\n")

pairs = [(1, "one"), (2, "two"), (3, "three")]
for number, word in pairs:
    print(f"{number} = {word}")

print()

scores = {"Alice": 92, "Bob": 75, "Charlie": 88}
for name, score in scores.items():
    print(f"{name}: {score}")

# ─────────────────────────────────────────
# Ternary Operator
# ─────────────────────────────────────────

print("\n--- Ternary Operator ---\n")

avg = 75
age = 20
user_input = ""

status = "pass" if avg >= 60 else "fail"
label = "adult" if age >= 18 else "minor"
name = user_input or "Anonymous"  # falsy shorthand — empty string → default

print("status:", status)
print("label:", label)
print("name:", name)

print()

# good — simple, one condition
grade = "A" if avg >= 90 else "B"
print("grade (simple ternary):", grade)

# bad — nested ternary, hard to read
grade = "A" if avg >= 90 else "B" if avg >= 80 else "C"
print("grade (nested — avoid):", grade)

print()

print(f"student is: {'adult' if age >= 18 else 'minor'}")

print()

config = {"host": "localhost"}
port = config.get("port") or 8080
print("port (fallback default):", port)

# ─────────────────────────────────────────
# List Comprehension
# ─────────────────────────────────────────

print("\n--- List Comprehension ---\n")

numbers = [1, 2, 3, 4, 5, 6]

# loop version
evens_loop = []
for n in numbers:
    if n % 2 == 0:
        evens_loop.append(n)
print("evens (loop):", evens_loop)

# comprehension — same result
evens = [n for n in numbers if n % 2 == 0]
print("evens (comprehension):", evens)

# with transformation
squared_evens = [n**2 for n in numbers if n % 2 == 0]
print("squared evens:", squared_evens)

# with ternary inside comprehension
labels = ["even" if n % 2 == 0 else "odd" for n in numbers]
print("labels:", labels)
