# Default solution: Time O(n), Space O(n)
def is_valid(s):
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}
    for char in s:
        if char in mapping:
            top_element = stack.pop() if stack else "#"
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)
    return not stack


# --- Test: is_valid ---
print(is_valid("()"))  # True
# '(' → push → stack: ['(']
# ')' → pop '(' → matches matching[')']='(' ✓ → stack: []
# End: stack empty → True

print(is_valid("()[]{}"))  # True
# Each pair opens and closes cleanly, stack is empty at the end

print(is_valid("(]"))  # False
# '(' → push → stack: ['(']
# ']' → pop '(' → matching[']']='[' but got '(' ✗ → return False

print(is_valid("([])"))  # True
# '(' → push → stack: ['(']
# '[' → push → stack: ['(', '[']
# ']' → pop '[' → matching[']']='[' ✓ → stack: ['(']
# ')' → pop '(' → matching[')']='(' ✓ → stack: []
# End: stack empty → True
