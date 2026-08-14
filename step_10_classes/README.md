# Step 10 — Classes and Objects

You have been using objects since step 1. `"abc".upper()` is a method call on a
`str` object; `[].append(x)` is a method call on a `list`. This step shows you
the other side of that: writing your own types, so that related data and the
functions that act on it live in one place.

## Syntax card

```python
class Rectangle:                       # class names use CapitalisedWords
    def __init__(self, width, height): # the constructor -- runs on Rectangle(...)
        self.width = width             # `self.x = ...` creates an attribute
        self.height = height

    def area(self):                    # every method takes `self` first
        return self.width * self.height

    def __repr__(self):                # how the object shows up when printed
        return f"Rectangle(width={self.width}, height={self.height})"

r = Rectangle(3, 4)                    # calls __init__ -- note: no `new`
r.width                                # 3          -- attribute access
r.area()                               # 12         -- method call, needs ()
isinstance(r, Rectangle)               # True

from dataclasses import dataclass

@dataclass                             # writes __init__ and __repr__ for you
class Point:
    x: int
    y: int
```

## What each piece does

**A class is a template; an object is one thing made from it.** `Rectangle` is
the idea of a rectangle. `Rectangle(3, 4)` is a particular one. You can make as
many as you like and each keeps its own `width` and `height`.

**`__init__` runs automatically when you create an object.** You never call it
yourself. Its job is to set up the attributes; note that it returns nothing.

**`self` is the object the method was called on.** It is passed automatically:
you write `def area(self)` but you call `r.area()`. This is the single most
common source of confusion, and it goes away once you notice that `r.area()` is
really `Rectangle.area(r)`.

Forgetting `self.` inside a method is the other classic slip. Plain `width = 3`
creates a local variable that vanishes when the method ends; `self.width = 3`
stores it on the object.

**`__repr__` is worth writing every time.** Without it, printing your object
gives `<__main__.Rectangle object at 0x7f3c...>`, which tells you nothing. With
it, you get something you can read — in `print`, in the debugger, and in pytest
failure messages. The convention is to return something that looks like the
call that would recreate the object.

**The double underscores mark "Python calls this for you".** `__init__` on
construction, `__repr__` on printing, `__len__` when you call `len(obj)`,
`__eq__` when you use `==`. They are often called *dunder* methods. You are
plugging your class into syntax that already exists.

**`@dataclass` removes the boilerplate.** When a class is mostly a bundle of
fields, the decorator generates `__init__`, `__repr__` and `__eq__` from the
field declarations. Two lines instead of ten, and `==` compares by value rather
than by identity — which plain classes do not do.

**When should you write a class?** When several pieces of data always travel
together *and* there are operations that belong to them. If you only need data,
a dict or a dataclass is enough. If you only need behaviour, a function is
enough. Do not reach for a class by default.

## Common errors you will hit

```
TypeError: Rectangle.__init__() missing 1 required positional argument: 'height'
```
You created the object with too few arguments. Note that `self` does not count.

```
TypeError: area() takes 0 positional arguments but 1 was given
```
You wrote `def area():` without `self`, then called `r.area()`. Add `self`.

```
AttributeError: 'Rectangle' object has no attribute 'wdith'
```
A typo, or you assigned it in a method that was never called. Unlike some
languages, Python only creates the attribute when the assignment actually runs.

```
AttributeError: 'Rectangle' object has no attribute 'area'... did you mean: ...
```
Usually a missing `()`: `r.area` is the method itself, `r.area()` calls it.

## Do the drills

```bash
python3 step_10_classes/examples.py
pytest step_10_classes/
```

## Recall drill

Close this file and write from memory:

1. A `Dog` class with a name, and a `speak()` method returning `"<name> says woof"`.
2. A `__repr__` for it, and what you would see printed without one.
3. The same class as a `@dataclass`, and one thing the decorator gives you for free.

## After this step

Go to `../CAPSTONE.md`. It is one small program that uses all ten steps at once —
which is the real test of whether the constructs have become automatic.
