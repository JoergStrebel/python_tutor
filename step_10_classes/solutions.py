"""Step 10 reference solutions."""

from dataclasses import dataclass


class Counter:
    def __init__(self, start=0):
        # `self.value` creates the attribute. A plain `value = start` would
        # make a local variable that disappears when __init__ returns.
        self.value = start

    def increment(self, by=1):
        self.value += by
        return self.value  # returning the new value makes the method chainable

    def reset(self):
        self.value = 0
        return self.value


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def __repr__(self):
        # The convention: return something that looks like the call which would
        # rebuild this object. It shows up in print(), in the debugger, and in
        # pytest's failure output.
        return f"Rectangle(width={self.width}, height={self.height})"


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        # Check BEFORE changing anything, so a refused withdrawal leaves the
        # balance exactly as it was.
        if amount > self.balance:
            raise ValueError(f"cannot withdraw {amount}, balance is {self.balance}")
        self.balance -= amount
        return self.balance

    def __repr__(self):
        return f"BankAccount(owner={self.owner!r}, balance={self.balance})"


@dataclass
class Point:
    # These two annotated lines are the whole declaration. The decorator turns
    # them into __init__, __repr__ and __eq__.
    x: int
    y: int

    def distance_to(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return (dx**2 + dy**2) ** 0.5  # ** 0.5 is a square root


class Stack:
    def __init__(self):
        # A fresh list per Stack. This is the object version of step 7's
        # "never use a mutable default" -- the list belongs to the instance.
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        # list.pop() already raises IndexError when empty, so we let it.
        return self.items.pop()

    def peek(self):
        if not self.items:
            raise IndexError("peek from an empty stack")
        return self.items[-1]

    def is_empty(self):
        return not self.items  # truthiness: an empty list is falsy

    def __len__(self):
        return len(self.items)  # this is what makes len(stack) work

    def __repr__(self):
        return f"Stack({self.items})"
