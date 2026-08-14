"""Step 10 examples -- run me with:  python3 step_10_classes/examples.py"""

from dataclasses import dataclass

# --- You have been using objects all along ----------------------------------

text = "hello"
print(f"{text!r} is an object of type {type(text).__name__}")
print("   .upper() is a method on it ->", text.upper())

items = [3, 1]
print(f"{items} is an object of type {type(items).__name__}")
items.append(2)
print("   .append(2) is a method on it ->", items)
print()

# --- Your own class ---------------------------------------------------------


class Rectangle:
    def __init__(self, width, height):
        # `self` is the new object. These two lines create its attributes.
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


r = Rectangle(3, 4)
print("r = Rectangle(3, 4)")
print("   r.width      =", r.width, "  <- attribute, no parentheses")
print("   r.area()     =", r.area(), " <- method, needs parentheses")
print("   r.perimeter()=", r.perimeter())
print("   r.area (no parens) is", r.area, "-- the method itself, uncalled")
print()

# Each object keeps its own data.
s = Rectangle(10, 1)
print(f"a second rectangle: s.area() = {s.area()}, while r.area() is still {r.area()}")
print()

# r.area() is really Rectangle.area(r) -- that is where `self` comes from.
print("Rectangle.area(r) =", Rectangle.area(r), "  <- the same call, spelled out")
print()

# --- Why __repr__ matters ---------------------------------------------------

print("printing r without a __repr__:")
print("  ", r)


class Rectangle2:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def __repr__(self):
        return f"Rectangle2(width={self.width}, height={self.height})"


print("printing one WITH a __repr__:")
print("  ", Rectangle2(3, 4))
print("   and inside a list:", [Rectangle2(1, 2), Rectangle2(3, 4)])
print()

# --- Methods that guard their input ------------------------------------------


class BankAccount:
    def __init__(self, owner, balance=0):  # a default, from step 7
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            # Refusing loudly beats quietly doing the wrong thing (step 9).
            raise ValueError(f"cannot withdraw {amount}, balance is {self.balance}")
        self.balance -= amount
        return self.balance

    def __repr__(self):
        return f"BankAccount(owner={self.owner!r}, balance={self.balance})"


account = BankAccount("ada", 100)
print("account          =", account)
account.deposit(50)
print("after deposit(50)=", account)
account.withdraw(30)
print("after withdraw(30)=", account)
try:
    account.withdraw(1000)
except ValueError as err:
    print("withdraw(1000) raised ValueError:", err)
print()

# --- Plain class vs. dataclass ----------------------------------------------


class PlainPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y


@dataclass
class Point:
    x: int
    y: int


print("PlainPoint(1, 2)            ->", PlainPoint(1, 2))
print("Point(1, 2)                 ->", Point(1, 2), "  <- __repr__ for free")
print()
print("PlainPoint(1, 2) == PlainPoint(1, 2) ->", PlainPoint(1, 2) == PlainPoint(1, 2))
print("   two plain objects are equal only if they are the SAME object")
print("Point(1, 2) == Point(1, 2)           ->", Point(1, 2) == Point(1, 2))
print("   a dataclass compares by VALUE -- __eq__ for free too")
print()

# --- Plugging into built-in syntax with dunder methods ----------------------


class Stack:
    def __init__(self):
        self.items = []  # a fresh list per Stack -- see step 7's mutable default

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return not self.items  # step 2's truthiness

    def __len__(self):
        return len(self.items)  # makes len(stack) work

    def __repr__(self):
        return f"Stack({self.items})"


stack = Stack()
for value in ["a", "b", "c"]:
    stack.push(value)
print("stack        =", stack)
print("len(stack)   =", len(stack), "  <- __len__ makes this work")
print("stack.pop()  =", stack.pop())
print("now          =", stack, "with len", len(stack))
print("is_empty()   =", stack.is_empty())
