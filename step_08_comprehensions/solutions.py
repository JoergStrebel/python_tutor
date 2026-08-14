"""Step 8 reference solutions."""


def squares(n):
    # range(1, n + 1) is empty when n < 1, so squares(0) gives [] for free.
    return [i * i for i in range(1, n + 1)]


def evens(numbers):
    # The `if` goes at the END, after the loop header.
    return [n for n in numbers if n % 2 == 0]


def lengths(words):
    # Braces plus a colon between the key and value expressions.
    return {word: len(word) for word in words}


def numbered(items):
    # enumerate yields (index, item) pairs, which unpack into two names right
    # in the comprehension's loop header.
    return [f"{i}. {item}" for i, item in enumerate(items, start=1)]


def pair_up(a, b):
    # zip is lazy -- it returns an iterator, so list() is needed to get a list.
    return list(zip(a, b))


def sort_by_length(words):
    # key=len calls len() on each word and sorts by those numbers. sorted()
    # returns a NEW list; words.sort() would modify the caller's list instead.
    return sorted(words, key=len)
