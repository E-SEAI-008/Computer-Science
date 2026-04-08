# 1. Create and Print a Dictionary
person = {
    "name": "John",
    "age": 30,
    "city": "New York",
}
print("person:", person)

# 2. Access Dictionary Elements
print("name:", person["name"])
print("email:", person.get("email", "No email available"))
print("keys:", person.keys())
print("values:", person.values())
print("items:", person.items())

# 3. Check for Key Existence
print(f'checking if the "age" is in person: {"age" in person}')

# if "age" in person:
#     print("age key exists")
# else:
#     print("age key doesn't exists")

# 4. Change and Update Dictionary Elements
person["city"] = "Hamburg"
person.update({"city": "Munich", "occupation": "Engineer"})
print("after update:", person)

# 5. Add New Items to the Dictionary
person["country"] = "USA"
person.update({"hobby": "cycling"})
print("after adding items:", person)

# 6. Remove Items from the Dictionary
removed = person.pop("city")
print("removed:", removed)

last_item = person.popitem()
print("popitem:", last_item)

del person["country"]
print("after del:", person)

person_copy_for_clear = person.copy()
person_copy_for_clear.clear()
print("after clear:", person_copy_for_clear)

# 7. Copy a Dictionary
person_copy = person.copy()
person["name"] = "Alice"
print("original after modification:", person)
print("copy unchanged:", person_copy)

# 8. Using setdefault()
print("setdefault existing key:", person.setdefault("age", "unknown"))
print("setdefault new key:", person.setdefault("email", "alice@example.com"))
print("after setdefault:", person)
