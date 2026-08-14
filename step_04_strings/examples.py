"""Step 4 examples -- run me with:  python3 step_04_strings/examples.py"""

s = "Python"

# --- Indexing ---------------------------------------------------------------

print(f"s          = {s!r}   (length {len(s)})")
print("  positions:  P  y  t  h  o  n")
print("  forwards:   0  1  2  3  4  5")
print("  backwards: -6 -5 -4 -3 -2 -1")
print()
print("s[0]  =", s[0], "  <- first")
print("s[5]  =", s[5], "  <- last, the hard way")
print("s[-1] =", s[-1], "  <- last, the good way")
print("s[-2] =", s[-2])
print()

# --- Slicing ----------------------------------------------------------------

print("s[1:4]   =", repr(s[1:4]), "  <- includes 1, excludes 4")
print("s[:3]    =", repr(s[:3]), "  <- from the start")
print("s[3:]    =", repr(s[3:]), "  <- to the end")
print("s[:]     =", repr(s[:]), " <- the whole thing (a copy)")
print("s[::2]   =", repr(s[::2]), "  <- every second character")
print("s[::-1]  =", repr(s[::-1]), " <- reversed")
print("s[1:-1]  =", repr(s[1:-1]), " <- drop first and last")
print()

# The two halves of any slice point always rejoin into the original.
n = 2
print(f"s[:{n}] + s[{n}:] == s  ->", s[:n] + s[n:] == s)

# Slices are forgiving where indexing is not.
print("s[10:20] =", repr(s[10:20]), "        <- no error, just empty")
print("s[10]    would raise IndexError")
print()

# --- Strings are immutable --------------------------------------------------

name = "ada"
name.upper()  # the result is computed and immediately thrown away
print(f"after a bare name.upper():   {name!r}   <- unchanged!")
name = name.upper()  # you must assign it
print(f"after name = name.upper():   {name!r}")
print()

# --- The methods you will use constantly ------------------------------------

messy = "   Hello, World!   "
print(f"{'original':<22}{messy!r}")
print(f"{'.strip()':<22}{messy.strip()!r}")
print(f"{'.lower()':<22}{messy.lower()!r}")
print(f"{'.replace(...)':<22}{messy.replace('World', 'Python')!r}")
print(f"{'.startswith(chained)':<22}{messy.strip().startswith('Hello')}")
print()

# --- split and join are inverses --------------------------------------------

line = "apple,pear,plum"
parts = line.split(",")
print(f"{line!r}.split(',')  -> {parts}")
print(f"'-'.join(parts)      -> {'-'.join(parts)!r}")
print()

# .split() with NO argument splits on any whitespace and drops the empties.
sentence = "  the   quick brown\tfox  "
print(f"{sentence!r}")
print("  .split(' ') ->", sentence.split(" "), "  <- note the empty strings")
print("  .split()    ->", sentence.split(), "        <- what you actually want")
print()

# --- Membership -------------------------------------------------------------

print('"th" in "Python"   ->', "th" in "Python")
print('"TH" in "Python"   ->', "TH" in "Python", "  <- case matters")
print('"TH" in "Python".upper() ->', "TH" in "Python".upper())
