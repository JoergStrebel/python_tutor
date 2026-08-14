"""Step 1 examples -- run me with:  python3 step_01_values/examples.py

Read each block next to its printed output. Then try changing a value and
running the file again. Breaking things on purpose is how you learn what the
rules actually are.
"""

# --- Variables and the four basic types ------------------------------------

name = "Ada"
age = 36
height = 1.72
is_student = False

print("name    =", name, "   type:", type(name).__name__)
print("age     =", age, "     type:", type(age).__name__)
print("height  =", height, "  type:", type(height).__name__)
print("student =", is_student, "  type:", type(is_student).__name__)
print()

# --- f-strings --------------------------------------------------------------

# The `f` prefix makes {} mean "evaluate this expression and paste it here".
print(f"{name} is {age} years old.")

# Any expression fits inside the braces, not just a bare name.
print(f"Next year {name} will be {age + 1}.")

# A format spec after the colon controls how the value is rendered.
print(f"Height rounded: {height:.1f} m")
print(f"One third:      {1 / 3:.3f}")
print(f"As a percent:   {0.8256:.1%}")
print()

# --- Why type matters -------------------------------------------------------

print('3 + 4     =', 3 + 4)  # int addition
print('"3" + "4" =', "3" + "4")  # str concatenation -- a completely different thing!
print()

# --- Converting between types ----------------------------------------------

typed_by_user = "42"  # input() would give you text like this
print(f'The string {typed_by_user!r} has type {type(typed_by_user).__name__}')

as_number = int(typed_by_user)
print(f"Converted to {as_number}, type {type(as_number).__name__}, plus 3 = {as_number + 3}")

# int() tolerates surrounding whitespace, which is handy for user input.
print("int('  7  ') =", int("  7  "))

# float -> int truncates towards zero. It does NOT round.
print("int(9.99)    =", int(9.99))
print("round(9.99)  =", round(9.99))
print()

# --- Several names, one line -----------------------------------------------

a, b = 1, 2
print(f"before swap: a={a}, b={b}")
a, b = b, a  # the classic Python swap -- no temporary variable needed
print(f"after swap:  a={a}, b={b}")
