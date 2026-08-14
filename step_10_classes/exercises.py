"""Step 10 drills -- classes, __init__, methods, __repr__, dataclasses.

Unlike the earlier steps these drills ask you to write whole classes. Delete the
`raise NotImplementedError` lines and write the real bodies.
"""

# You will need this import for drill 5.
# from dataclasses import dataclass


class Counter:
    """Drill 1: a counter that remembers its value.

        c = Counter()        # starts at 0
        c.value              -> 0
        c.increment()        -> 1     (and c.value becomes 1)
        c.increment(5)       -> 6
        c.reset()            -> 0
        Counter(10).value    -> 10    (an optional starting value)

    Practise: __init__ with a default argument, an attribute, and methods that
    change it. Each method returns the new value.
    """

    def __init__(self, start=0):
        raise NotImplementedError("drill 1: Counter.__init__")

    def increment(self, by=1):
        raise NotImplementedError("drill 1: Counter.increment")

    def reset(self):
        raise NotImplementedError("drill 1: Counter.reset")


class Rectangle:
    """Drills 2 and 3: a rectangle that can measure itself and print nicely.

        r = Rectangle(3, 4)
        r.width          -> 3
        r.height         -> 4
        r.area()         -> 12
        r.perimeter()    -> 14
        repr(r)          -> "Rectangle(width=3, height=4)"

    Drill 2 is __init__, area and perimeter.
    Drill 3 is __repr__ -- note the exact format expected above.
    """

    def __init__(self, width, height):
        raise NotImplementedError("drill 2: Rectangle.__init__")

    def area(self):
        raise NotImplementedError("drill 2: Rectangle.area")

    def perimeter(self):
        raise NotImplementedError("drill 2: Rectangle.perimeter")

    def __repr__(self):
        raise NotImplementedError("drill 3: Rectangle.__repr__")


class BankAccount:
    """Drill 4: an account that refuses to go overdrawn.

        a = BankAccount("ada")        # balance defaults to 0
        a = BankAccount("ada", 100)
        a.owner            -> "ada"
        a.balance          -> 100
        a.deposit(50)      -> 150     (and a.balance becomes 150)
        a.withdraw(30)     -> 120
        a.withdraw(1000)   -> raises ValueError, and the balance is unchanged

    The error message must mention the amount requested.

    Practise: methods that change state, plus a `raise` guard from step 9.
    """

    def __init__(self, owner, balance=0):
        raise NotImplementedError("drill 4: BankAccount.__init__")

    def deposit(self, amount):
        raise NotImplementedError("drill 4: BankAccount.deposit")

    def withdraw(self, amount):
        raise NotImplementedError("drill 4: BankAccount.withdraw")


# Drill 5: rewrite this as a dataclass.
#
#     p = Point(3, 4)
#     p.x               -> 3
#     repr(p)           -> "Point(x=3, y=4)"
#     Point(1, 2) == Point(1, 2)   -> True     (a plain class gives False here)
#     Point(0, 0).distance_to(Point(3, 4))  -> 5.0
#
# Add the @dataclass decorator and declare the two fields with type
# annotations, then write distance_to yourself. Do NOT write __init__ or
# __repr__ -- the decorator generates them.
#
# The distance formula is the square root of (dx squared + dy squared).
# math.sqrt or the ** 0.5 operator will both do it.
class Point:
    """Drill 5: a point, as a dataclass."""

    def distance_to(self, other):
        raise NotImplementedError("drill 5: Point.distance_to")


class Stack:
    """Drill 6: a last-in, first-out stack wrapping a list.

        s = Stack()
        s.is_empty()   -> True
        s.push("a")
        s.push("b")
        len(s)         -> 2
        s.peek()       -> "b"      (look, do not remove)
        s.pop()        -> "b"      (remove and return)
        len(s)         -> 1
        s.is_empty()   -> False

    Popping or peeking an empty stack must raise an IndexError.

    Practise: wrapping a list in a class, and __len__ so that len() works.
    """

    def __init__(self):
        raise NotImplementedError("drill 6: Stack.__init__")

    def push(self, item):
        raise NotImplementedError("drill 6: Stack.push")

    def pop(self):
        raise NotImplementedError("drill 6: Stack.pop")

    def peek(self):
        raise NotImplementedError("drill 6: Stack.peek")

    def is_empty(self):
        raise NotImplementedError("drill 6: Stack.is_empty")

    def __len__(self):
        raise NotImplementedError("drill 6: Stack.__len__")
