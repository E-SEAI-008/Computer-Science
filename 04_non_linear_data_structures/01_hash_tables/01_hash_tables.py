# ==============================================================================
# SECTION 1: You've Already Seen This
# ==============================================================================

# This is a hash map — you've used this pattern before
student = {"name": "Alice", "avg": 91}
print(student["name"])  # O(1) lookup

students = {"S001": {"name": "Alice", "avg": 91}, "S002": {"name": "Bob", "avg": 75}}
print(students["S001"]["name"])  # O(1) lookup

# This is a hash set — you've used this too
subjects = {"Math", "English", "Science"}
if "Math" in subjects:  # O(1) membership check
    print("enrolled in Math")


# ==============================================================================
# SECTION 2: What Are Collisions?
# ==============================================================================

# A collision happens when two different keys produce the same hash index
# Example with size=8:
#   hash("Alice") % 8 = 6
#   hash("Bob") % 8 = 3
#   hash("Dan") % 8 = 3  ← collision! Both Bob and Dan want bucket 3

# Two ways to handle collisions:

# 1. CHAINING (what we use):
#    Each bucket holds a list of all items that hash to that index
#    Bucket 3: [('Bob', 85), ('Dan', 78)]
#    Lookup: hash the key, go to bucket, scan the list

# 2. OPEN ADDRESSING:
#    If a bucket is occupied, probe for the next empty slot
#    Try index, index+1, index+2, ... until you find an empty spot

# Why collisions matter:
# - With chaining: if bucket has k items, lookup is O(k)
# - Good hash function + low load factor keeps k small (usually 1-2)
# - Worst case: all items in one bucket = O(n) lookup


# ==============================================================================
# SECTION 3: Understanding Load Factor
# ==============================================================================

# Understanding Load Factor
# Load Factor = Number of items / Number of buckets

# Low load factor (sparse)
# buckets = 10, items = 3
# load factor = 3/10 = 0.3
# Buckets: [[], [item], [], [], [item], [], [], [item], [], []]
# Lots of empty space, few collisions

# High load factor (crowded)
# buckets = 10, items = 15
# load factor = 15/10 = 1.5
# Buckets: [[item, item], [item], [item, item, item], [], [item], ...]
# Many collisions, slower lookups

# Why it matters:
# - Low (< 0.5): Fast lookups, but wastes memory
# - Medium (0.5 - 0.75): Good balance — the sweet spot
# - High (> 0.75): Too many collisions, performance degrades


# ==============================================================================
# SECTION 4: Hash Set Implementation
# ==============================================================================


class HashSet:
    def __init__(self, size=10):
        """Initialise the hash set with a fixed number of buckets."""
        self.size = size
        self.buckets = [[] for _ in range(size)]

    def hash_func(self, key):
        """A simple hash function that sums character ordinals.
        Then takes modulo with self.size to get an index."""
        if isinstance(key, str):
            return sum(ord(ch) for ch in key) % self.size
        if isinstance(key, int):
            return key % self.size
        return hash(key) % self.size  # fallback to Python's built-in

    def add(self, key):
        """Insert a key into the set if it's not already present."""
        index = self.hash_func(key)
        bucket = self.buckets[index]
        if key not in bucket:
            bucket.append(key)

    def remove(self, key):
        """Remove a key from the set if it exists."""
        index = self.hash_func(key)
        bucket = self.buckets[index]
        try:
            bucket.remove(key)
        except ValueError:
            pass  # key wasn't in the bucket, nothing to do

    def __contains__(self, key):
        """Enable 'in' operator: key in my_set"""
        index = self.hash_func(key)
        bucket = self.buckets[index]
        return key in bucket


my_set = HashSet()
my_set.add("Piano")
my_set.add("Running")
my_set.add("Piano")  # duplicate — won't be inserted twice

print("'Piano' in my_set?", "Piano" in my_set)  # True
print("'Skiing' in my_set?", "Skiing" in my_set)  # False

my_set.remove("Piano")
print("'Piano' in my_set after removal?", "Piano" in my_set)  # False


# ==============================================================================
# SECTION 5: Hash Collision Example
# ==============================================================================

# Custom hash function calculations (with size=8):
# "Alice" = (65+108+105+99+101) = 478 % 8 = 6
# "Bob" = (66+111+98) = 275 % 8 = 3
# "Dan" = (68+97+110) = 275 % 8 = 3 ← collision with Bob!
# "Eve" = (69+118+101) = 288 % 8 = 0

# Resulting bucket distribution:
# Bucket 0: [('Eve', 95)]
# Bucket 1: []
# Bucket 2: []
# Bucket 3: [('Bob', 85), ('Dan', 78)] ← Collision here!
# Bucket 4: []
# Bucket 5: []
# Bucket 6: [('Alice', 92)]
# Bucket 7: []


# ==============================================================================
# SECTION 6: Hash Map Implementation
# ==============================================================================


class HashMap:
    def __init__(self, size=10):
        """Initialize the hash map with a fixed number of buckets."""
        self.size = size
        self.buckets = [[] for _ in range(size)]  # each bucket holds (key, value) pairs

    def hash_func(self, key):
        """A simple hash function."""
        if isinstance(key, str):
            return sum(ord(ch) for ch in key) % self.size
        elif isinstance(key, int):
            return key % self.size
        else:
            return hash(key) % self.size

    def __setitem__(self, key, value):
        """Enable assignment: my_map[key] = value"""
        index = self.hash_func(key)
        bucket = self.buckets[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)  # update existing key
                return
        bucket.append((key, value))  # new entry

    def __getitem__(self, key):
        """Enable lookup: my_map[key]"""
        index = self.hash_func(key)
        bucket = self.buckets[index]
        for k, v in bucket:
            if k == key:
                return v
        raise KeyError(f"Key '{key}' not found")

    def __delitem__(self, key):
        """Enable deletion: del my_map[key]"""
        index = self.hash_func(key)
        bucket = self.buckets[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return
        raise KeyError(f"Key '{key}' not found")

    def __contains__(self, key):
        """Enable 'in' operator: key in my_map"""
        index = self.hash_func(key)
        bucket = self.buckets[index]
        for k, v in bucket:
            if k == key:
                return True
        return False

    def get(self, key, default=None):
        """Get value with optional default (like dict.get())"""
        try:
            return self[key]
        except KeyError:
            return default


my_map = HashMap()
my_map["Book"] = 12.99
my_map["Laptop"] = 999.00
my_map["Book"] = 10.99  # update the value

print("Book price:", my_map["Book"])  # 10.99
print("Laptop price:", my_map["Laptop"])  # 999.00
print("'Phone' in my_map?", "Phone" in my_map)  # False
print("'Book' in my_map?", "Book" in my_map)  # True
print("Phone price:", my_map.get("Phone", 0))  # 0 (default)

del my_map["Book"]
print("Book price after deletion:", my_map.get("Book"))  # None
