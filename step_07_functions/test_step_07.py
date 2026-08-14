"""Tests for step 7. Run with:  pytest step_07_functions/"""

from pytutor import load

m = load(__file__)


def test_drill_1_power():
    assert m.power(3) == 9, "with no exp given, it should square"
    assert m.power(2, 10) == 1024, "2 to the 10th"
    assert m.power(5, 0) == 1, "anything to the power 0 is 1"
    assert m.power(base=2, exp=3) == 8, "it must accept keyword arguments too"


def test_drill_2_make_greeting():
    assert m.make_greeting("Ada") == "Hello, Ada!", "all three defaults"
    assert m.make_greeting("Ada", "Hi") == "Hi, Ada!", "override the greeting"
    assert m.make_greeting("Ada", punct="?") == "Hello, Ada?", "skip to the last"
    assert m.make_greeting("Ada", "Yo", ".") == "Yo, Ada.", "override everything"


def test_drill_3_total():
    assert m.total(1, 2, 3) == 6, "three numbers"
    assert m.total(5) == 5, "one number"
    assert m.total() == 0, "no numbers at all -> 0, not an error"
    assert m.total(*[1, 2, 3, 4]) == 10, "a list can be spread with *"


def test_drill_4_describe():
    assert m.describe(size=3, colour="red") == "colour=red, size=3", "sorted by key"
    assert m.describe(colour="red", size=3) == "colour=red, size=3", "order-independent"
    assert m.describe(a=1) == "a=1", "a single pair has no separator"
    assert m.describe() == "", "no arguments -> empty string"


def test_drill_5_apply_twice():
    assert m.apply_twice(lambda n: n + 1, 5) == 7, "5 -> 6 -> 7"
    assert m.apply_twice(lambda n: n * 2, 3) == 12, "3 -> 6 -> 12"
    assert m.apply_twice(str.upper, "hi") == "HI", "already uppercase stays put"
    assert m.apply_twice(m.power, 2) == 16, "2 -> 4 -> 16, reusing drill 1"


def test_drill_6_make_accumulator():
    acc = m.make_accumulator()
    assert callable(acc), "make_accumulator must return a FUNCTION, not a number"
    assert acc(10) == 10, "first call returns the first value"
    assert acc(5) == 15, "it remembers the 10"
    assert acc(1) == 16, "and keeps remembering"


def test_drill_6_accumulators_are_independent():
    first = m.make_accumulator()
    second = m.make_accumulator()
    first(100)
    assert second(3) == 3, "a fresh accumulator must start from 0 again"
