# Step 8 — Comprehensions, `enumerate`, `zip`, `sorted`

In step 3 you wrote this shape over and over:

```python
result = []
for n in numbers:
    result.append(n * 2)
```

A comprehension says the same thing in one line. This step drills that
compression, plus the three built-ins that remove the remaining boilerplate from
loops. Together they are what makes Python code look like Python.

## Syntax card

```python
[expr for item in seq]                  # list comprehension
[expr for item in seq if condition]     # ...with a filter
{k_expr: v_expr for item in seq}        # dict comprehension
{expr for item in seq}                  # set comprehension
(expr for item in seq)                  # generator -- lazy, no list built

enumerate(seq)                # (0, first), (1, second), ...
enumerate(seq, start=1)       # (1, first), (2, second), ...
zip(a, b)                     # (a[0], b[0]), (a[1], b[1]), ... stops at shortest

sorted(seq)                   # a new sorted list
sorted(seq, reverse=True)     # descending
sorted(seq, key=len)          # sort by a computed value
sorted(d.items(), key=lambda pair: pair[1])   # sort a dict by its values

lambda x: x * 2               # a small unnamed function, for key= and friends
```

## What each piece does

**Read a comprehension middle-first.** `[n * 2 for n in numbers if n > 0]` is
the loop you already know, rearranged:

```
[  n * 2      for n in numbers      if n > 0  ]
   ^what to      ^the loop            ^the filter
    collect       header               (optional)
```

The order on the page is *result, loop, condition*; the order of execution is
*loop, condition, result*. Once you see the correspondence to the three-line
version, they stop being cryptic.

**Use one when it stays readable.** A comprehension is right for "transform
and/or filter a sequence". If you need two nested loops plus branching, or the
line no longer fits comfortably, write the explicit loop. Clever is not the goal.

**`enumerate` gives you the index without `range(len(...))`.**

```python
for i, item in enumerate(items, start=1):    # 1-based numbering, free
```

That `start=1` argument saves an awful lot of `i + 1`.

**`zip` walks two sequences in step.** It stops at the shorter one, silently — so
mismatched lengths lose data rather than raising. `dict(zip(keys, values))` is a
neat way to build a dict from two lists.

**`sorted(key=...)` sorts by a computed value.** The `key` function is called
once per item and the results are compared. `key=len` sorts by length,
`key=str.lower` sorts case-insensitively, `key=lambda p: p[1]` sorts pairs by
their second element.

Python's sort is *stable*: items that compare equal keep their original relative
order. That is why `sort_by_length` in drill 6 has a predictable answer even when
two words are the same length.

**`lambda` is just a compact `def`.** `lambda x: x * 2` and

```python
def double(x):
    return x * 2
```

are the same thing, except the lambda has no name and must be a single
expression. Use it for throwaway `key=` functions; use `def` for anything you
would want to name or test.

## Common errors you will hit

```
SyntaxError: invalid syntax
```
Often a comprehension with the parts in the wrong order — the expression comes
*first*, before the `for`.

```
TypeError: 'generator' object is not subscriptable
```
You used `(...)` instead of `[...]` and got a lazy generator. Wrap it in
`list(...)`, or use square brackets.

```
TypeError: 'zip' object is not subscriptable
```
Same family: `zip` and `enumerate` return lazy iterators. They are perfect in a
`for` loop; call `list(...)` when you want an actual list.

```
TypeError: '<' not supported between instances of 'str' and 'int'
```
You sorted a list mixing text and numbers. Give `sorted` a `key` that makes them
comparable.

**Silent bug: `zip` truncated your data.** The result is only as long as the
shortest input.

## Do the drills

```bash
python3 step_08_comprehensions/examples.py
pytest step_08_comprehensions/
```

## Recall drill

Close this file and write from memory:

1. A comprehension for the squares of 1 to 10, and one for the even squares only.
2. A loop that prints `1. apple`, `2. pear` from a list, using `enumerate`.
3. The call that sorts a list of `(name, score)` pairs by score, highest first.
