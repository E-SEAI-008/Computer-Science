paths_a = [["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]
paths_b = [["B", "C"], ["D", "B"], ["C", "A"]]


# Default solution: Time O(n²), Space O(1)
def dest_city(paths):
    for i in range(len(paths)):
        candidate = paths[i][1]
        good = True
        for j in range(len(paths)):
            if paths[j][0] == candidate:
                good = False
                break
        if good:
            return candidate
    return None


# --- Test: dest_city ---
print("--- dest_city ---")
print(dest_city(paths_a))  # Sao Paulo
# candidate="New York": found in starts → skip
# candidate="Lima":     found in starts → skip
# candidate="Sao Paulo": not in starts → return "Sao Paulo"

print(dest_city(paths_b))  # A
# candidate="C": found in starts → skip
# candidate="B": found in starts → skip
# candidate="A": not in starts → return "A"


# Efficient: Hash set — Time O(n), Space O(n)
def dest_city_efficient(paths):
    has_outgoing = set()
    for i in range(len(paths)):
        has_outgoing.add(paths[i][0])
    for i in range(len(paths)):
        candidate = paths[i][1]
        if candidate not in has_outgoing:
            return candidate
    return None


# --- Test: dest_city_efficient ---
print("\n--- dest_city_efficient ---")
print(dest_city_efficient(paths_a))  # Sao Paulo
# has_outgoing = {"London", "New York", "Lima"}
# "New York" in set? Yes. "Lima" in set? Yes. "Sao Paulo" in set? No → return "Sao Paulo"

print(dest_city_efficient(paths_b))  # A
# has_outgoing = {"B", "D", "C"}
# "C" in set? Yes. "B" in set? Yes. "A" in set? No → return "A"


# Alternative efficient: set comprehension — Time O(n), Space O(n)
def dest_city_alternative(paths):
    departures = {path[0] for path in paths}
    for path in paths:
        destination = path[1]
        if destination not in departures:
            return destination
    return None


# --- Test: dest_city_alternative ---
print("\n--- dest_city_alternative ---")
print(dest_city_alternative(paths_a))  # Sao Paulo
# departures = {"London", "New York", "Lima"}
# "New York" in departures? Yes. "Lima"? Yes. "Sao Paulo"? No → return "Sao Paulo"

print(dest_city_alternative(paths_b))  # A
# departures = {"B", "D", "C"}
# "C"? Yes. "B"? Yes. "A"? No → return "A"
