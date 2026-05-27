# Approach 1
def fib_naive(n):
    if n <= 1:
        return n
    return fib_naive(n - 1) + fib_naive(n - 2)


# print(fib_naive(2))
# print(fib_naive(3))
# print(fib_naive(4))

# Computing fib(5):

#                     fib(5)
#                    /      \
#               fib(4)        fib(3)
#              /     \        /     \
#         fib(3)   fib(2)  fib(2)  fib(1)
#         /   \     /  \    /  \
#     fib(2) fib(1) ...  ... ...  ...
#      / \
# fib(1) fib(0)


# Approach 2
def fib_memo(n, memo=None):
    if memo is None:
        memo = {}

    if n in memo:
        return memo[n]

    if n <= 1:
        return n

    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]


# print(fib_memo(2))
# print(fib_memo(3))
# print(fib_memo(40))


# Approach 3
def fib_iterative(n):
    if n <= 1:
        return n

    prev, curr = 0, 1

    for i in range(2, n + 1):
        prev, curr = curr, prev + curr

    return curr


print(fib_iterative(2))
print(fib_iterative(3))
print(fib_iterative(4))

# Computing fib(6):

# Initial: prev = 0, curr = 1

# i = 2:  prev, curr = 1, 0+1 = 1, 1
# i = 3:  prev, curr = 1, 1+1 = 1, 2
# i = 4:  prev, curr = 2, 1+2 = 2, 3
# i = 5:  prev, curr = 3, 2+3 = 3, 5
# i = 6:  prev, curr = 5, 3+5 = 5, 8

# Return curr = 8

# Sequence visualization:
# i=2: [0, 1, 1]
# i=3: [0, 1, 1, 2]
# i=4: [0, 1, 1, 2, 3]
# i=5: [0, 1, 1, 2, 3, 5]
# i=6: [0, 1, 1, 2, 3, 5, 8]
