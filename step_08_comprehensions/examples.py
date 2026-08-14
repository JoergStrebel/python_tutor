"""Step 8 examples -- run me with:  python3 step_08_comprehensions/examples.py"""

numbers = [1, 2, 3, 4, 5, 6]

# --- The same job, three lines and one line ---------------------------------

doubled_long = []
for n in numbers:
    doubled_long.append(n * 2)

doubled_short = [n * 2 for n in numbers]

print("the loop version   :", doubled_long)
print("the comprehension  :", doubled_short)
print("identical?         :", doubled_long == doubled_short)
print()

# --- Adding a filter --------------------------------------------------------

evens_long = []
for n in numbers:
    if n % 2 == 0:
        evens_long.append(n)

evens_short = [n for n in numbers if n % 2 == 0]

print("filter, the long way :", evens_long)
print("filter, the short way:", evens_short)
print()

print("  [ n * 2      for n in numbers      if n > 3 ]")
print("    ^collect      ^loop header         ^filter")
print("  ->", [n * 2 for n in numbers if n > 3])
print()

# --- The other three brackets -----------------------------------------------

words = ["apple", "fig", "cherry"]
print("list comp :", [w.upper() for w in words])
print("dict comp :", {w: len(w) for w in words})
print("set comp  :", {len(w) for w in words}, "  <- duplicates collapse")

lazy = (w.upper() for w in words)
print("generator :", lazy, "  <- nothing computed yet")
print("            ", list(lazy), "  <- list() runs it")
print()

# --- enumerate --------------------------------------------------------------

print("without enumerate (clumsy):")
for i in range(len(words)):
    print(f"   {i + 1}. {words[i]}")

print("with enumerate:")
for i, word in enumerate(words, start=1):
    print(f"   {i}. {word}")

print("list(enumerate(words)) =", list(enumerate(words)))
print()

# --- zip --------------------------------------------------------------------

names = ["ada", "grace", "alan"]
scores = [95, 88, 91]

for name, score in zip(names, scores):
    print(f"   {name}: {score}")

print("dict(zip(names, scores)) =", dict(zip(names, scores)))

short = [1, 2]
print("zip stops at the shortest:", list(zip(names, short)), " <- alan is lost")
print()

# --- sorted -----------------------------------------------------------------

mixed = ["banana", "fig", "cherry", "date"]
print("sorted()               :", sorted(mixed))
print("sorted(reverse=True)   :", sorted(mixed, reverse=True))
print("sorted(key=len)        :", sorted(mixed, key=len))
print()

# key= with a lambda, on pairs
pairs = [("ada", 95), ("grace", 88), ("alan", 91)]
print("pairs                      :", pairs)
print("sorted by score            :", sorted(pairs, key=lambda p: p[1]))
print("sorted by score, descending:", sorted(pairs, key=lambda p: p[1], reverse=True))
print()

# Sorting a dict by its values -- an extremely common recipe.
counts = {"the": 5, "cat": 2, "sat": 9}
print("counts             :", counts)
print("by count, descending:", sorted(counts.items(), key=lambda kv: kv[1], reverse=True))
print()

# Stability: equal keys keep their original order.
same_length = ["bb", "aa", "cc"]
print(f"sorted({same_length}, key=len) -> {sorted(same_length, key=len)}")
print("   all length 2, so the original order survives")
print()

# --- lambda is just a short def ---------------------------------------------


def double(x):
    return x * 2


anonymous = lambda x: x * 2  # noqa: E731 -- shown for comparison only
print("double(5)    =", double(5))
print("anonymous(5) =", anonymous(5), "  <- same thing, no name")
