"""Step 5 reference solutions."""


def add_item(items, x):
    items.append(x)  # mutates the caller's list -- that is the point here
    return items  # returning it as well is a convenience, not a necessity


def second_largest(numbers):
    # set() throws away duplicates; sorted() turns it back into an ordered list.
    distinct = sorted(set(numbers))
    if len(distinct) < 2:
        return None  # nothing to be second
    return distinct[-2]  # second from the end


def flatten(pairs):
    flat = []
    for a, b in pairs:  # unpack each 2-tuple straight into two names
        flat.append(a)
        flat.append(b)
    return flat
    # `flat.extend((a, b))` would also work -- extend adds several items,
    # append adds exactly one.


def min_max(numbers):
    if not numbers:  # step 2's truthiness, guarding against an empty list
        return (None, None)
    return (min(numbers), max(numbers))


def rotate(items, k):
    if not items:  # avoids dividing by zero in the % below
        return []
    k = k % len(items)  # 4 % 3 == 1, so a full turn costs nothing
    return items[k:] + items[:k]  # both slices are new lists, so is the sum


def split_head_tail(items):
    if not items:
        return (None, [])
    head, *tail = items  # tail is always a list, even when empty
    return (head, tail)
