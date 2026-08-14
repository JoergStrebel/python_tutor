"""Step 7 reference solutions."""


def power(base, exp=2):
    # ** is exponentiation. Anything to the power 0 is 1, which falls out free.
    return base**exp


def make_greeting(name, greeting="Hello", punct="!"):
    return f"{greeting}, {name}{punct}"


def total(*nums):
    # nums is a tuple, and sum() of an empty tuple is 0 -- so the empty case
    # needs no special handling.
    return sum(nums)


def describe(**kwargs):
    parts = []
    for key, value in sorted(kwargs.items()):  # sorted() orders by key
        parts.append(f"{key}={value}")
    return ", ".join(parts)  # "" when parts is empty -- exactly what we want


def apply_twice(fn, x):
    # fn is just a name holding a function. fn(x) calls it.
    return fn(fn(x))


def make_accumulator():
    running = 0  # lives in make_accumulator's scope, one per call of it

    def add(n):
        nonlocal running  # without this, `running += n` raises UnboundLocalError
        running += n
        return running

    return add  # the function OBJECT, not add() -- no parentheses
