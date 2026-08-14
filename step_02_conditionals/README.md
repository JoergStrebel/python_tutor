# Step 2 — Making Decisions: `if`, `elif`, `else`

A program that always does the same thing is a document. Branching is what makes
it a program. This step drills the decision syntax and, just as importantly,
*truthiness* — Python's rule for what counts as yes and no.

## Syntax card

```python
if condition:
    ...
elif other_condition:      # as many elif branches as you like, all optional
    ...
else:                      # optional, at most one
    ...

==   !=   <   <=   >   >=       # comparison -- these produce True or False
and   or   not                  # combining conditions
in                              # membership: "a" in "cat", 3 in [1, 2, 3]

value_if_true if condition else value_if_false     # conditional expression
```

## What each piece does

**The colon and the indentation are the block.** Python has no `{}` and no
`end`. The colon says "a block starts here" and the indentation says how far it
reaches. Four spaces is the convention; be consistent or Python will refuse to
run the file at all.

**`=` assigns, `==` compares.** `x = 5` puts 5 into `x`. `x == 5` asks a question
and answers `True` or `False`. Writing `if x = 5:` is a syntax error — which is
Python doing you a favour.

**`elif` is not the same as a second `if`.** In an `if/elif/elif` chain, Python
checks conditions top to bottom and stops at the first match. A run of separate
`if`s checks every one of them. This matters enormously for banded logic:

```python
# WRONG -- every branch runs, so a score of 95 ends up as "D"
if score >= 90: grade = "A"
if score >= 80: grade = "B"
if score >= 70: grade = "C"

# RIGHT -- stops at the first match, so 95 stays "A"
if score >= 90: grade = "A"
elif score >= 80: grade = "B"
elif score >= 70: grade = "C"
```

Order matters in such a chain: test the narrowest condition first.

**Truthiness: everything can be used as a condition.** You do not need
`if len(items) > 0:` — `if items:` says the same thing. Python treats these as
false:

```python
False   None   0   0.0   ""   []   {}   ()   set()
```

Everything else is true. So `if name:` means "if name is a non-empty string".
This idiom is everywhere in real Python code, which is why drill 6 makes you
type it.

**`and` / `or` short-circuit.** In `a and b`, if `a` is false Python never even
looks at `b`. That is what makes `if items and items[0] == "x":` safe on an
empty list.

## Common errors you will hit

```
IndentationError: expected an indented block after 'if' statement on line 3
```
You wrote `if x > 3:` and then put the next line flush against the left margin.
Everything belonging to the `if` must be indented.

```
TabError: inconsistent use of tabs and spaces in indentation
```
You mixed tab characters and spaces. Set your editor to insert spaces.

```
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
```
You wrote `if x = 5:`. Use `==`.

```
TypeError: '>' not supported between instances of 'str' and 'int'
```
You compared `"5" > 3`. Convert first — this is the step-1 lesson coming back.

## Do the drills

```bash
python3 step_02_conditionals/examples.py
pytest step_02_conditionals/
```

## Recall drill

Close this file and write from memory:

1. A function that returns `"positive"`, `"negative"` or `"zero"` for a number.
2. The list of every value Python considers false.
3. A single line that sets `label` to `"empty"` when `items` is empty and
   `"full"` otherwise (use a conditional expression).
