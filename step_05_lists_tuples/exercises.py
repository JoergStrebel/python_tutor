"""Step 5 drills -- lists, tuples, mutation, unpacking."""


def add_item(items, x):
    """Append `x` to `items` IN PLACE, and also return the list.

    This drill is about mutation on purpose: after calling it, the caller's own
    list must have grown.

        shopping = ["milk"]
        add_item(shopping, "eggs")
        shopping                      -> ["milk", "eggs"]

    Practise: .append(), and noticing that the caller sees the change.
    """
    raise NotImplementedError("drill 1: add_item")


def second_largest(numbers):
    """Return the second largest DISTINCT value in `numbers`.

    second_largest([1, 5, 3])        -> 3
    second_largest([5, 5, 3])        -> 3    (5 twice still counts once)
    second_largest([7])              -> None (there is no second value)
    second_largest([])               -> None
    second_largest([2, 2, 2])        -> None (only one distinct value)

    Hint: sorted() gives you a new sorted list; you saw `set` briefly in step 2
    and will meet it properly in step 6 -- but you can also solve this with a
    plain loop.

    Practise: sorted(), indexing from the end, guarding against short lists.
    """
    raise NotImplementedError("drill 2: second_largest")


def flatten(pairs):
    """Turn a list of 2-tuples into one flat list.

    flatten([(1, 2), (3, 4)])  -> [1, 2, 3, 4]
    flatten([])                -> []

    Practise: unpacking inside a for loop -- `for a, b in pairs:`
    """
    raise NotImplementedError("drill 3: flatten")


def min_max(numbers):
    """Return the smallest and largest values as a tuple (smallest, largest).

    min_max([3, 1, 4])  -> (1, 4)
    min_max([7])        -> (7, 7)
    min_max([])         -> (None, None)

    Practise: returning a tuple; the built-ins min() and max().
    """
    raise NotImplementedError("drill 4: min_max")


def rotate(items, k):
    """Move the first `k` items to the end, and return the result as a NEW list.

    rotate([1, 2, 3, 4, 5], 2)  -> [3, 4, 5, 1, 2]
    rotate([1, 2, 3], 0)        -> [1, 2, 3]
    rotate([1, 2, 3], 4)        -> [2, 3, 1]   (4 is one full turn plus one)
    rotate([], 3)               -> []

    Hint: items[k:] + items[:k]. For k larger than the list, reduce it first
    with the remainder operator: k % len(items).

    Practise: slicing, list concatenation, and NOT modifying the input.
    """
    raise NotImplementedError("drill 5: rotate")


def split_head_tail(items):
    """Return a tuple (first_item, list_of_the_rest).

    split_head_tail([1, 2, 3])  -> (1, [2, 3])
    split_head_tail([9])        -> (9, [])
    split_head_tail([])         -> (None, [])

    Practise: star-unpacking -- `head, *tail = items`
    """
    raise NotImplementedError("drill 6: split_head_tail")
