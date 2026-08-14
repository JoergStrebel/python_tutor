# Step 6 — Dictionaries and Sets

A list answers "what is at position 3?". A dictionary answers "what is stored
under this name?" — and answers it instantly, however large it gets. Sets answer
"have I seen this before?". Between them they solve a startling share of real
problems.

## Syntax card

```python
ages = {"ada": 36, "grace": 45}      # dict literal: key -> value
ages["ada"]                          # 36    -- raises KeyError if absent
ages.get("bob")                      # None  -- never raises
ages.get("bob", 0)                   # 0     -- your own default
ages["bob"] = 27                     # add or overwrite
del ages["bob"]                      # remove
"ada" in ages                        # membership tests the KEYS
len(ages)

for key in ages:                     # iterating a dict gives its KEYS
for key, value in ages.items():      # ...usually you want both
for value in ages.values():

seen = {"a", "b"}                    # set literal -- unordered, no duplicates
empty = set()                        # NOT {} -- that is an empty dict!
seen.add("c")
a | b     a & b     a - b            # union, intersection, difference
```

## What each piece does

**A dict maps keys to values.** Keys must be immutable — strings, numbers and
tuples work; lists do not. Values can be anything. Since Python 3.7 a dict keeps
its insertion order, so iterating one is predictable.

**`[]` versus `.get()` is a real decision.** `ages["bob"]` raises `KeyError` when
`bob` is absent. `ages.get("bob", 0)` returns your default instead. Use `[]` when
a missing key means your program is broken, and `.get()` when absence is normal.

**The counting idiom.** Worth memorising outright, because you will write it
constantly:

```python
counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1
```

Read it as: "whatever was there before, or 0 if nothing, plus one".

**`.items()` gives you pairs, which unpack.** This joins up with step 5:

```python
for name, age in ages.items():
    print(f"{name} is {age}")
```

**Sets discard duplicates and order.** `set([3, 1, 3, 2])` is `{1, 2, 3}` — three
items, and you cannot rely on the order. Membership testing (`x in s`) is
instant, which makes sets the right tool for "have I already seen this?".

The set operators read as English: `a | b` is "in either", `a & b` is "in both",
`a - b` is "in a but not b".

**The empty-set gotcha:** `{}` was already taken by dicts, so an empty set must
be written `set()`.

## Common errors you will hit

```
KeyError: 'bob'
```
You looked up a key that is not there. Use `.get(key, default)`, or guard with
`if key in d:`.

```
TypeError: unhashable type: 'list'
```
You tried to use a list as a dict key or put one in a set. Use a tuple instead —
`(1, 2)` is fine where `[1, 2]` is not.

```
TypeError: 'dict' object is not callable
```
You wrote `ages("ada")` with round brackets. Lookups use square brackets.

```
RuntimeError: dictionary changed size during iteration
```
You added or deleted keys inside a `for` loop over the same dict. Collect what
you want to change first, then apply it afterwards.

**Silent bug: iterating a dict gives keys, not values.** `for x in ages:` binds
`x` to `"ada"`, not `36`. Say `.values()` or `.items()` when you mean those.

## Do the drills

```bash
python3 step_06_dicts_sets/examples.py
pytest step_06_dicts_sets/
```

## Recall drill

Close this file and write from memory:

1. The three-line word-counting idiom.
2. A loop that prints `key: value` for every entry of a dict.
3. The expression for "the items that appear in both `a` and `b`", and how you
   write an empty set.
