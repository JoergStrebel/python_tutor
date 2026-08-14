"""Step 6 reference solutions."""


def count_words(text):
    counts = {}
    for word in text.lower().split():
        # "what was there before, or 0 if nothing, plus one"
        counts[word] = counts.get(word, 0) + 1
    return counts


def invert(d):
    flipped = {}
    for key, value in d.items():
        flipped[value] = key  # a later duplicate value simply overwrites
    return flipped


def safe_lookup(d, key, default=None):
    # .get() exists precisely for this. Note that passing `default` through
    # works even when it is None, since that is .get's own default anyway.
    return d.get(key, default)


def merge(a, b):
    merged = dict(a)  # a shallow copy -- `a` itself is left alone
    merged.update(b)  # b's entries overwrite on a clash
    return merged
    # Modern one-liner, same result:   return {**a, **b}


def unique_preserving_order(items):
    seen = set()  # fast membership test
    result = []  # remembers the order
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


def common_tags(a, b):
    # set(a) & set(b) is the intersection; sorted() turns it into a list with a
    # predictable order, since sets have no order of their own.
    return sorted(set(a) & set(b))
