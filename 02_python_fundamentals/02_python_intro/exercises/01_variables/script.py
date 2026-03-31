# Step 1: Create variables:
name = "John"
age = 20
height = 2.01

# Step 2: Print the variables:
print("name:", name)
print("age:", age)
print("height:", height)

# Step 3: Check the type of the variables:
print("type of name:", type(name))
print("type of age:", type(age))
print("type of height:", type(height))

# Step 4: Casting
age_str = str(age)
print(f"My name is {name} and I am {age_str} years old.")

# Bonus: Global Variable (Bonus)
global_message = "Hello from the global scope."
print("before function:", global_message)


def update_global_message():
    global global_message
    global_message = "Hello from the function scope."
    print("inside function:", global_message)


update_global_message()
print("after function:", global_message)
