# Step 1: Create Strings
first_name = "John"
last_name = "Doe"
bio = """I am a real person.
Trust me on this."""

# Step 2: Access Characters and Slice Strings
print("first character:", first_name[0])
print("last character:", last_name[-1])
print("first 10 chars:", bio[0:10])

# Step 3: Loop Through a String
for character in first_name:
    print("character:", character)

# Step 4: String Length
print("bio length:", len(bio))

# Step 5: Check Substrings
print("'Python' in bio:", "Python" in bio)
print("'Java' not in bio:", "Java" not in bio)

# Step 6: Modify Strings
print("uppercase:", first_name.upper())
print("lowercase:", last_name.lower())
print("stripped:", bio.strip())
print("replaced:", bio.replace("person", "coding"))
print("split:", bio.split())

# Step 7: Concatenate Strings
full_name = first_name + " " + last_name
print("full name:", full_name)

# Step 8: String Formatting
print(f"Hello, my name is {full_name} and I love Python!")
print("My full name is {} and I am {} years old.".format(full_name, 30))

# Step 9: Escape Characters
quote = 'He said, "Python\'s great!"'
print("quote:", quote)

# Bonus: Use String Methods
print("centered bio: ", bio.center(50))
print("count of 'a' in full_name:", full_name.count("a"))
