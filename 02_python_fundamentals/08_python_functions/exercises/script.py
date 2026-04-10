# 1. Sum of List Elements
def sum_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total


print("Sum of list [1, 2, 3, 4]:", sum_list([1, 2, 3, 4]))


# 2. Repeated Greeting
def repeat_greeting(name, times):
    for _ in range(times):
        print(f"Hello, {name}")


print("Repeated Greeting:")
repeat_greeting("Kosta", 3)


# 3. Factorial Calculation
# def factorial(n):
#     fctrl = 1
#     multiplier = n
#     if n == 0:
#         return 1
#     while multiplier > 0:
#         fctrl *= multiplier
#         multiplier = multiplier - 1
#     return fctrl


def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


print("Factorial of 5:", factorial(5))


# 4. Fibonacci Sequence Generator
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]

    sequence = [0, 1]
    while len(sequence) < n:
        number = sequence[-1] + sequence[-2]
        sequence.append(number)
    return sequence


print("Fibonacci numbers:", fibonacci(1))


# 5. Maximum of Two Numbers
def max_of_two(a, b):
    if a > b:
        return a
    else:
        return b


print("Maximum of 10 and 20:", max_of_two(10, 20))


# 6. Print a Pattern with Nested Loops
def print_triangle(rows):
    for i in range(1, rows + 1):
        for j in range(i):
            print("*", end="")
        print()


# def print_triangle(rows):
#     for i in range(1, rows + 1):
#         print("*" * i)

print("Triangle pattern with 5 rows:")
print_triangle(5)
