"""Tests for step 2. Run with:  pytest step_02_conditionals/"""

from pytutor import load

m = load(__file__)


def test_drill_1_sign():
    assert m.sign(-3) == -1, "sign(-3) should be -1"
    assert m.sign(0) == 0, "sign(0) should be 0"
    assert m.sign(42) == 1, "sign(42) should be 1"
    assert m.sign(-0.5) == -1, "sign works on floats too"


def test_drill_2_is_even():
    assert m.is_even(4) is True, "4 is even"
    assert m.is_even(7) is False, "7 is odd"
    assert m.is_even(0) is True, "0 is even"
    assert m.is_even(-2) is True, "-2 is even"
    assert m.is_even(-3) is False, "-3 is odd"


def test_drill_3_grade():
    assert m.grade(95) == "A", "95 is an A"
    assert m.grade(90) == "A", "90 is exactly the A boundary"
    assert m.grade(85) == "B", "85 is a B"
    assert m.grade(70) == "C", "70 is exactly the C boundary"
    assert m.grade(69) == "D", "69 is a D"
    assert m.grade(0) == "F", "0 is an F"
    assert m.grade(59) == "F", "59 is just below the D boundary"


def test_drill_4_is_leap_year():
    assert m.is_leap_year(2024) is True, "2024 is divisible by 4 -> leap"
    assert m.is_leap_year(2023) is False, "2023 is not divisible by 4"
    assert m.is_leap_year(1900) is False, "1900 is a century year but not /400"
    assert m.is_leap_year(2000) is True, "2000 is divisible by 400 -> leap"
    assert m.is_leap_year(2100) is False, "2100 is a century year but not /400"


def test_drill_5_can_vote():
    assert m.can_vote(20, True) is True, "20 and a citizen -> can vote"
    assert m.can_vote(17, True) is False, "too young"
    assert m.can_vote(20, False) is False, "not a citizen"
    assert m.can_vote(18, True) is True, "18 is exactly old enough"


def test_drill_6_describe_empty():
    for falsy in ["", [], {}, (), 0, 0.0, None, False, set()]:
        assert m.describe_empty(falsy) == "empty", f"{falsy!r} is falsy -> 'empty'"

    for truthy in ["hi", [0], {"a": 1}, (1,), 1, -1, 0.5, True, " "]:
        assert (
            m.describe_empty(truthy) == "has content"
        ), f"{truthy!r} is truthy -> 'has content'"
