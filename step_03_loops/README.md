# Step 3 — Repetition: `for` and `while`

Loops are where programs stop being calculators. Two forms cover almost
everything: `for` when you know what you are iterating over, `while` when you are
waiting for a condition to change.

## Syntax card

```python
for item in sequence:          # iterate over the items themselves
    ...

for i in range(5):             # 0 1 2 3 4      -- stop is EXCLUSIVE
for i in range(1, 6):          # 1 2 3 4 5      -- start, stop
for i in range(0, 10, 2):      # 0 2 4 6 8      -- start, stop, step
for i in range(5, 0, -1):      # 5 4 3 2 1      -- counting down

while condition:               # repeat as long as the condition holds
    ...

break        # leave the loop immediately
continue     # skip the rest of this pass, go to the next item
```

The accumulator pattern — the single most common loop shape in all of
programming:

```python
total = 0                      # 1. start with an empty answer
for n in numbers:              # 2. visit every item
    total = total + n          # 3. fold it into the answer
return total                   # 4. hand back the finished answer
```

## What each piece does

**`for` iterates over items, not indices.** Coming from other languages you may
reach for `for i in range(len(items)): items[i]`. Python wants
`for item in items:`. Only use `range(len(...))` when you genuinely need the
position — and step 8 will show you `enumerate`, which is better even then.

**`range` stops *before* its second argument.** `range(1, 6)` gives 1,2,3,4,5.
This feels wrong for about a week and then feels obviously right, because
`range(n)` produces exactly `n` items and `range(len(items))` covers exactly the
valid indices. To include the endpoint, write `range(1, n + 1)`.

**`while` needs you to change something.** A `for` loop ends on its own. A
`while` loop ends only when its condition turns false, so *something inside the
body must move towards that*. Forget the `n = n - 1` and the loop runs forever —
press `Ctrl+C` to stop it.

**`break` versus `continue`.** `break` abandons the whole loop; use it when you
have found what you were searching for. `continue` abandons only this one pass;
use it to skip items you do not care about.

**Build a list with `.append`.** Very common alongside the accumulator:

```python
result = []
for n in numbers:
    if n > 0:
        result.append(n)
```

Step 8 will compress exactly this into a one-line comprehension. Type the long
form enough times first that the short form feels like a relief rather than a
riddle.

## Common errors you will hit

```
TypeError: 'int' object is not iterable
```
You wrote `for i in 5:`. A bare number is not a sequence — you meant `range(5)`.

```
IndexError: list index out of range
```
Usually an off-by-one: `range(1, len(items) + 1)` where you wanted
`range(len(items))`.

**The loop never stops.** Your `while` condition never becomes false. Press
`Ctrl+C`, then check that the body actually changes the variable being tested.

**The result is always the last item.** You put `return` *inside* the loop when
it belonged after it, so the function exits on the first pass. Check your
indentation.

## Do the drills

```bash
python3 step_03_loops/examples.py
pytest step_03_loops/
```

## Recall drill

Close this file and write from memory:

1. The four lines of the accumulator pattern that sum a list.
2. A `range(...)` call producing `10 9 8 7 6`.
3. A loop that prints only the odd numbers from 1 to 20, using `continue`.
