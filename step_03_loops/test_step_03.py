"""Tests for step 3. Run with:  pytest step_03_loops/"""

from pytutor import load

m = load(__file__)


def test_drill_1_sum_to():
    assert m.sum_to(5) == 15, "1+2+3+4+5 = 15"
    assert m.sum_to(1) == 1, "sum_to(1) is just 1"
    assert m.sum_to(0) == 0, "sum_to(0) should be 0, not an error"
    assert m.sum_to(-4) == 0, "a negative n should also give 0"
    assert m.sum_to(100) == 5050, "the famous 1..100 sum"


def test_drill_2_count_vowels():
    assert m.count_vowels("hello") == 2, "e and o"
    assert m.count_vowels("XYZ") == 0, "no vowels at all"
    assert m.count_vowels("AEIOU") == 5, "uppercase vowels count too"
    assert m.count_vowels("") == 0, "an empty string has no vowels"
    assert m.count_vowels("Programming") == 3, "o, a, i"


def test_drill_3_first_multiple_over():
    assert m.first_multiple_over(7, 50) == 56, "7*8 = 56 is the first over 50"
    assert m.first_multiple_over(10, 10) == 20, "strictly greater, so not 10"
    assert m.first_multiple_over(3, 0) == 3, "the first multiple of 3 over 0"
    assert m.first_multiple_over(1, 99) == 100, "multiples of 1 are every number"
    assert m.first_multiple_over(25, 100) == 125, "25*5 = 125"


def test_drill_4_skip_negatives():
    assert m.skip_negatives([1, -2, 3, -4]) == [1, 3], "drop the negatives"
    assert m.skip_negatives([-1, -2]) == [], "all negative -> empty list"
    assert m.skip_negatives([]) == [], "empty in, empty out"
    assert m.skip_negatives([0, -1, 0]) == [0, 0], "0 is not negative -- keep it"


def test_drill_4_does_not_modify_its_input():
    original = [1, -2, 3]
    m.skip_negatives(original)
    assert original == [1, -2, 3], "build a NEW list; leave the argument alone"


def test_drill_5_countdown():
    assert m.countdown(5) == [5, 4, 3, 2, 1], "counts down to 1, not to 0"
    assert m.countdown(1) == [1], "countdown(1) is just [1]"
    assert m.countdown(0) == [], "countdown(0) should be empty, not an error"
    assert m.countdown(-3) == [], "a negative n should also give []"


def test_drill_6_times_table():
    rows = m.times_table(3)
    assert len(rows) == 10, "the table runs from 1 to 10, so 10 rows"
    assert rows[0] == "3 x 1 = 3", 'the first row should be "3 x 1 = 3"'
    assert rows[9] == "3 x 10 = 30", 'the last row should be "3 x 10 = 30"'
    assert m.times_table(7)[6] == "7 x 7 = 49", "7 x 7 = 49"
