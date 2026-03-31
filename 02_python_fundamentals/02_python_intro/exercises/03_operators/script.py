# Step 1: Arithmetic Operators
a = 15
b = 4

# Perform arithmetic operations
print("addition:", a + b)
print("subtraction:", a - b)
print("multiplication:", a * b)
print("division:", a / b)
print("floor division:", a // b)
print("modulus:", a % b)
print("exponentiation:", a**b)

# Step 2: Assignment Operators
# Modify x using assignment operators
x = 10

x += 5
print("after +=:", x)
x -= 3
print("after -=:", x)
x *= 2
print("after *=:", x)
x /= 4
print("after /=:", x)

# Step 3: Comparison Operators
# Compare a and b
print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)

# Step 4: Logical Operators
# Combine Boolean variables
is_python_fun = True
is_java_fun = False

print("and:", is_python_fun and is_java_fun)
print("or:", is_python_fun or is_java_fun)
print("not:", not is_python_fun)

# Step 5: Identity Operators
# Check identities
list1 = [1, 2, 3]
list2 = list1
list3 = [1, 2, 3]

print("list1 is list2:", list1 is list2)
print("list1 is not list2:", list1 is not list2)
# Check if list1 is list3
print("list1 is list3:", list1 is list3)

# Step 6: Membership Operators
# Check membership
text = "Python programming is fun!"

print("'Python' in text:", "Python" in text)
print("'Java' not in text:", "Java" not in text)

# Step 7: Bitwise Operators (Bonus)
# Perform bitwise operations
a = 5
b = 3

print("a & b:", a & b)
print("a | b:", a | b)
print("a ^ b:", a ^ b)
print("a << 1:", a << 1)
print("b >> 1:", b >> 1)

# Step 8: Operator Precedence
# Write expressions with precedence
print("without parentheses 2 + 3 * 4 ** 2:", 2 + 3 * 4**2)
print("with parentheses (2 + 3) * (4 ** 2):", (2 + 3) * (4**2))
print("with parentheses ((2 + 3) * 4) ** 2:", ((2 + 3) * 4) ** 2)
