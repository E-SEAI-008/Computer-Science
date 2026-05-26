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
