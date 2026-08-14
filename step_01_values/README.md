# Step 1 — Values, Variables and f-strings

Everything in Python is a *value*: a number, a piece of text, a truth value. A
*variable* is just a name pointing at a value. This step drills the four types you
will touch every single day and the one string-formatting syntax worth memorising.

## Syntax card

Re-type this from memory before you start the drills.

```python
name = "Ada"              # str   -- text, in single or double quotes
age = 36                  # int   -- whole number
height = 1.72             # float -- number with a decimal point
is_student = True         # bool  -- True or False (capitalised!)

f"Hello, {name}!"         # f-string: put an expression inside {}
f"{height:.2f}"           # format spec: 2 digits after the decimal point
f"{age + 1}"              # any expression works inside the braces

int("42")                 # convert str -> int
float("3.5")              # convert str -> float
str(42)                   # convert int -> str
type(age).__name__        # the name of a value's type, as a string: "int"
```

## What each piece does

**Assignment (`=`) is not equality.** `age = 36` means "make the name `age` point
at the value `36`". You are not stating a fact; you are giving an order. Comparing
for equality is `==`, which arrives in step 2.

**You never declare a type.** Python works out that `36` is an `int` on its own.
The type still matters enormously — `"3" + "4"` is `"34"` while `3 + 4` is `7` —
but you never write the type down. This is why `type(x)` is a useful debugging
tool: it answers "what have I actually got here?"

**f-strings are the way to build text.** The `f` before the opening quote turns
`{...}` into "evaluate this and paste the result in". You will type this hundreds
of times, so get it into your fingers now:

```python
f"{count} items cost {price:.2f} EUR"
```

The `:.2f` after the colon is a *format spec*: `f` means fixed-point, `.2` means
two digits after the point. `f"{1/3:.2f}"` gives `"0.33"`. Without it you would
get `0.3333333333333333`.

**Conversion is explicit.** `input()` always hands you a `str`, even when the user
typed a number. `int("42")` converts it. Forgetting this conversion is the single
most common beginner bug.

## Common errors you will hit

```
TypeError: can only concatenate str (not "int") to str
```
You wrote `"Age: " + age` where `age` is an `int`. Python refuses to guess.
Fix: `f"Age: {age}"` — or `"Age: " + str(age)`, but prefer the f-string.

```
ValueError: invalid literal for int() with base 10: 'twelve'
```
You called `int()` on text that is not a number. The string `" 42 "` *does* work
(`int` tolerates surrounding whitespace), but `"twelve"` never will.

```
NameError: name 'nmae' is not defined
```
A typo in a variable name. Python has no idea what you meant; read the name in the
message character by character.

## Do the drills

```bash
python3 step_01_values/examples.py      # 1. read the worked examples
                                        # 2. fill in exercises.py
pytest step_01_values/                  # 3. until green
```

## Recall drill

Close this file and write from memory:

1. A line that stores your name, and a line that prints `Hello, <name>!` using an f-string.
2. An f-string that shows the number `2/3` with exactly three decimal places.
3. Two lines that turn the text `"17"` into a number and then add 3 to it.
