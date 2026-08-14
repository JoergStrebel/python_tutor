"""Step 7 drills -- parameters, defaults, *args, **kwargs, scope."""


def power(base, exp=2):
    """Return `base` raised to the power `exp`, squaring by default.

    power(3)      -> 9
    power(2, 10)  -> 1024
    power(5, 0)   -> 1

    The signature is already written for you -- note where the default goes.
    Python's exponent operator is **.

    Practise: default parameter values.
    """
    raise NotImplementedError("drill 1: power")


def make_greeting(name, greeting="Hello", punct="!"):
    """Build a greeting from its three parts.

    make_greeting("Ada")                      -> "Hello, Ada!"
    make_greeting("Ada", "Hi")                -> "Hi, Ada!"
    make_greeting("Ada", punct="?")           -> "Hello, Ada?"
    make_greeting("Ada", "Yo", ".")           -> "Yo, Ada."

    Note the exact format: greeting, comma, space, name, punctuation.

    Practise: several defaults, and an f-string (step 1 again).
    """
    raise NotImplementedError("drill 2: make_greeting")


def total(*nums):
    """Add up however many numbers you are given.

    total(1, 2, 3)  -> 6
    total(5)        -> 5
    total()         -> 0

    Practise: *args. Inside the function, `nums` is a tuple.
    """
    raise NotImplementedError("drill 3: total")


def describe(**kwargs):
    """Render keyword arguments as "key=value" pairs, sorted by key.

    describe(size=3, colour="red")  -> "colour=red, size=3"
    describe(a=1)                   -> "a=1"
    describe()                      -> ""

    Pairs are joined by a comma and a space. Sorting keeps the result
    predictable regardless of the order they were passed in.

    Practise: **kwargs, .items(), sorted(), and ", ".join()
    """
    raise NotImplementedError("drill 4: describe")


def apply_twice(fn, x):
    """Apply the function `fn` to `x`, then apply it to the result.

    apply_twice(lambda n: n + 1, 5)     -> 7
    apply_twice(str.upper, "hi")        -> "HI"

    Practise: treating a function as an ordinary value you can call.
    """
    raise NotImplementedError("drill 5: apply_twice")


def make_accumulator():
    """Return a FUNCTION that keeps a running total across its calls.

        acc = make_accumulator()
        acc(10)   -> 10
        acc(5)    -> 15
        acc(1)    -> 16

        other = make_accumulator()
        other(3)  -> 3      (a fresh, independent total)

    Practise: a closure with `nonlocal`. Note you are returning the inner
    function itself -- write `return step`, not `return step()`.
    """
    raise NotImplementedError("drill 6: make_accumulator")
