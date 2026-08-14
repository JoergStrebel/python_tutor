"""Step 3 examples -- run me with:  python3 step_03_loops/examples.py"""

# --- for over a sequence ----------------------------------------------------

for fruit in ["apple", "pear", "plum"]:
    print("fruit:", fruit)
print()

# A string is a sequence of characters, so this works too.
for letter in "cat":
    print("letter:", letter)
print()

# --- range --------------------------------------------------------------

print("range(5)        ->", list(range(5)))
print("range(1, 6)     ->", list(range(1, 6)))
print("range(0, 10, 2) ->", list(range(0, 10, 2)))
print("range(5, 0, -1) ->", list(range(5, 0, -1)))
print("range(3, 3)     ->", list(range(3, 3)), "  <- empty: stop is exclusive")
print()

# --- The accumulator pattern ------------------------------------------------

numbers = [4, 8, 15, 16, 23, 42]

total = 0  # 1. start with an empty answer
for n in numbers:  # 2. visit every item
    total = total + n  # 3. fold it in   (total += n is shorthand)
print(f"sum of {numbers} = {total}")  # 4. use the finished answer

# The same shape, but accumulating into a list instead of a number.
big_ones = []
for n in numbers:
    if n > 15:
        big_ones.append(n)
print(f"the ones over 15: {big_ones}")
print()

# --- break: stop as soon as you have your answer ----------------------------

for n in numbers:
    print(f"  checking {n}...")
    if n % 2 == 1:
        print(f"  found the first odd number: {n}")
        break  # nothing after this is checked
print()

# --- continue: skip this one, keep going ------------------------------------

print("odd numbers from 1 to 10, via continue:")
for n in range(1, 11):
    if n % 2 == 0:
        continue  # even -> jump straight to the next n
    print(" ", n)
print()

# --- while: repeat until something changes ----------------------------------

countdown = 5
while countdown > 0:
    print("T-minus", countdown)
    countdown = countdown - 1  # WITHOUT this line the loop never ends
print("Lift off!")
print()

# --- A while loop that searches ---------------------------------------------

# Find the first power of 2 above 1000.
value = 1
while value <= 1000:
    value = value * 2
print(f"first power of 2 above 1000: {value}")
print()

# --- The shorthand operators you will see everywhere -------------------------

x = 10
x += 3  # same as x = x + 3
x -= 5  # same as x = x - 5
x *= 2  # same as x = x * 2
print("after += 3, -= 5, *= 2 starting from 10:", x)
