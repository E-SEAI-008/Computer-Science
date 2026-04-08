print("--- Conditionals ---\n")

# if/else statement
score = 75
if score >= 90:
    print("grade:", "A")
elif score >= 80:
    print("grade:", "B")
elif score >= 70:
    print("grade:", "C")
else:
    print("grade:", "F")

# Ternary Operator
age = 18
status = "adult" if age >= 18 else "minor"
print("status:", status)

print("\n--- For and While Loops ---\n")

# for-loop
vehicles = ["car", "bike", "plane"]
for vehicle in vehicles:
    print("vehicle:", vehicle)

# range (with steps optionally)
for i in range(0, 10):
    print("floats:", i / 10)

# while-loop with break/continue/pass & else statement
count = 0
while count < 10:
    count += 1
    if count % 2 == 0:
        continue
    if count > 7:
        break
    if count == 0:
        pass
    print("odd count:", count)
else:
    print("Loop completed without break")

print("\n--- Loop Else and Pattern Matching ---\n")

# else runs only if loop didn't break
haystack = ["cat", "needle", "dog"]
for word in haystack:
    if word == "needle":
        print("found:", word)
        break
else:
    print("result:", "not found")

# pattern matching with guards
fruits = ["apple", "cherry", "mango"]
veggies = ["carrot", "broccoli"]
meat = ["chicken", "beef"]

item = "test"
match item:
    case _ if item in fruits:
        print("category:", "fruit")
    case _ if item in veggies:
        print("category:", "veggies")
    case _ if item in meat:
        print("category:", "meat")
    case _:
        print("category:", "unknown")
