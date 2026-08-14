"""Step 9 drills -- try/except, raise, reading and writing files."""


def parse_int(text, default=0):
    """Convert `text` to an int, returning `default` when that is impossible.

    parse_int("42")        -> 42
    parse_int("abc")       -> 0
    parse_int("abc", -1)   -> -1
    parse_int("")          -> 0

    Practise: try/except ValueError. Keep the try block down to the one line
    that can actually fail.
    """
    raise NotImplementedError("drill 1: parse_int")


def divide(a, b):
    """Return a / b, or None if b is zero.

    divide(10, 2)  -> 5.0
    divide(10, 0)  -> None

    Practise: catching ZeroDivisionError.
    """
    raise NotImplementedError("drill 2: divide")


def require_positive(n):
    """Return `n` if it is greater than zero, otherwise RAISE a ValueError.

    require_positive(5)   -> 5
    require_positive(0)   -> raises ValueError
    require_positive(-2)  -> raises ValueError

    The message must mention the offending value, so that
    str(the_exception) contains "-2" when called with -2.

    Practise: `raise ValueError(f"...")` -- reporting a problem rather than
    silently returning None.
    """
    raise NotImplementedError("drill 3: require_positive")


def read_lines(path):
    """Read a text file and return its lines WITHOUT their trailing newlines.

    For a file containing "a\\nb\\n", return ["a", "b"].
    For an empty file, return [].

    Practise: `with open(path) as f:` and stripping the newline off each line.
    """
    raise NotImplementedError("drill 4: read_lines")


def write_lines(path, lines):
    """Write each item of `lines` to `path` as its own line. Return the count.

        write_lines(p, ["a", "b"])   -> 2, and the file holds "a\\nb\\n"
        write_lines(p, [])           -> 0, and the file is empty

    An existing file at `path` is overwritten.

    Practise: `with open(path, "w") as f:` and remembering that f.write() does
    NOT add the newline for you.
    """
    raise NotImplementedError("drill 5: write_lines")


def count_lines(path):
    """Return the number of lines in the file, or 0 if the file does not exist.

    A missing file is a normal outcome here, not a crash.

    Practise: catching FileNotFoundError, and reusing your own read_lines.
    """
    raise NotImplementedError("drill 6: count_lines")
