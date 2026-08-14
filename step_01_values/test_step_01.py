"""Tests for step 1. Run with:  pytest step_01_values/"""

from pytutor import load

m = load(__file__)


def test_drill_1_greet():
    assert m.greet("Ada") == "Hello, Ada!", 'greet("Ada") should be "Hello, Ada!"'
    assert m.greet("Bob") == "Hello, Bob!", 'greet("Bob") should be "Hello, Bob!"'


def test_drill_2_celsius_to_fahrenheit():
    assert m.celsius_to_fahrenheit(0) == 32, "0 C is 32 F"
    assert m.celsius_to_fahrenheit(100) == 212, "100 C is 212 F"
    assert m.celsius_to_fahrenheit(-40) == -40, "-40 C is -40 F (they meet there)"
    assert m.celsius_to_fahrenheit(37) == 98.6, "37 C is 98.6 F"


def test_drill_3_describe_type():
    assert m.describe_type(3) == "int", "3 is an int"
    assert m.describe_type("hi") == "str", '"hi" is a str'
    assert m.describe_type(2.5) == "float", "2.5 is a float"
    assert m.describe_type(True) == "bool", "True is a bool"
    assert m.describe_type([1, 2]) == "list", "[1, 2] is a list"


def test_drill_4_to_int():
    assert m.to_int("42") == 42, 'to_int("42") should be the number 42'
    assert m.to_int("  7  ") == 7, "int() copes with surrounding whitespace"
    assert m.to_int("-3") == -3, "negative numbers work too"
    assert isinstance(m.to_int("42"), int), "the result must be an int, not a str"


def test_drill_5_format_price():
    assert m.format_price(3.5) == "3.50 EUR", "3.5 should render as 3.50"
    assert m.format_price(12) == "12.00 EUR", "a whole number still gets 2 decimals"
    assert m.format_price(0.999) == "1.00 EUR", "the format spec rounds"
    assert m.format_price(0) == "0.00 EUR", "zero renders as 0.00"


def test_drill_6_swap():
    assert m.swap(1, 2) == (2, 1), "swap(1, 2) should be (2, 1)"
    assert m.swap("x", "y") == ("y", "x"), 'swap("x", "y") should be ("y", "x")'
    assert m.swap(None, 5) == (5, None), "swap works on any two values"
