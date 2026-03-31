print("--- Python Syntax ---\n")

# This is a single-line comment

"""
This is a multi-line comment.
You can write multiple lines in here.
Useful for documentation!
"""

# Variable declaration - no type needed!
name = "John"

# The print() function displays output
print("Hello, ", name)

print("\n--- Variables and Type Checking ---\n")

# Creating variables of different types
student_name = "Bob"
is_enrolled = True

# Check the type of each variable
print("type of student_name: ", type(student_name))
print("type of is_enrolled: ", type(is_enrolled))

# Variables can be reassigned to different types (dynamic typing)
my_variable = 10
print("my_variable before reassignment: ", type(my_variable))

my_variable = "Now I'm a string"
print("my_variable after reassignment: ", type(my_variable))

print("\n--- Type Casting ---\n")
name = "Elizabeth"
# Converting between types
age = 25
age_str = str(age)  # Convert int to string
print("age as string: ", "I am " + age_str + " years old")

# Casting examples
float_example = float(5)
bool_example = bool(0)

print("float(5): ", float_example)
print("bool(1): ", bool_example)

# Be careful with invalid casting
# invalid = int("Hello")

print("\n--- Working with Numbers ---\n")

# Arithmetic operations
a = 10
b = 3

print("a + b:", a + b)  # 13
print("a - b:", a - b)  # 7
print("a * b:", a * b)  # 30
print("a / b:", a / b)  # 3.333...
print("a // b:", a // b)  # 3 (floor division)
print("a % b:", a % b)  # 1 (modulus)
print("a ** b:", a**b)  # 1000 (exponentiation)

# Type mixing
result = 5 + 2.5
print("5 + 2.5:", result, type(result))

# Assignment Operators
x = 10

x += 5  # x = x + 5  → 15
print("after +=5:", x)

x -= 3  # x = x - 3  → 12
print("after -=3:", x)

x *= 2  # x = x * 2  → 24
print("after *=2:", x)

x /= 4  # x = x / 4  → 6.0
print("after /=4:", x)

x //= 2  # x = x // 2 → 3.0
print("after //=2:", x)

x %= 2  # x = x % 2  → 1.0
print("after %=2:", x)

x = 2
x **= 3  # x = x ** 3 → 8
print("after **=3:", x)

print("\n--- String Basics ---\n")

# Creating strings
# single_quotes = 'Hello'
double_quotes = "World"
multi_line = """This is a
multi-line
string"""

# String concatenation
greeting = "Hello" + " " + "Python"
print("greeting:", greeting)  # Hello Python

# String repetition
laugh = "ha" * 3
print("laugh:", laugh)  # hahaha

print("\n--- String Methods ---\n")

text = "  Hello Python World  "

# Case conversion
print("upper:", text.upper())
print("lower:", text.lower())

# Whitespace removal
print("strip:", text.strip())
print("lstrip:", text.lstrip())
print("rstrip:", text.rstrip())

# Replacement
print("replace:", text.replace("Python", "JavaScript"))

# Chaining
words = text.strip().upper()
print("strip + upper:", words)

# Checking content
print("'Python' in text:", "Python" in text)  # True
print("'Java' not in text:", "Java" not in text)  # True

print("\n--- String Formatting ---\n")

name = "Alice"
age = 25
gpa = 3.85

# f-strings
message1 = f"My name is {name} and I am {age} years old."
print("f-string:", message1)

print("\n--- Booleans and Truthy/Falsy Values ---\n")

# Boolean values
is_sunny = True
is_raining = False

print("is_sunny:", is_sunny)
print("is_raining:", is_raining)

# Truthy values (evaluate to True)
print("bool('Hello'):", bool("Hello"))  # True
print("bool(42):", bool(42))  # True

# Falsy values (evaluate to False)
print("bool(''):", bool(""))  # False
print("bool(0):", bool(0))  # False
print("bool(None):", bool(None))  # False

# Using booleans in conditions
temperature = 25
is_warm = temperature > 20
print("is warm:", is_warm)  # True

print("\n--- Comparison Operators ---\n")

x = 10
y = 5

print("x == y:", x == y)  # False
print("x != y:", x != y)  # True
print("x > y:", x > y)  # True
print("x < y:", x < y)  # False
print("x >= 10:", x >= 10)  # True
print("y <= 5:", y <= 5)  # True

# Comparing strings
print("'apple' < 'banana':", "apple" < "banana")  # True
print("'Python' == 'python':", "Python" == "python")  # False

print("\n--- Logical Operators ---\n")

# Logical AND - both must be True
age = 25
has_license = True
can_drive = age >= 18 and has_license
print("can drive:", can_drive)  # True

# Logical OR - at least one must be True
is_weekend = False
is_holiday = True
can_relax = is_weekend or is_holiday
print("can relax:", can_relax)  # True

# Logical NOT - inverts the boolean
is_raining = False
is_sunny = not is_raining
print("is sunny:", is_sunny)  # True

# Combining logical operators
temperature = 25
is_summer = True
go_swimming = temperature > 20 and is_summer and not is_raining
print("go swimming:", go_swimming)  # True
