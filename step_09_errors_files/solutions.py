"""Step 9 reference solutions."""


def parse_int(text, default=0):
    try:
        return int(text)  # only the line that can fail is inside the try
    except ValueError:
        return default


def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None
    # An `if b == 0: return None` guard would work equally well here. Catching
    # is the better habit when the check is harder than a comparison.


def require_positive(n):
    if n <= 0:
        # The f-string puts the offending value into the message, which is what
        # makes the traceback useful when this fires in real code.
        raise ValueError(f"expected a positive number, got {n}")
    return n


def read_lines(path):
    with open(path) as f:
        # Iterating the file gives one line at a time, each still carrying its
        # "\n". rstrip("\n") removes only that, leaving other whitespace alone.
        return [line.rstrip("\n") for line in f]


def write_lines(path, lines):
    with open(path, "w") as f:
        for line in lines:
            f.write(line + "\n")  # write() adds nothing -- the \n is ours
    return len(lines)


def count_lines(path):
    try:
        return len(read_lines(path))  # reuse the function above
    except FileNotFoundError:
        return 0
