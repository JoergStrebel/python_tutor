# Step 7 — Functions in Depth

You have been writing function *bodies* since step 1. Now you write the whole
thing: parameters, defaults, keyword arguments, and the scope rules that decide
which variables a function can see.

## Syntax card

```python
def name(a, b):                      # parameters a and b
    """One-line summary of what it does."""
    return a + b                     # a function with no return gives back None

def power(base, exp=2):              # exp has a DEFAULT -- callers may omit it
    return base ** exp

power(3)                             # 9    -- positional
power(3, 3)                          # 27   -- positional
power(base=3, exp=3)                 # 27   -- keyword: order stops mattering
power(exp=3, base=3)                 # 27   -- same call

def total(*nums):                    # *args: any number of positional arguments
    return sum(nums)                 #        nums arrives as a TUPLE

def describe(**kwargs):              # **kwargs: any number of keyword arguments
    return kwargs                    #           kwargs arrives as a DICT

f = power                            # a function is a value you can pass around
f(4)                                 # 16
```

## What each piece does

**`return` versus `print`.** A function that prints shows you something once. A
function that returns hands a value back so the rest of the program can use it.
Every drill in this tutorial returns, because returning is what makes code
composable — and testable. A function with no `return` returns `None`.

**Defaults make parameters optional.** `def power(base, exp=2)` means `exp` is 2
unless the caller says otherwise. Parameters with defaults must come after those
without.

**One default is a trap: never use a mutable default.**

```python
def add(item, target=[]):        # DANGER
    target.append(item)
    return target
```

The `[]` is created *once*, when the `def` line runs, not per call — so the list
survives between calls and grows forever. The fix is the standard idiom:

```python
def add(item, target=None):
    if target is None:
        target = []
    target.append(item)
    return target
```

`examples.py` demonstrates the bug live. It catches everyone once.

**Keyword arguments at the call site aid readability.** `make_greeting("Ada",
punct="?")` is clearer than `make_greeting("Ada", "Hello", "?")`, and lets you
skip over a middle default.

**`*args` collects extras into a tuple; `**kwargs` into a dict.** The names are
convention, not syntax — the `*` and `**` do the work. You will meet these
constantly when reading other people's code.

**Scope: a function's variables are private to that call.** Assigning inside a
function creates a *local* name, even if a global of that name exists. To keep
state across calls, the clean way is a closure with `nonlocal`:

```python
def make_counter():
    count = 0
    def step():
        nonlocal count       # "assign to the OUTER count, not a new local one"
        count += 1
        return count
    return step
```

Without `nonlocal`, `count += 1` would try to read a local `count` that has not
been assigned yet, and raise `UnboundLocalError`.

## Common errors you will hit

```
TypeError: power() missing 1 required positional argument: 'base'
```
You called it with too few arguments.

```
TypeError: power() takes from 1 to 2 positional arguments but 3 were given
```
Too many.

```
SyntaxError: parameter without a default follows parameter with a default
```
You wrote `def f(a=1, b)`. Put the defaulted parameters last.

```
UnboundLocalError: cannot access local variable 'count' where it is not
associated with a value
```
You assigned to a name inside a function that you also wanted to read from the
enclosing scope. Add `nonlocal` (or `global`).

**Silent bug: the function returns `None`.** You forgot `return`, or you indented
it inside a loop so it fired on the first pass.

## Do the drills

```bash
python3 step_07_functions/examples.py
pytest step_07_functions/
```

## Recall drill

Close this file and write from memory:

1. A function with one required and one defaulted parameter, plus two calls —
   one using the default and one overriding it by keyword.
2. The safe way to give a parameter an empty-list default.
3. A `make_counter()` closure that returns 1, 2, 3 on successive calls.
