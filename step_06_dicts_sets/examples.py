"""Step 6 examples -- run me with:  python3 step_06_dicts_sets/examples.py"""

# --- Building and reading a dict --------------------------------------------

ages = {"ada": 36, "grace": 45}
print("ages         =", ages)
print('ages["ada"]  =', ages["ada"])
print("len(ages)    =", len(ages))
print('"ada" in ages=', "ada" in ages, "  <- `in` tests the KEYS")
print()

ages["bob"] = 27  # add
ages["ada"] = 37  # overwrite -- same syntax
print("after adding bob and ageing ada:", ages)
del ages["bob"]
print("after del ages['bob']:          ", ages)
print()

# --- [] raises, .get() does not ---------------------------------------------

try:
    ages["bob"]
except KeyError as err:
    print("ages['bob'] raises KeyError:", err)

print("ages.get('bob')      ->", ages.get("bob"), "   <- None, no crash")
print("ages.get('bob', 0)   ->", ages.get("bob", 0), "      <- your own default")
print()

# --- The three ways to iterate ----------------------------------------------

print("for k in ages:")
for k in ages:
    print("   ", k, "   <- keys only")

print("for v in ages.values():")
for v in ages.values():
    print("   ", v)

print("for k, v in ages.items():")
for k, v in ages.items():  # each item is a (key, value) tuple, unpacked
    print(f"    {k} is {v}")
print()

# --- The counting idiom -- memorise this ------------------------------------

words = "the cat sat on the mat the end".split()
counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1
print("words :", words)
print("counts:", counts)
print()

# --- Sets -------------------------------------------------------------------

print("set([3, 1, 3, 2]) =", set([3, 1, 3, 2]), "  <- duplicates gone")
print("{} is a", type({}).__name__, "-- an EMPTY SET must be written set()")
print("set() is a", type(set()).__name__)
print()

a = {"python", "rust", "go"}
b = {"go", "java"}
print("a       =", a)
print("b       =", b)
print("a | b   =", a | b, "  <- union: in either")
print("a & b   =", a & b, "                       <- intersection: in both")
print("a - b   =", a - b, "        <- difference: in a but not b")
print()

# Sets are the tool for "have I seen this before?"
seen = set()
first_time = []
for item in ["a", "b", "a", "c", "b"]:
    if item not in seen:
        seen.add(item)
        first_time.append(item)
print("first sighting of each:", first_time)
print()

# --- Keys must be immutable -------------------------------------------------

good = {(1, 2): "a tuple key is fine"}
print("tuple key works:", good)
try:
    {[1, 2]: "nope"}
except TypeError as err:
    print("list key raises TypeError:", err)
