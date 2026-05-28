# Time Complexity: O(N * L)
# Where N is the total number of words and L is the maximum length of a word. Creating a set from each word takes O(L) time. Checking if it is a subset of the rows takes O(1) time because the size of the alphabet is constant (at most 26 characters).
# Space Complexity: O(1) auxiliary space
# The 'rows' sets and 'w_set' take up constant space because they will never store more than 26 characters. (Note: If you count the 'result' array used to return the matching words, the space complexity would be O(N * L) in the worst-case scenario).
def find_words(words):
    rows = [
        set("qwertyuiop"),
        set("asdfghjkl"),
        set("zxcvbnm"),
    ]

    result = []

    for word in words:
        w_set = set(word.lower())
        if any(w_set.issubset(row) for row in rows):
            result.append(word)
    return result


print(find_words(["Hello", "Alaska", "Dad", "Peace"]))  # ["Alaska", "Dad"]
print(find_words(["omk"]))  # []
print(find_words(["adsdf", "sfd"]))  # ["adsdf", "sfd"]
