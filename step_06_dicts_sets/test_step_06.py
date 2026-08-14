"""Tests for step 6. Run with:  pytest step_06_dicts_sets/"""

from pytutor import load

m = load(__file__)


def test_drill_1_count_words():
    assert m.count_words("the cat the") == {"the": 2, "cat": 1}, "the appears twice"
    assert m.count_words("") == {}, "no words -> empty dict"
    assert m.count_words("One one ONE") == {"one": 3}, "case must be ignored"
    assert m.count_words("a  b") == {"a": 1, "b": 1}, "extra spacing is fine"


def test_drill_2_invert():
    assert m.invert({"a": 1, "b": 2}) == {1: "a", 2: "b"}, "keys and values swap"
    assert m.invert({}) == {}, "empty in, empty out"
    assert m.invert({"a": 1, "b": 1}) == {1: "b"}, "on a clash the last key wins"


def test_drill_2_invert_does_not_modify_its_input():
    original = {"a": 1}
    m.invert(original)
    assert original == {"a": 1}, "build a NEW dict; leave the argument alone"


def test_drill_3_safe_lookup():
    assert m.safe_lookup({"a": 1}, "a") == 1, "present key -> its value"
    assert m.safe_lookup({"a": 1}, "z") is None, "absent key -> None by default"
    assert m.safe_lookup({"a": 1}, "z", 0) == 0, "absent key -> your default"
    assert m.safe_lookup({}, "z", "?") == "?", "works on an empty dict"
    assert m.safe_lookup({"a": None}, "a", "?") is None, "a stored None is a value"


def test_drill_4_merge():
    assert m.merge({"x": 1}, {"y": 2}) == {"x": 1, "y": 2}, "both sets of entries"
    assert m.merge({"x": 1}, {"x": 9}) == {"x": 9}, "on a clash, b wins"
    assert m.merge({}, {}) == {}, "empty + empty -> empty"
    assert m.merge({"a": 1}, {}) == {"a": 1}, "merging nothing changes nothing"


def test_drill_4_merge_does_not_modify_its_inputs():
    a, b = {"x": 1}, {"x": 9}
    m.merge(a, b)
    assert a == {"x": 1}, "the first dict must be left alone"
    assert b == {"x": 9}, "the second dict must be left alone"


def test_drill_5_unique_preserving_order():
    assert m.unique_preserving_order([3, 1, 3, 2, 1]) == [3, 1, 2], "first-seen order"
    assert m.unique_preserving_order([]) == [], "empty in, empty out"
    assert m.unique_preserving_order([1, 2, 3]) == [1, 2, 3], "no duplicates to drop"
    assert m.unique_preserving_order(["b", "a", "b"]) == ["b", "a"], "order is kept"


def test_drill_6_common_tags():
    assert m.common_tags(["x", "y"], ["y", "z"]) == ["y"], "only y is in both"
    assert m.common_tags(["a"], ["b"]) == [], "nothing in common -> []"
    assert m.common_tags(["b", "a"], ["a", "b"]) == ["a", "b"], "the result is sorted"
    assert m.common_tags(["a", "a"], ["a"]) == ["a"], "no duplicates in the result"
    assert m.common_tags([], ["a"]) == [], "empty input -> empty result"
