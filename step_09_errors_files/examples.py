"""Step 9 examples -- run me with:  python3 step_09_errors_files/examples.py

This file writes a couple of scratch files into a temporary directory and
cleans up after itself, so it will not litter your tutorial folder.
"""

import tempfile
from pathlib import Path

# --- Catching a specific exception ------------------------------------------

for text in ["42", "abc", ""]:
    try:
        number = int(text)
    except ValueError as err:
        print(f"int({text!r}) failed -> {type(err).__name__}: {err}")
    else:
        print(f"int({text!r}) worked -> {number}")
print()

# --- Several exception types ------------------------------------------------

data = {"a": 1}
for key in ["a", "z"]:
    try:
        print(f"data[{key!r}] = {data[key]}")
    except KeyError:
        print(f"data[{key!r}] -> no such key (KeyError)")
print()

# --- try / except / else / finally, in execution order ----------------------


def demo(divisor):
    print(f"demo({divisor}):")
    try:
        print("   try:     about to divide")
        result = 10 / divisor
    except ZeroDivisionError:
        print("   except:  cannot divide by zero")
        result = None
    else:
        print("   else:    no exception, result is", result)
    finally:
        print("   finally: this always runs")
    return result


demo(2)
demo(0)
print()

# --- Raising your own ------------------------------------------------------


def set_age(age):
    if age < 0:
        # Put the offending value in the message -- it saves debugging time.
        raise ValueError(f"age must not be negative, got {age}")
    return age


print("set_age(30) ->", set_age(30))
try:
    set_age(-5)
except ValueError as err:
    print("set_age(-5) raised ValueError:", err)
print()

# --- Files ------------------------------------------------------------------

with tempfile.TemporaryDirectory() as tmp:
    path = Path(tmp) / "notes.txt"

    # Writing. "w" creates the file, or truncates it if it already exists.
    with open(path, "w") as f:
        f.write("first line\n")  # the \n is YOUR job -- write does not add one
        f.write("second line\n")
    print(f"wrote {path.name}")

    # Reading the whole thing at once.
    with open(path) as f:  # "r" is the default mode
        whole = f.read()
    print("f.read() gave:", repr(whole))

    # Reading as a list of lines. Note the newlines are still attached.
    with open(path) as f:
        lines = f.readlines()
    print("f.readlines() gave:", lines)

    # Usually you want them stripped:
    with open(path) as f:
        clean = [line.rstrip("\n") for line in f]
    print("stripped         :", clean)

    # Appending rather than truncating.
    with open(path, "a") as f:
        f.write("third line\n")
    print("after 'a' mode   :", path.read_text().splitlines())

    # "w" destroys what was there, immediately.
    with open(path, "w") as f:
        f.write("only this\n")
    print("after 'w' mode   :", path.read_text().splitlines(), " <- the rest is gone")
    print()

    # --- pathlib shortcuts --------------------------------------------------

    other = Path(tmp) / "quick.txt"
    other.write_text("one\ntwo\n")  # open, write and close in one call
    print("read_text()      :", repr(other.read_text()))
    print("splitlines()     :", other.read_text().splitlines())
    print("exists()         :", other.exists())

    missing = Path(tmp) / "nope.txt"
    print("missing.exists() :", missing.exists())
    try:
        missing.read_text()
    except FileNotFoundError as err:
        print("reading it raised FileNotFoundError:", err)

print("\n(the temporary directory has now been deleted)")
