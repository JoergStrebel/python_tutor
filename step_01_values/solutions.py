"""Step 1 reference solutions.

Look here AFTER your own tests go green. The point of comparing is not "was I
right" -- the tests already told you that -- but "was there a shorter way to say
it".
"""


def greet(name):
    # The f-string does the joining. Note there is no `+` and no str() call.
    return f"Hello, {name}!"


def celsius_to_fahrenheit(c):
    # `/` always produces a float in Python 3, so 100 -> 212.0 rather than 212.
    # That is fine: 212.0 == 212 is True.
    return c * 9 / 5 + 32


def describe_type(x):
    # type(x) gives the type object itself, e.g. <class 'int'>.
    # .__name__ pulls out just the readable name, "int".
    return type(x).__name__


def to_int(text):
    # int() strips surrounding whitespace itself, so no .strip() is needed.
    return int(text)


def format_price(amount):
    # :.2f  ->  fixed-point notation, exactly 2 digits after the decimal point.
    # It rounds rather than truncates, so 0.999 becomes "1.00".
    return f"{amount:.2f} EUR"


def swap(a, b):
    # Writing two values separated by a comma builds a tuple -- the parentheses
    # are optional. `return b, a` and `return (b, a)` are the same thing.
    return b, a
