print("--- Basic Function ---\n")


# Basic function - no input & no return - function without return statement returns None
def say_hello():
    print("Hello!")


say_hello()

result = say_hello()
print("result:", result)

print("\n--- Arguments and Return ---\n")


# Function with return statement & positional arguments
def greet(greeting, name):
    return f"{greeting}, {name}"


greet_result = greet("Hello", "Alice")
print("greet_result:", greet_result)


# Default parameters - used when argument is not provided
def greet_default(name, greeting="Hello"):
    return f"{greeting}, {name}"


print("greet_default:", greet_default("Bob"))  # Uses default greeting
print("greet_default:", greet_default("Bob", "Hey"))  # Overrides default

# Keyword arguments - pass arguments by name, order doesn't matter
print("greet_default:", greet_default(greeting="Hi", name="Charlie"))


# Difference between return and no return
def add_with_return(a, b):
    return a + b


def add_no_return(a, b):
    result = a + b
    # return result


print("with return:", add_with_return(3, 4))
print("no return:", add_no_return(3, 4))


# Return multiple values - Python packs them into a tuple
def min_max(numbers):
    return min(numbers), max(numbers)


numbers_list = [3, 1, 9, 4, 7]

low, high = min_max(numbers_list)
print("min:", low)
print("max:", high)

print("\n--- *args and **kwargs ---\n")


# *args - collect any number of positional arguments into a tuple
#       - useful when you don't know hoe many values will be passed
def total(*numbers):
    print("received numbers:", numbers)
    return sum(numbers)


print("total:", total(1, 2, 3, 4, 5))


# **kwargs - collect any number of keyword arguments into a dictionary
#          - useful for named options
def describe(**info):
    print("received info:", info)
    for key, value in info.items():
        print(f"    {key}: {value}")


describe(name="John", age=25, city="Hamburg")


# Combining both - *args before **kwargs
def mixed(required, *args, **kwargs):
    print("required:", required)
    print("extra positional:", args)
    print("extra keyword:", kwargs)


mixed("hello", 1, 2, 3, color="red", size="large")

print("\n--- Lambda ---\n")

# Lambda is an anonymous one-liner function
# Syntax: lambda parameter(s): expression

# Basic lambda assigned to a variable
square = lambda x: x**2
print("square of 5:", square(5))

# Lambda with multiple parameters
add = lambda a, b: a + b
print("add 3+4:", add(3, 4))

# Lambda inside a function
# sorted() and map() accept a function as an argument
students = [
    {"name": "Charlie", "avg": 95},
    {"name": "Alice", "avg": 88},
    {"name": "Bob", "avg": 72},
]

# sorted() - lambda defines what to sort by
# sorted_students = sorted(students, key=lambda student: student["avg"])
sorted_students = sorted(students, key=lambda student: student["name"])
print(sorted_students)


# map() — apply a function to every item in a list
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print("squared:", squared)

print("\n--- Scope ---\n")


# Variables inside a function are local — invisible outside
def my_function():
    local_var = "I only exist inside"
    print("inside:", local_var)


my_function()
# print(local_var)   # NameError — doesn't exist out here

# global variable
counter = 0


def increment():
    global counter  # Creating a global variable inside block scope requires "global" keyword
    counter += 1


increment()
increment()
print("counter:", counter)

print("\n--- Error Handling ---\n")

# try: code that might fail
# except: runs if an error occurs
# else: runs only if NO error occurred
# finally: always runs, error or not


def divide(a, b):
    try:
        result = a / b  # ZeroDivisionError might occur
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
        return None
    else:
        print("Success: No Errors occured!")
        return result
    finally:
        print("Finally: This always runs!")


print("10 / 2 =", divide(10, 2))
print("10 / 0 =", divide(10, 0))


# Catching multiple exception types
def parse_input(value):
    try:
        number = int(value)
        result = 100 / number
    except ValueError:
        print("Error: Not a valid number")
        return None
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
        return None
    except Exception as MyPersonalError:
        print("Unexpected error:", MyPersonalError)  # Catch-all for anything else
        return None
    else:
        return result


print("parse '5':", parse_input("5"))
print("parse 'abc':", parse_input("abc"))
print("parse '0':", parse_input("0"))
