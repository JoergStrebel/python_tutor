"""Step 5 examples -- run me with:  python3 step_05_lists_tuples/examples.py"""

# --- Lists behave like strings for indexing and slicing ---------------------

items = ["a", "b", "c", "d", "e"]
print("items    =", items)
print("items[0] =", items[0])
print("items[-1]=", items[-1])
print("items[1:3] =", items[1:3], "  <- same slice rule as strings")
print("items[::-1]=", items[::-1])
print("len(items)=", len(items))
print()

# --- ...but unlike strings, lists can be changed ----------------------------

nums = [3, 1, 2]
print("start:            ", nums)
nums.append(4)
print("after .append(4): ", nums)
nums.insert(0, 0)
print("after .insert(0,0):", nums)
nums.remove(1)
print("after .remove(1): ", nums, "  <- removes the VALUE 1, not index 1")
last = nums.pop()
print(f"after .pop():      {nums}   (it returned {last})")
print()

# --- The None trap ----------------------------------------------------------

a = [3, 1, 2]
a.sort()  # correct: sorts in place
print("a.sort() then a       ->", a)

b = [3, 1, 2]
b = b.sort()  # WRONG: sort() returns None
print("b = b.sort() then b   ->", b, "  <-- your list is gone!")

c = [3, 1, 2]
c_sorted = sorted(c)  # the function form returns a NEW list
print(f"sorted(c) -> {c_sorted}, and c is still {c}")
print()

# --- Mutation across a function call ----------------------------------------


def add_in_place(lst, x):
    lst.append(x)  # changes the CALLER's list
    return lst


def add_a_copy(lst, x):
    return lst + [x]  # builds a new list; caller's list untouched


original = [1, 2]
add_in_place(original, 3)
print(f"after add_in_place:  original is {original}   <- it changed")

original = [1, 2]
result = add_a_copy(original, 3)
print(f"after add_a_copy:    original is {original}, result is {result}")
print()

# Copying a list explicitly:
source = [1, 2, 3]
copy1 = source[:]  # full slice
copy2 = list(source)  # constructor
copy1.append(99)
print(f"source {source} is unaffected by changes to its copy {copy1}")
print()

# --- Tuples -----------------------------------------------------------------

point = (3, 4)
print("point       =", point)
print("point[0]    =", point[0])
try:
    point[0] = 5
except TypeError as err:
    print("point[0] = 5 raises TypeError:", err)

# It is the COMMA that makes a tuple, not the parentheses.
print("type((5))   =", type((5)).__name__, "  <- just a number in brackets")
print("type((5,))  =", type((5,)).__name__, " <- the trailing comma makes it")
print("type(5, )   is the same as (5,):", (5,))
print()

# --- Unpacking --------------------------------------------------------------

x, y = point
print(f"x, y = point   ->  x={x}, y={y}")

first, *rest = [10, 20, 30, 40]
print(f"first, *rest   ->  first={first}, rest={rest}")

*most, final = [10, 20, 30, 40]
print(f"*most, final   ->  most={most}, final={final}")

# Unpacking in a for loop -- extremely common with pairs.
pairs = [("ada", 36), ("grace", 45)]
for name, age in pairs:
    print(f"  {name} is {age}")
