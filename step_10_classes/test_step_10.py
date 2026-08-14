"""Tests for step 10. Run with:  pytest step_10_classes/"""

import dataclasses

import pytest

from pytutor import load

m = load(__file__)


def test_drill_1_counter_starts_at_zero():
    c = m.Counter()
    assert c.value == 0, "a new Counter should start at 0"


def test_drill_1_counter_accepts_a_starting_value():
    assert m.Counter(10).value == 10, "Counter(10) should start at 10"


def test_drill_1_counter_increments():
    c = m.Counter()
    assert c.increment() == 1, "increment() returns the new value"
    assert c.value == 1, "and updates the attribute"
    assert c.increment(5) == 6, "increment(5) adds 5"
    assert c.value == 6, "the attribute keeps up"


def test_drill_1_counter_resets():
    c = m.Counter(7)
    assert c.reset() == 0, "reset() returns 0"
    assert c.value == 0, "and sets the attribute back to 0"


def test_drill_1_counters_are_independent():
    a, b = m.Counter(), m.Counter()
    a.increment()
    assert b.value == 0, "each Counter keeps its own value"


def test_drill_2_rectangle_attributes_and_measurements():
    r = m.Rectangle(3, 4)
    assert r.width == 3, "the width attribute"
    assert r.height == 4, "the height attribute"
    assert r.area() == 12, "3 * 4"
    assert r.perimeter() == 14, "2 * (3 + 4)"

    square = m.Rectangle(5, 5)
    assert square.area() == 25, "a square is just a rectangle"
    assert square.perimeter() == 20, "2 * (5 + 5)"


def test_drill_3_rectangle_repr():
    assert (
        repr(m.Rectangle(3, 4)) == "Rectangle(width=3, height=4)"
    ), "__repr__ should read like the call that would rebuild the object"
    assert repr(m.Rectangle(1, 2)) == "Rectangle(width=1, height=2)", "same shape"


def test_drill_4_bank_account_setup():
    a = m.BankAccount("ada")
    assert a.owner == "ada", "the owner attribute"
    assert a.balance == 0, "the balance defaults to 0"
    assert m.BankAccount("bob", 100).balance == 100, "or takes a starting balance"


def test_drill_4_deposit_and_withdraw():
    a = m.BankAccount("ada", 100)
    assert a.deposit(50) == 150, "deposit returns the new balance"
    assert a.balance == 150, "and updates the attribute"
    assert a.withdraw(30) == 120, "withdraw returns the new balance"
    assert a.balance == 120, "and updates the attribute"


def test_drill_4_overdraft_is_refused():
    a = m.BankAccount("ada", 100)
    with pytest.raises(ValueError):
        a.withdraw(1000)
    assert a.balance == 100, "a refused withdrawal must leave the balance alone"


def test_drill_4_error_message_names_the_amount():
    a = m.BankAccount("ada", 100)
    with pytest.raises(ValueError) as info:
        a.withdraw(1000)
    assert "1000" in str(info.value), "say how much was requested"


def test_drill_5_point_is_a_dataclass():
    assert dataclasses.is_dataclass(m.Point), "Point must use the @dataclass decorator"


def test_drill_5_point_construction_and_repr():
    p = m.Point(3, 4)
    assert p.x == 3, "the x field"
    assert p.y == 4, "the y field"
    assert repr(p) == "Point(x=3, y=4)", "the decorator generates this __repr__"


def test_drill_5_dataclasses_compare_by_value():
    assert m.Point(1, 2) == m.Point(1, 2), "two equal Points are ==; that is free"
    assert m.Point(1, 2) != m.Point(2, 1), "different fields, different Points"


def test_drill_5_distance_to():
    assert m.Point(0, 0).distance_to(m.Point(3, 4)) == 5.0, "the 3-4-5 triangle"
    assert m.Point(1, 1).distance_to(m.Point(1, 1)) == 0.0, "no distance to itself"
    assert m.Point(0, 0).distance_to(m.Point(0, -2)) == 2.0, "negatives work"


def test_drill_6_stack_starts_empty():
    s = m.Stack()
    assert s.is_empty() is True, "a new Stack is empty"
    assert len(s) == 0, "__len__ should report 0"


def test_drill_6_stack_push_peek_pop():
    s = m.Stack()
    s.push("a")
    s.push("b")
    assert len(s) == 2, "two items pushed"
    assert s.is_empty() is False, "no longer empty"
    assert s.peek() == "b", "peek returns the LAST item pushed"
    assert len(s) == 2, "peek must not remove anything"
    assert s.pop() == "b", "pop returns the last item"
    assert len(s) == 1, "pop removes it"
    assert s.pop() == "a", "then the one below"
    assert s.is_empty() is True, "empty again"


def test_drill_6_empty_stack_raises():
    s = m.Stack()
    with pytest.raises(IndexError):
        s.pop()
    with pytest.raises(IndexError):
        s.peek()


def test_drill_6_stacks_are_independent():
    a, b = m.Stack(), m.Stack()
    a.push("x")
    assert len(b) == 0, "each Stack needs its OWN list, made in __init__"
