# 1. Create a Tuple
my_tuple = ("apple", "banana", "cherry", "mango", "kiwi", "cherry")

# 2. Print the Tuple
print("tuple:", my_tuple)

# 3. Access Tuple Items
print("first item:", my_tuple[0])
print("last item:", my_tuple[-1])

# 4. Slice the Tuple
print("middle items:", my_tuple[1:4])
print("start to index 3:", my_tuple[:3])
print("index 3 to end:", my_tuple[3:])

# 5. Check if an Item Exists
if "mango" in my_tuple:
    print("mango is in the tuple")

# 6. Count and Index
print("count of 'cherry':", my_tuple.count("cherry"))
print("index of 'cherry':", my_tuple.index("cherry"))

# 7. Packing and Unpacking
first, second, third, fourth, fifth, sixth = my_tuple
print("unpacked:", first, second, third, fourth, fifth, sixth)

start, *middle, last = my_tuple
print("start:", start)
print("middle:", middle)
print("last:", last)

# 8. Joining Tuples
another_tuple = ("grape", "pear", "plum")
combined = my_tuple + another_tuple
print("conatenated:", combined)
print("multiplied:", another_tuple * 2)
