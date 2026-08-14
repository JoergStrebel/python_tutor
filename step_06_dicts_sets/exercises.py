"""Step 6 drills -- dicts, sets, lookup and membership."""


def count_words(text):
    """Count how often each word appears in `text`, ignoring case.

    count_words("the cat the")  -> {"the": 2, "cat": 1}
    count_words("")             -> {}

    Split on whitespace (plain .split() from step 4 does the right thing).

    Practise: the counting idiom, counts[k] = counts.get(k, 0) + 1
    """
    raise NotImplementedError("drill 1: count_words")


def invert(d):
    """Return a new dict with keys and values swapped.

    invert({"a": 1, "b": 2})  -> {1: "a", 2: "b"}
    invert({})                -> {}

    If two keys share a value, the LAST one wins -- that falls out naturally,
    so you do not need to do anything special.

    Practise: iterating with .items() and building a new dict.
    """
    raise NotImplementedError("drill 2: invert")


def safe_lookup(d, key, default=None):
    """Return d[key] if the key is present, otherwise `default`.

    safe_lookup({"a": 1}, "a")        -> 1
    safe_lookup({"a": 1}, "z")        -> None
    safe_lookup({"a": 1}, "z", 0)     -> 0

    Practise: .get() with a default. This is a one-liner -- do NOT use
    try/except (that is step 9, and it is the wrong tool here).
    """
    raise NotImplementedError("drill 3: safe_lookup")


def merge(a, b):
    """Return a NEW dict with everything from `a` and `b`. On a clash, b wins.

    merge({"x": 1}, {"y": 2})           -> {"x": 1, "y": 2}
    merge({"x": 1}, {"x": 9})           -> {"x": 9}
    merge({}, {})                       -> {}

    Neither input dict may be modified.

    Practise: copying a dict and updating it -- or the newer  {**a, **b}  form.
    """
    raise NotImplementedError("drill 4: merge")


def unique_preserving_order(items):
    """Return a list of the items with duplicates removed, keeping first order.

    unique_preserving_order([3, 1, 3, 2, 1])  -> [3, 1, 2]
    unique_preserving_order([])               -> []

    Note: plain `list(set(items))` is NOT good enough -- a set loses the order.

    Practise: a set used as a "have I seen this?" memory, alongside a list.
    """
    raise NotImplementedError("drill 5: unique_preserving_order")


def common_tags(a, b):
    """Return the tags present in BOTH collections, as a sorted list.

    common_tags(["x", "y"], ["y", "z"])   -> ["y"]
    common_tags(["a"], ["b"])             -> []
    common_tags(["b", "a"], ["a", "b"])   -> ["a", "b"]   (sorted!)

    The inputs are lists and may contain duplicates; the output must not.

    Practise: set(), the & operator, and sorted() to get a predictable order.
    """
    raise NotImplementedError("drill 6: common_tags")
