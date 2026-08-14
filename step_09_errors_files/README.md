# Step 9 — Errors and Files

Until now every crash has been your mistake. Files introduce failures that are
nobody's fault — the file is missing, the disk is full, the text is not a number.
Handling those is what separates a script from a program. The two topics belong
together because files are where you first meet them.

## Syntax card

```python
try:
    risky()
except ValueError:                   # catch one specific kind
    ...
except (TypeError, KeyError) as err: # catch several; `as` names the exception
    print(err)
else:                                # runs only if NO exception happened
    ...
finally:                             # always runs, exception or not
    ...

raise ValueError("message explaining what was wrong")

with open(path) as f:                # the file is closed for you, always
    text = f.read()                  # the whole file as one string
    lines = f.readlines()            # a list of lines, newlines included
    for line in f:                   # one line at a time -- best for big files

with open(path, "w") as f:           # "w" truncates, "a" appends, "r" is default
    f.write("hello\n")               # write does NOT add a newline for you

from pathlib import Path
Path("notes.txt").exists()
Path("notes.txt").read_text()
Path("notes.txt").write_text("hello\n")
```

## What each piece does

**Catch what you expect, not everything.** A bare `except:` swallows typos,
`KeyboardInterrupt` and genuine bugs along with the error you meant to handle,
and leaves you debugging in the dark. Name the exception:

```python
except ValueError:          # good -- you know what you are handling
except:                     # bad  -- hides your own mistakes
```

The exceptions you will actually catch: `ValueError` (bad conversion),
`KeyError` (missing dict key), `IndexError` (bad list index),
`ZeroDivisionError`, `FileNotFoundError`, `TypeError`.

**Keep the `try` block short.** Wrap only the line that can fail. A long `try`
catches errors from lines you never meant to guard.

**`else` and `finally` each have a job.** `else` holds the "it worked" path,
keeping it out of the `try` where it might raise a second, confusing error.
`finally` runs no matter what — even if you `return` from inside the `try` — so
it is where cleanup goes.

**`raise` is how *your* code reports a problem.** When a caller hands you
nonsense, raising is better than returning `None` and hoping they check:

```python
if n <= 0:
    raise ValueError(f"n must be positive, got {n}")
```

Include the offending value in the message. Future you will be grateful.

**`with open(...)` closes the file for you.** Even if an exception fires inside
the block. Always use it — the bare `open()` without `with` leaks file handles
and is the mark of code written before 2010.

**Write mode `"w"` destroys the existing file immediately**, before you write a
single byte. Use `"a"` to append.

**`f.write()` does not add a newline.** Unlike `print`. If you want lines, write
`"\n"` yourself.

**`pathlib` is the modern way to handle paths.** `Path("a") / "b" / "c.txt"`
builds a path with the right separator for the operating system, and
`.read_text()` / `.write_text()` handle the open-and-close in one call.

## Common errors you will hit

```
FileNotFoundError: [Errno 2] No such file or directory: 'notes.txt'
```
Wrong path, or the file genuinely is not there. Note that relative paths are
resolved from wherever you *ran* Python, not from where the script lives.

```
ValueError: invalid literal for int() with base 10: 'abc'
```
The step-1 error again — now with a way to handle it.

```
io.UnsupportedOperation: not writable
```
You opened for reading and then called `.write()`. Pass `"w"` or `"a"`.

**Silent bug: the file is empty afterwards.** You opened it with `"w"` when you
meant `"r"` or `"a"`, and truncated it.

**Silent bug: everything ends up on one line.** You forgot the `"\n"` in
`f.write()`.

## Do the drills

```bash
python3 step_09_errors_files/examples.py
pytest step_09_errors_files/
```

The file drills are tested using pytest's `tmp_path` fixture, so nothing is
written into your tutorial folder.

## Recall drill

Close this file and write from memory:

1. A `try`/`except` that turns `int(text)` into 0 when the text is not a number.
2. The three lines that read a file into a list of lines using `with`.
3. A `raise` statement rejecting a negative argument, with the value in the message.
