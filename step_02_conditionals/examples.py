"""Step 2 examples -- run me with:  python3 step_02_conditionals/examples.py"""

# --- The basic shape --------------------------------------------------------

temperature = -3

if temperature > 30:
    print("It is hot.")
elif temperature > 20:
    print("It is pleasant.")
elif temperature > 10:
    print("Bring a jacket.")
else:
    print("It is cold.")
print()

# --- elif vs. a run of separate ifs -----------------------------------------

score = 75

# A chain: stops at the first match.
if score >= 90:
    chained = "A"
elif score >= 80:
    chained = "B"
elif score >= 70:
    chained = "C"

# Separate ifs: EVERY true branch runs, so the last one wins.
if score >= 90:
    separate = "A"
if score >= 80:
    separate = "B"
if score >= 70:
    separate = "C"

print(f"score {score} with elif chain    -> {chained}")
if chained != separate:
    print(f"score {score} with separate ifs  -> {separate}   <-- the classic bug")
else:
    print(f"score {score} with separate ifs  matches  {separate}   <-- correct category by chance")
print()

# --- Comparisons produce real values ----------------------------------------

print("3 > 2      =", 3 > 2)
print("3 == 3.0   =", 3 == 3.0)  # int and float compare by value
print("'a' == 'A' =", "a" == "A")  # comparison is case sensitive
print("2 < 5 < 9  =", 2 < 5 < 9)  # chained -- reads like maths, and works
print()

# --- Truthiness -------------------------------------------------------------

print("Values Python considers FALSE:")
for value in [False, None, 0, 0.0, "", [], {}, ()]:
    # bool(x) shows you exactly how `if x:` would treat x.
    print(f"  {value!r:<8} -> bool() is {bool(value)}")

print("\nValues Python considers TRUE:")
for value in [True, 1, -1, 0.1, "no", " ", [0], {"a": 1}]:
    print(f"  {value!r:<8} -> bool() is {bool(value)}")
print()

items = []
# Idiomatic:
if not items:
    print("`if not items:` -- the Pythonic way to say 'the list is empty'")
# Also correct, but wordier -- you will see both, prefer the first:
if len(items) == 0:
    print("`if len(items) == 0:` -- same result, more typing")
print()

# --- and / or / not ---------------------------------------------------------

age, has_ticket = 20, True
print("age >= 18 and has_ticket =", age >= 18 and has_ticket)
print("age < 18 or has_ticket   =", age < 18 or has_ticket)
print("not has_ticket           =", not has_ticket)

# Short-circuiting: the second half is never evaluated when the first settles it.
names = []
if names and names[0] == "Ada":  # names[0] would raise IndexError on its own!
    print("first name is Ada")
elif names and names[0] != "Ada":
    print("first name is not Ada")
else:
    print("`names and names[0]` did not crash -- `and` stopped at the empty list")
print()

# --- Conditional expression (the one-line if) -------------------------------

count = 1
label = "item" if count == 1 else "items"
print(f"{count} {label}")

count = 7
label = "item" if count == 1 else "items"
print(f"{count} {label}")
