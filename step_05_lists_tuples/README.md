# Step 5 — Lists and Tuples

A list is an ordered, *changeable* collection. A tuple is an ordered,
*unchangeable* one. Slicing works exactly as it did on strings in step 4 — that
transfer is deliberate.

## Syntax card

```python
items = ["a", "b", "c"]        # list literal
point = (3, 4)                 # tuple literal -- the commas make it, not the ()

items[0]        items[-1]        items[1:3]       len(items)     # as for strings

items.append("d")              # add one item to the end       (changes items!)
items.insert(0, "z")           # add at a position
items.remove("b")              # delete by value
popped = items.pop()           # remove and return the last item
items.sort()                   # sort IN PLACE, returns None
best = sorted(items)           # returns a NEW sorted list

"a" in items                   # membership
items + other                  # concatenate into a new list
[0] * 3                        # -> [0, 0, 0]

x, y = point                   # unpacking: two names from a 2-tuple
first, *rest = items           # star-unpacking: "first" and "everything else"
```

## What each piece does

**Lists mutate; strings do not.** This is the big new idea of this step.
`items.append("d")` changes the list itself and returns `None`. Compare with
step 4, where `s.upper()` left `s` alone and returned a new string.

The practical consequence is a trap worth meeting deliberately:

```python
items.sort()                   # correct: sorts items where it stands
items = items.sort()           # WRONG: sort() returns None, so items is now None
```

The rule of thumb: a method that changes the object in place returns `None`.
When you want a new object instead, look for the function form —
`sorted(items)`, `reversed(items)`.

**A function can change a list you pass to it.** Because the function receives
the same list, not a copy:

```python
def add_one(lst):
    lst.append(1)      # the caller's list changes too

def add_one_safely(lst):
    return lst + [1]   # builds a new list, caller's is untouched
```

Both are legitimate; drill 1 makes you do the first on purpose so you can feel
the difference. To copy a list deliberately: `items[:]` or `list(items)`.

**Tuples are for fixed-size records.** `(3, 4)` is a point; `("Ada", 36)` is a
person. You cannot append to one, and that is the point — a tuple says "this
shape will not change". Functions returning two things return a tuple, which you
saw in step 1's `swap`.

Watch out for the one-item tuple: `(5)` is just the number 5 in brackets.
`(5,)` — with the trailing comma — is the tuple.

**Unpacking is everywhere in real Python.** `x, y = point` beats
`x = point[0]; y = point[1]`. The star form absorbs "all the rest" into a list:

```python
first, *rest = [1, 2, 3, 4]    # first = 1, rest = [2, 3, 4]
```

## Common errors you will hit

```
AttributeError: 'NoneType' object has no attribute 'append'
```
You wrote `items = items.sort()` (or `.append()`) earlier and clobbered your
list with `None`.

```
TypeError: 'tuple' object does not support item assignment
```
You tried `point[0] = 5`. Tuples are immutable — build a new one.

```
ValueError: not enough values to unpack (expected 2, got 1)
```
The left side of your unpacking has more names than the right side has items.

```
ValueError: list.remove(x): x not in list
```
`.remove()` needs the value to be present. Guard with `if x in items:` first.

**Silent bug: the caller's list changed unexpectedly.** You mutated an argument
when you meant to build a new list. Return `lst + [x]` instead of appending.

## Do the drills

```bash
python3 step_05_lists_tuples/examples.py
pytest step_05_lists_tuples/
```

## Recall drill

Close this file and write from memory:

1. The difference between `items.sort()` and `sorted(items)`, in one sentence each.
2. Three lines that build a list of the squares of 1 to 5 using `.append()`.
3. An unpacking line that splits `[10, 20, 30]` into `head = 10` and `tail = [20, 30]`.
