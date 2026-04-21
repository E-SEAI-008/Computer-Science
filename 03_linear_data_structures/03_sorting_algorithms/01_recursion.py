print("--- Recursion ---\n")

# A function that calls itself with a smaller version of the problem, until it reaches a base case that stops the chain.


def countdown(n):
    if n == 0:
        return
    print(n)
    countdown(n - 1)


# countdown(3)

# What is a Call Stack?

# A call stack is a mechanism for an interpreter to keep track of its place in a script that calls multiple functions — what function is currently being run and what functions are called from within that function, etc. - MDN

# - Stores function calls, local variables, return addresses
# - Managed automatically, memory is freed when a function returns
# - Limited size (~1–8 MB depending on OS)
# - Stack overflow = you exceeded this limit


# countdown(3)
#   └── countdown(2)
#         └── countdown(1)
#               └── countdown(0)  ← base case, returns
#               ← returns
#         ← returns
#   ← returns
