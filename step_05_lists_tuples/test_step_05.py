"""Tests for step 5. Run with:  pytest step_05_lists_tuples/"""

from pytutor import load

m = load(__file__)


def test_drill_1_add_item_mutates_the_caller_list():
    shopping = ["milk"]
    m.add_item(shopping, "eggs")
    assert shopping == ["milk", "eggs"], "the CALLER's list must have grown"

    empty = []
    returned = m.add_item(empty, "x")
    assert returned == ["x"], "the list is also returned"
    assert returned is empty, "return the same list object, not a copy"


def test_drill_2_second_largest():
    assert m.second_largest([1, 5, 3]) == 3, "5 is largest, 3 is second"
    assert m.second_largest([5, 5, 3]) == 3, "duplicates count once"
    assert m.second_largest([7]) is None, "one value -> no second"
    assert m.second_largest([]) is None, "empty -> None"
    assert m.second_largest([2, 2, 2]) is None, "only one distinct value"
    assert m.second_largest([-1, -5]) == -5, "negatives work too"


def test_drill_3_flatten():
    assert m.flatten([(1, 2), (3, 4)]) == [1, 2, 3, 4], "two pairs -> four items"
    assert m.flatten([]) == [], "empty in, empty out"
    assert m.flatten([("a", "b")]) == ["a", "b"], "works on any values"


def test_drill_4_min_max():
    assert m.min_max([3, 1, 4]) == (1, 4), "smallest first, largest second"
    assert m.min_max([7]) == (7, 7), "one item is both min and max"
    assert m.min_max([]) == (None, None), "empty -> (None, None)"
    assert m.min_max([-2, 0, 2]) == (-2, 2), "negatives included"
    assert isinstance(m.min_max([1, 2]), tuple), "return a tuple, not a list"


def test_drill_5_rotate():
    assert m.rotate([1, 2, 3, 4, 5], 2) == [3, 4, 5, 1, 2], "first 2 move to the end"
    assert m.rotate([1, 2, 3], 0) == [1, 2, 3], "rotating by 0 changes nothing"
    assert m.rotate([1, 2, 3], 3) == [1, 2, 3], "a full turn changes nothing"
    assert m.rotate([1, 2, 3], 4) == [2, 3, 1], "4 is one full turn plus one"
    assert m.rotate([], 3) == [], "an empty list rotates to itself"


def test_drill_5_rotate_does_not_modify_its_input():
    original = [1, 2, 3]
    m.rotate(original, 1)
    assert original == [1, 2, 3], "rotate must build a NEW list"


def test_drill_6_split_head_tail():
    assert m.split_head_tail([1, 2, 3]) == (1, [2, 3]), "head 1, tail [2, 3]"
    assert m.split_head_tail([9]) == (9, []), "a lone item leaves an empty tail"
    assert m.split_head_tail([]) == (None, []), "empty -> (None, [])"
    head, tail = m.split_head_tail(["a", "b"])
    assert isinstance(tail, list), "the tail must be a list, not a tuple"
