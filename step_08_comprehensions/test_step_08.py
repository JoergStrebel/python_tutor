"""Tests for step 8. Run with:  pytest step_08_comprehensions/"""

from pytutor import load

m = load(__file__)


def test_drill_1_squares():
    assert m.squares(5) == [1, 4, 9, 16, 25], "the squares of 1 to 5"
    assert m.squares(1) == [1], "just 1 squared"
    assert m.squares(0) == [], "no numbers -> empty list"
    assert m.squares(-2) == [], "a negative n should also give []"


def test_drill_2_evens():
    assert m.evens([1, 2, 3, 4]) == [2, 4], "keep the even ones"
    assert m.evens([1, 3]) == [], "no evens -> empty list"
    assert m.evens([]) == [], "empty in, empty out"
    assert m.evens([0, -2, -3]) == [0, -2], "0 and -2 are even"
    assert m.evens([4, 2]) == [4, 2], "the original order is kept"


def test_drill_3_lengths():
    assert m.lengths(["fig", "apple"]) == {"fig": 3, "apple": 5}, "word -> its length"
    assert m.lengths([]) == {}, "empty in, empty out"
    assert m.lengths([""]) == {"": 0}, "an empty word has length 0"
    assert isinstance(m.lengths(["a"]), dict), "the result must be a dict"


def test_drill_4_numbered():
    assert m.numbered(["apple", "pear"]) == ["1. apple", "2. pear"], "numbering from 1"
    assert m.numbered([]) == [], "empty in, empty out"
    assert m.numbered(["solo"]) == ["1. solo"], "a single item is number 1"
    assert m.numbered(list("abc"))[2] == "3. c", "the third item is number 3"


def test_drill_5_pair_up():
    assert m.pair_up([1, 2], ["x", "y"]) == [(1, "x"), (2, "y")], "element by element"
    assert m.pair_up([1, 2, 3], ["x"]) == [(1, "x")], "zip stops at the shortest"
    assert m.pair_up([], []) == [], "empty in, empty out"
    assert isinstance(m.pair_up([1], ["a"]), list), "call list() -- zip is lazy"


def test_drill_6_sort_by_length():
    assert m.sort_by_length(["banana", "fig", "date"]) == ["fig", "date", "banana"]
    assert m.sort_by_length(["bb", "aa"]) == ["bb", "aa"], "equal lengths keep order"
    assert m.sort_by_length([]) == [], "empty in, empty out"
    assert m.sort_by_length(["a"]) == ["a"], "a single word"


def test_drill_6_does_not_modify_its_input():
    original = ["banana", "fig"]
    m.sort_by_length(original)
    assert original == ["banana", "fig"], "use sorted(), not .sort()"
