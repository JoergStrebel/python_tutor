"""Step 1 drills -- variables, types, f-strings.

Replace each `raise NotImplementedError` with your own code. Do them one at a
time and run `pytest step_01_values/` after each one.

Keep the function names and signatures exactly as they are: the tests call them
by name.
"""


def greet(name):
    """Return a greeting, e.g. greet("Ada") -> "Hello, Ada!"

    Practise: f-string.
    """
    return f"Hello, {name}!"


def celsius_to_fahrenheit(c):
    """Return the temperature `c` (degrees Celsius) in degrees Fahrenheit.

    The formula is:  F = C * 9 / 5 + 32

    Practise: arithmetic, returning a number rather than printing it.
    """
    return c * 9/5 + 32


def describe_type(x):
    """Return the NAME of x's type as a string.

    describe_type(3)      -> "int"
    describe_type("hi")   -> "str"
    describe_type(2.5)    -> "float"
    describe_type(True)   -> "bool"
    """
    return type(x).__name__


def to_int(text):
    """Convert `text` to a whole number and return it.

    to_int("42")    -> 42
    to_int("  7  ") -> 7      (int() copes with surrounding spaces on its own)

    Practise: int() conversion.
    """
    return int(text)


def format_price(amount):
    """Return `amount` as a price string with exactly 2 decimal places.

    format_price(3.5)    -> "3.50 EUR"
    format_price(12)     -> "12.00 EUR"
    format_price(0.999)  -> "1.00 EUR"    (the format spec rounds for you)

    """
    return f"{amount:.2f} EUR"


def swap(a, b):
    """Return the two values in the opposite order, as a pair.

    swap(1, 2)         -> (2, 1)
    swap("x", "y")     -> ("y", "x")

    Practise: returning more than one value at once.
    """
    return b,a
