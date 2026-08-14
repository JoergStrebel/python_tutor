"""Step 7 examples -- run me with:  python3 step_07_functions/examples.py"""

# --- return vs print --------------------------------------------------------


def double_and_print(n):
    print("  (inside) the answer is", n * 2)  # shows it, gives nothing back


def double_and_return(n):
    return n * 2  # hands the value back


print("double_and_print(5):")
result_a = double_and_print(5)
print("  it returned:", result_a, "  <- None, so you cannot use it further")

result_b = double_and_return(5)
print("double_and_return(5) returned:", result_b)
print("  ...so you can keep going:", result_b + 1)
print()

# --- Defaults and keyword arguments -----------------------------------------


def power(base, exp=2):
    """Raise base to the power exp. Squares by default."""
    return base**exp


print("power(3)              =", power(3), "   <- exp defaulted to 2")
print("power(3, 3)           =", power(3, 3))
print("power(base=3, exp=3)  =", power(base=3, exp=3))
print("power(exp=3, base=3)  =", power(exp=3, base=3), "  <- order stops mattering")
print()


def describe_pet(name, species="dog", age=1):
    return f"{name} the {species}, age {age}"


print(describe_pet("Rex"))
print(describe_pet("Milo", "cat"))
print(describe_pet("Ada", age=7))  # skip the middle default by naming the last
print()

# --- The mutable default trap -----------------------------------------------


def add_broken(item, target=[]):  # the [] is created ONCE, at def time
    target.append(item)
    return target


def add_fixed(item, target=None):  # the idiomatic fix
    if target is None:
        target = []  # a fresh list on every call
    target.append(item)
    return target


print("Calling add_broken three times with no target:")
print("  ", add_broken("a"))
print("  ", add_broken("b"), "   <- the 'a' is still there!")
print("  ", add_broken("c"), "  <- and it keeps growing")

print("Calling add_fixed three times with no target:")
print("  ", add_fixed("a"))
print("  ", add_fixed("b"), "   <- fresh every time, as expected")
print("  ", add_fixed("c"))
print()

# --- *args and **kwargs -----------------------------------------------------


def total(*nums):
    print(f"  (inside) nums = {nums}, a {type(nums).__name__}")
    return sum(nums)


print("total(1, 2, 3) =", total(1, 2, 3))
print("total()        =", total())
print()


def describe(**kwargs):
    print(f"  (inside) kwargs = {kwargs}, a {type(kwargs).__name__}")
    return ", ".join(f"{k}={v}" for k, v in sorted(kwargs.items()))


print("describe(colour='red', size=3) ->", describe(colour="red", size=3))
print()

# --- Functions are values ---------------------------------------------------


def shout(text):
    return text.upper() + "!"


def apply_twice(fn, x):
    return fn(fn(x))  # call the function you were handed, twice


print("apply_twice(shout, 'hi')  =", apply_twice(shout, "hi"))
print("apply_twice(len, 'hi')    would fail -- len('hi') is 2, len(2) is an error")

alias = shout  # no parentheses: this points at the function itself
print("alias('bye')              =", alias("bye"))
print()

# --- Scope ------------------------------------------------------------------

message = "global"


def reads_global():
    return message  # reading an outer variable is fine


def makes_a_local():
    message = "local"  # this creates a NEW local name; the global is untouched
    return message


print("reads_global()   ->", reads_global())
print("makes_a_local()  ->", makes_a_local())
print("message is still ->", message)
print()

# --- Closures and nonlocal --------------------------------------------------


def make_counter():
    count = 0  # lives in make_counter's scope

    def step():
        nonlocal count  # "the count above, not a new local one"
        count += 1
        return count

    return step  # return the inner function itself


counter = make_counter()
print("counter() ->", counter())
print("counter() ->", counter())
print("counter() ->", counter(), "  <- it remembers between calls")

other = make_counter()  # a second, independent counter
print("a fresh counter() ->", other())
