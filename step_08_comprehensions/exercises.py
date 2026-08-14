"""Step 8 drills -- comprehensions, enumerate, zip, sorted."""


def squares(n):
    """Return the squares of 1 to n, in order.

    squares(5)  -> [1, 4, 9, 16, 25]
    squares(0)  -> []

    Practise: a plain list comprehension over range(1, n + 1).
    """
    raise NotImplementedError("drill 1: squares")


def evens(numbers):
    """Return only the even numbers, in their original order.

    evens([1, 2, 3, 4])  -> [2, 4]
    evens([1, 3])        -> []

    Practise: a comprehension with an `if` filter. Compare it with your
    skip_negatives from step 3 -- same shape, a third of the lines.
    """
    raise NotImplementedError("drill 2: evens")


def lengths(words):
    """Map each word to its length.

    lengths(["fig", "apple"])  -> {"fig": 3, "apple": 5}
    lengths([])                -> {}

    Practise: a DICT comprehension -- {key_expr: value_expr for ...}
    """
    raise NotImplementedError("drill 3: lengths")


def numbered(items):
    """Number a list of items from 1, as strings.

    numbered(["apple", "pear"])  -> ["1. apple", "2. pear"]
    numbered([])                 -> []

    Note the exact format: number, dot, single space, item.

    Practise: enumerate(items, start=1) inside a comprehension.
    """
    raise NotImplementedError("drill 4: numbered")


def pair_up(a, b):
    """Pair the two sequences together element by element.

    pair_up([1, 2], ["x", "y"])  -> [(1, "x"), (2, "y")]
    pair_up([1, 2, 3], ["x"])    -> [(1, "x")]      (zip stops at the shortest)
    pair_up([], [])              -> []

    The result must be a LIST of tuples, so remember that zip is lazy.

    Practise: zip() and list().
    """
    raise NotImplementedError("drill 5: pair_up")


def sort_by_length(words):
    """Return the words sorted shortest first.

    sort_by_length(["banana", "fig", "date"])  -> ["fig", "date", "banana"]
    sort_by_length(["bb", "aa"])               -> ["bb", "aa"]

    That second case is not a typo: both words have length 2, and Python's sort
    is STABLE, so words of equal length keep the order they came in.

    The input list must not be modified -- use sorted(), not .sort().

    Practise: sorted(..., key=len)
    """
    raise NotImplementedError("drill 6: sort_by_length")
