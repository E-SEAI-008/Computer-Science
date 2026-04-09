# 1. Basic If Condition
number = 0

if number > 0:
    print("Number is positive")
elif number < 0:
    print("Number is negative")
else:
    print("Number is zero")

# 2. Grade Calculator
score = 85

if score >= 90:
    print("grade: A")
elif score >= 80:
    print("grade: B")
elif score >= 70:
    print("grade: C")
elif score >= 60:
    print("grade: D")
else:
    print("grade: F")

# 3. Ternary Operator Practice
age = 19
status = "adult" if age >= 18 else "minor"
print("status:", status)

# 4. For Loop over a List
vehicles = ["car", "bike", "plane"]
for vehicle in vehicles:
    print(f"vehicle: {vehicle}")

# 5. For Loop with Conditions
for number in range(1, 11):
    if number % 2 != 0:
        continue
    print("is even:", number)

# 6. While Loop Summation
total = 0
count = 1

while count <= 100:
    total += count
    count += 1
print(f"Sum of 1 to 100: {total}")

# 7. Break out of a Loop
words = ["hello", "dog", "word", "garden", "tent"]

for word in words:
    if len(word) > 5:
        print("first word longer than 5 letters:", word)
        break

# 8. Nested Loops
people = ["John", "Jane", "Joe"]
pets = ["cat", "dog", "bird"]

for person in people:
    for pet in pets:
        print(f"{person} has a {pet}")

# 9. Loop with Else Clause
haystack = [
    "test",
    "cat",
    "needle",
    "january",
    "home",
]
needle = "fdbdfbf"

for word in haystack:
    if word == needle:
        print(f"Success! {needle} was found in the list")
        break
else:
    print(f"{needle} was not found in the list")

# 10. Pass Statement Usage
items = ["apple", "banana", "cherry"]

for item in items:
    pass

# 11. Pattern matching
fruits = ["apple", "banana", "orange", "mango"]
veggies = ["carrot", "broccoli", "spinach", "pepper"]
meat = ["chicken", "beef", "pork", "lamb"]

item = "chicken"

match item:
    case _ if item in fruits:
        print(f"{item} is a fruit")
    case _ if item in veggies:
        print(f"{item} is a veggie")
    case _ if item in meat:
        print(f"{item} is a meat")
    case _:
        print("Item is not categorized")
