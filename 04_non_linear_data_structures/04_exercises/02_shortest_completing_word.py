from collections import Counter


# Time Complexity: O(P + N * L)
# Where P is the length of the license plate, N is the number of words, and L is the maximum length of a word in the array. Creating the initial Counter for the license plate takes O(P) time. For each word, creating its Counter takes O(L) time, and comparing the Counters takes O(1) time because they hold a maximum of 26 letters.
# Space Complexity: O(1) auxiliary space
# The Counter objects will store at most 26 key-value pairs (for the 26 letters of the English alphabet), which requires constant space.
def shortest_completing_word(license_plate, words):
    plate_count = Counter(c.lower() for c in license_plate if c.isalpha())

    shortest = None

    for word in words:
        if not (plate_count - Counter(word)):
            if shortest is None or len(word) < len(shortest):
                shortest = word
    return shortest


print(
    shortest_completing_word("1s3 PSt", ["step", "steps", "stripe", "stepple"])
)  # → "steps"
print(
    shortest_completing_word("1s3 456", ["looks", "pest", "stew", "show"])
)  # → "pest"

# Default LMS solution
# Same complexity

# def shortest_completing_word(licensePlate, words):
#     def count(itera):
#         ans = [0] * 26
#         for letter in itera:
#             ans[ord(letter) - ord('a')] += 1
#         return ans

#     def dominates(c1, c2):
#         return all(x1 >= x2 for x1, x2 in zip(c1, c2))

#     ans = None
#     target = count(c.lower() for c in licensePlate if c.isalpha())
#     for word in words:
#         if (ans is None or len(word) < len(ans)) and dominates(count(word.lower()), target):
#             ans = word

#     return ans
