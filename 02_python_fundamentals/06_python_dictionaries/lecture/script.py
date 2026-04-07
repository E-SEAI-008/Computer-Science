print("--- Creating Dictionaries ---\n")

# Creating dictionaries with curly braces
person = {
    "name": "John",
    "age": 25,
    "city": "New York",
}

# Empty dictionary
empty = {}
print("type of empty:", type(empty))  # <class 'dict'>

# Using dict() constructor
person2 = dict(name="Bob", age=30, city="London")
print("person2:", person2)

# From list of tuples
pairs = [("name", "Charlie"), ("age", 35)]
person3 = dict(pairs)
print("person3:", person3)

# Using fromkeys() - all keys get same value
keys = ["name", "age", "city"]
template = dict.fromkeys(keys, "Unknown")
print("template:", template)

print("\n--- Accessing Dictionary Items ---\n")

person = {
    "name": "Alice",
    "age": 25,
    "city": "New York",
    "email": "alice@email.com",
}

# Access using square brackets - Crashes with Error when not existing
print("name:", person["name"])
print("age:", person["age"])

# Safe access using get() - Doesn't crash when not existing
print("email:", person.get("email"))
print("phone:", person.get("phone"))

# .get() - Lets you set a fallback default:
print("phone default:", person.get("phone", "Not provided"))

# Check if key exists
if "age" in person:
    print("age exists:", person["age"])

if "phone" not in person:
    print("phone not available")

# Get all keys
print("keys:", list(person.keys()))

# Get all values
print("values:", list(person.values()))

# Get all key-value pairs
print("items:", list(person.items()))

print("\n--- Modifying Dictionary Elements ---\n")

person = {
    "name": "Alice",
    "age": 25,
    "city": "New York",
}

# Change existing value
person["age"] = 26
print("after age update:", person)

# Add new key-value pair
person["email"] = "alice@email.com"
print("after adding email:", person)

# Add or update multiple items at once
person.update(
    {
        "age": 27,
        "phone": "555-1234",
        "country": "USA",
    }
)
print("after update():", person)

# setdefault() - Add only if key doesn't exist
person.setdefault("name", "Jane")
print("name (unchanged):", person["name"])

person.setdefault("test", "default_value")
print("test (added):", person["test"])

print("\n--- Removing Items from Dictionaries ---\n")

person = {
    "age": 25,
    "email": "alice@email.com",
    "name": "Alice",
    "phone": "555-1234",
    "city": "New York",
}

# pop() - remove and return value - Crashes with Error when not existing
email = person.pop("email")
print("removed email:", email)
print("after pop:", person)

# pop() with default - Doesn't crash when not existing
mobile = person.pop("mobile", "Not found")
print("mobile pop default:", mobile)

# popitem() - Remove and return last inserted item
last_item = person.popitem()
print("popitem:", last_item)

# del keyword - Delete specific key
del person["age"]
print("after del age:", person)

# clear() - Remove all items
person.clear()
print("after clear:", person)

print("\n--- Looping Through Dictionaries ---\n")

person = {
    "name": "Alice",
    "age": 25,
    "city": "New York",
    "email": "alice@email.com",
}

# Loop through key-value pairs
for key, value in person.items():
    print(f"{key}: {value}")

# With enumerate for numbering
for index, (key, value) in enumerate(person.items(), start=1):
    print(f"  {index}. {key}: {value}")

print("\n--- Copying Dictionaries ---\n")

# copy() - Creates a shallow copy
original = {
    "name": "Alice",
    "age": 25,
}
copy1 = original.copy()
copy1["age"] = 30
print("original:", original)
print("copy1:", copy1)

# SHALLOW COPY WARNING - Nested objects are still referenced
original = {
    "name": "Alice",
    "scores": [85, 90, 95],
}
shallow = original.copy()
shallow["scores"].append(100)  # Modifies original too!
print("original scores (affected):", original["scores"])

# DEEP COPY - For nested structures
import copy  # To use a module you need to import it first

original = {
    "name": "Alice",
    "scores": [85, 90, 95],
}
deep = copy.deepcopy(original)
deep["scores"].append(100)  # Does not modify the original!
print("original scores (safe):", original["scores"])
print("deep scores:", deep["scores"])

print("\n--- Nested Dictionaries ---\n")

# Keys can be any immutable type (string, integer, tuple etc.)

users = {
    "user1": {
        "name": {"first_name": "John", "last_name": "Doe"},
        "age": 25,
        "email": "alice@email.com",
        "scores": [90, 90, 90],
        10: 10,
    },
    "user2": {"name": "Bob", "age": 30, "email": "bob@email.com"},
    "user3": {"name": "Charlie", "age": 35, "email": "charlie@email.com"},
}

# Access nested values
print("user1 name:", users["user1"]["name"]["first_name"])

# Safe access with get()
email = users.get("user1", {}).get("email", "No email")
print("user1 email:", email)

phone = users.get("user1", {}).get("phone", "No phone")
print("user1 phone:", phone)

# Loop through nested dictionary
for user_id, user_info in users.items():
    print(f"  {user_id}:")
    for key, value in user_info.items():
        print(f"    {key}: {value}")

print("\n--- Merging Dictionaries ---\n")

# Python 3.9+ - Using | operator
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged = dict1 | dict2
print("merged:", merged)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Overlapping keys - Second dict wins
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
merged = dict1 | dict2
print("overlapping:", merged)  # {'a': 1, 'b': 3, 'c': 4}

# Using ** unpacking (Python 3.5+)
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged = {**dict1, **dict2}
print("unpacked merge:", merged)

# Merging multiple dictionaries
d1 = {"a": 1}
d2 = {"b": 2}
d3 = {"c": 3}
merged = {**d1, **d2, **d3}
print("multi merge:", merged)
