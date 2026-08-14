# Python Syntax Cheatsheet — the ten step cards, plus the errors

**How to use this page:** before each new step, drill the previous step's card:

```bash
python3 quiz.py 3          # the number of the card, 1 to 11
```

The quiz names the thing you are trying to do, one idiom at a time, and you
write how you do it. Then it shows you the card and you say whether you had it.
Two minutes a day, and the syntax stops being something you look up.

Working on paper instead? Pick a card and re-type it from memory into a scratch
file, then check it against this page.

This is a *recall* aid, not a reference manual. It contains only what the
tutorial drills. The quiz's questions live in `quiz_bank.py` and are checked
against this page by `test_quiz.py` — if you edit a card here, run that test.

---

## 1 — Values, variables, f-strings

```python
name = "Ada"              # str
age = 36                  # int
height = 1.72             # float
is_student = True         # bool -- capitalised

f"Hello, {name}!"         # f-string: expression inside {}
f"{height:.2f}"           # 2 decimal places
f"{age + 1}"              # any expression works

int("42")     float("3.5")     str(42)
type(age).__name__        # -> "int"
a, b = b, a               # swap, no temporary
```

## 2 — Conditionals

```python
if condition:
    ...
elif other:               # checked only if the ones above failed
    ...
else:
    ...

==  !=  <  <=  >  >=      and  or  not      in

x = "one" if n == 1 else "many"      # conditional expression
```

Falsy values — everything else is true:

```python
False   None   0   0.0   ""   []   {}   ()   set()
```

## 3 — Loops

```python
for item in sequence:
for i in range(5):            # 0 1 2 3 4  -- stop is EXCLUSIVE
for i in range(1, 6):         # 1 2 3 4 5
for i in range(0, 10, 2):     # 0 2 4 6 8
for i in range(5, 0, -1):     # 5 4 3 2 1

while condition:
    ...                       # something here must change the condition

break        # leave the loop
continue     # skip to the next item
```

The accumulator — the shape behind half of all loops:

```python
total = 0
for n in numbers:
    total += n
return total
```

## 4 — Strings

```python
s[0]     s[-1]     s[1:4]     s[:3]     s[3:]     s[::-1]     len(s)

s.lower()   s.upper()   s.strip()   s.capitalize()
s.split(",")            s.split()            # .split() splits on any whitespace
",".join(parts)                              # the inverse of split
s.replace(old, new)     s.startswith(p)      "th" in s
```

Strings are **immutable** — `s.upper()` returns a new string, it does not change `s`.

## 5 — Lists and tuples

```python
items = ["a", "b"]        # list -- changeable
point = (3, 4)            # tuple -- fixed. The COMMA makes it: (5,) not (5)

items.append(x)     items.insert(i, x)     items.remove(value)     items.pop()
items.sort()              # in place, returns None
sorted(items)             # a NEW list

items[:]  or  list(items) # copy
items + other             # concatenate
[0] * 3                   # -> [0, 0, 0]

x, y = point              # unpacking
head, *tail = items       # star-unpacking
```

In-place methods return `None` — `items = items.sort()` destroys your list.

## 6 — Dicts and sets

```python
ages = {"ada": 36}
ages["ada"]               # KeyError if absent
ages.get("bob", 0)        # your default instead
ages["bob"] = 27          del ages["bob"]          "ada" in ages

for k in ages:            # KEYS
for k, v in ages.items()  # pairs
for v in ages.values()

seen = {"a", "b"}         empty = set()        # NOT {} -- that is a dict
seen.add(x)
a | b        a & b        a - b                # union, intersection, difference
```

The counting idiom:

```python
counts[word] = counts.get(word, 0) + 1
```

## 7 — Functions

```python
def power(base, exp=2):   # defaults come last
    """Docstring."""
    return base ** exp

power(3)          power(3, 3)         power(base=3, exp=3)

def total(*nums):         # extra positionals -> a TUPLE
def describe(**kwargs):   # extra keywords    -> a DICT

f = power                 # a function is a value; f(4) calls it
```

Never use a mutable default:

```python
def add(item, target=None):
    if target is None:
        target = []
```

Closure with state:

```python
def make_counter():
    count = 0
    def step():
        nonlocal count
        count += 1
        return count
    return step
```

## 8 — Comprehensions and friends

```python
[expr for item in seq]
[expr for item in seq if condition]
{k: v for item in seq}                  # dict
{expr for item in seq}                  # set
(expr for item in seq)                  # lazy generator

enumerate(seq)          enumerate(seq, start=1)
zip(a, b)                               # stops at the shortest
sorted(seq, key=len, reverse=True)
sorted(d.items(), key=lambda kv: kv[1])
lambda x: x * 2
```

`zip` and `enumerate` are lazy — wrap in `list(...)` when you need a list.

## 9 — Errors and files

```python
try:
    risky()
except ValueError as err:      # name what you expect; never a bare except:
    ...
else:                          # ran without an exception
    ...
finally:                       # always
    ...

raise ValueError(f"expected a positive number, got {n}")

with open(path) as f:          # closes itself, even on an exception
    text = f.read()
    lines = [line.rstrip("\n") for line in f]

with open(path, "w") as f:     # "w" truncates, "a" appends
    f.write(line + "\n")       # write() adds no newline

from pathlib import Path
Path("f.txt").exists()   .read_text()   .write_text(s)
```

Common ones to catch: `ValueError`, `KeyError`, `IndexError`,
`ZeroDivisionError`, `FileNotFoundError`, `TypeError`.

## 10 — Classes

```python
class Rectangle:
    def __init__(self, width, height):     # runs on Rectangle(...)
        self.width = width                 # self.x makes an attribute
        self.height = height

    def area(self):                        # every method takes self first
        return self.width * self.height

    def __repr__(self):                    # how it prints
        return f"Rectangle(width={self.width}, height={self.height})"

r = Rectangle(3, 4)
r.width          # attribute, no ()
r.area()         # method, needs ()

from dataclasses import dataclass

@dataclass                                 # __init__, __repr__, __eq__ for free
class Point:
    x: int
    y: int
```

`__len__` makes `len(obj)` work; `__eq__` makes `==` work.

---

## 11 — Errors worth recognising on sight

| Message | What you did |
|---|---|
| `NameError: name 'x' is not defined` | Typo, or used before assigning |
| `TypeError: can only concatenate str (not "int") to str` | `"a" + 1` — use an f-string |
| `IndentationError: expected an indented block` | Forgot to indent after a `:` |
| `IndexError: list index out of range` | Off-by-one; `len(x)` is one past the end |
| `KeyError: 'bob'` | Missing dict key — use `.get()` |
| `ValueError: invalid literal for int()` | `int("abc")` |
| `AttributeError: 'NoneType' object has no attribute ...` | You assigned the result of an in-place method |
| `UnboundLocalError` | Assigned to a name you also read from an outer scope — needs `nonlocal` |
| `TypeError: 'zip' object is not subscriptable` | It is lazy — wrap in `list()` |
| `FileNotFoundError` | Wrong path, or relative to the wrong directory |

**Read tracebacks from the bottom up.** The last line says what went wrong; the
lines above say how you got there.
