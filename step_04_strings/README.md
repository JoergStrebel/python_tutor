# Step 4 — Strings: Indexing, Slicing, Methods

Text is the data you handle most. This step drills two things: the *slice*
notation `[a:b]`, which you will later reuse unchanged on lists, and the handful
of string methods that cover most real work.

## Syntax card

```python
s = "Python"

s[0]        # "P"     -- first character (counting starts at 0)
s[-1]       # "n"     -- last character (negative counts from the end)
s[1:4]      # "yth"   -- from 1 up to but NOT including 4
s[:3]       # "Pyt"   -- from the start
s[3:]       # "hon"   -- to the end
s[::-1]     # "nohtyP" -- step of -1: reversed
len(s)      # 6

s.lower()   s.upper()   s.strip()          # clean up
s.split(",")            # "a,b" -> ["a", "b"];  .split() alone splits on spaces
",".join(["a", "b"])    # -> "a,b"          -- the inverse of split
s.replace("y", "i")     # -> "Pithon"
s.startswith("Py")      s.endswith("on")
"th" in s               # True -- substring test
```

## What each piece does

**Indexing starts at 0, so the last index is `len(s) - 1`.** Rather than
computing that, use `s[-1]`. Negative indices count backwards from the end:
`s[-1]` last, `s[-2]` second to last.

**A slice `[start:stop]` includes `start` and excludes `stop`.** Same rule as
`range` in step 3 — and for the same reason: it makes `s[:n] + s[n:] == s` true
for every `n`, and makes the length of a slice simply `stop - start`. Omitting
either end means "as far as you can go", so `s[:]` is a full copy.

**Slices never raise `IndexError`.** `"abc"[10:20]` quietly gives `""`, whereas
`"abc"[10]` crashes. Slicing is the forgiving operation.

**Strings are immutable.** `s.upper()` does *not* change `s`; it returns a new
string. This trips up every beginner:

```python
name = "ada"
name.upper()          # this line achieves nothing -- the result is thrown away
print(name)           # still "ada"

name = name.upper()   # THIS is how you keep it
```

The same applies to `.strip()`, `.replace()` and friends. If a string method's
result is not assigned or returned, you have wasted the call.

**`split` and `join` are a matched pair.** `split` cuts text into a list; `join`
glues a list back into text. Note the odd-looking direction of `join` — you call
it *on the separator*: `", ".join(words)`. It reads backwards at first and
becomes second nature quickly.

`.split()` with no argument is special: it splits on any run of whitespace and
discards empties, which is exactly what you want for splitting a sentence into
words.

## Common errors you will hit

```
TypeError: 'str' object does not support item assignment
```
You wrote `s[0] = "X"`. Strings cannot be modified. Build a new one:
`s = "X" + s[1:]`.

```
IndexError: string index out of range
```
You indexed past the end — often `s[len(s)]`, which is one too far. Use
`s[len(s) - 1]` or, better, `s[-1]`.

```
TypeError: sequence item 0: expected str instance, int found
```
You called `",".join([1, 2, 3])`. `join` needs strings — convert first.

**The change did not stick.** You called `s.strip()` without assigning the
result. See the immutability note above.

## Do the drills

```bash
python3 step_04_strings/examples.py
pytest step_04_strings/
```

## Recall drill

Close this file and write from memory:

1. The slice that reverses a string.
2. Two lines that turn `"a, b, c"` into `["a", "b", "c"]` with no stray spaces.
3. The slice expressions for "everything except the first character" and
   "everything except the last character".
