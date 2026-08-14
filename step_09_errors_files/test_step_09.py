"""Tests for step 9. Run with:  pytest step_09_errors_files/

The file drills use pytest's `tmp_path` fixture: a fresh empty directory per
test, deleted afterwards. Nothing is written into your tutorial folder.
"""

import pytest

from pytutor import load

m = load(__file__)


def test_drill_1_parse_int():
    assert m.parse_int("42") == 42, "a valid number converts"
    assert m.parse_int("abc") == 0, "invalid text -> the default 0"
    assert m.parse_int("abc", -1) == -1, "invalid text -> your own default"
    assert m.parse_int("") == 0, "an empty string is not a number"
    assert m.parse_int("  7 ") == 7, "int() still tolerates whitespace"
    assert m.parse_int("-5") == -5, "negative numbers are valid"


def test_drill_2_divide():
    assert m.divide(10, 2) == 5.0, "10 / 2 is 5.0"
    assert m.divide(10, 0) is None, "dividing by zero -> None, not a crash"
    assert m.divide(0, 5) == 0.0, "0 / 5 is fine"
    assert m.divide(-6, 3) == -2.0, "negatives are fine"


def test_drill_3_require_positive_returns_valid_input():
    assert m.require_positive(5) == 5, "a positive number is returned unchanged"
    assert m.require_positive(0.5) == 0.5, "floats count too"


def test_drill_3_require_positive_raises():
    with pytest.raises(ValueError):
        m.require_positive(0)  # zero is not positive

    with pytest.raises(ValueError):
        m.require_positive(-2)


def test_drill_3_error_message_names_the_value():
    with pytest.raises(ValueError) as info:
        m.require_positive(-2)
    assert "-2" in str(info.value), "put the offending value in the message"


def test_drill_4_read_lines(tmp_path):
    path = tmp_path / "notes.txt"
    path.write_text("a\nb\n")
    assert m.read_lines(path) == ["a", "b"], "newlines must be stripped"

    empty = tmp_path / "empty.txt"
    empty.write_text("")
    assert m.read_lines(empty) == [], "an empty file has no lines"

    no_final_newline = tmp_path / "ragged.txt"
    no_final_newline.write_text("a\nb")
    assert m.read_lines(no_final_newline) == ["a", "b"], "a missing final \\n is ok"


def test_drill_5_write_lines(tmp_path):
    path = tmp_path / "out.txt"
    assert m.write_lines(path, ["a", "b"]) == 2, "it returns how many it wrote"
    assert path.read_text() == "a\nb\n", "each line needs its own trailing newline"

    assert m.write_lines(path, []) == 0, "writing nothing returns 0"
    assert path.read_text() == "", "and leaves the file empty (mode 'w' truncates)"


def test_drill_5_round_trips_with_drill_4(tmp_path):
    path = tmp_path / "round.txt"
    original = ["one", "two", "three"]
    m.write_lines(path, original)
    assert m.read_lines(path) == original, "write then read should give it back"


def test_drill_6_count_lines(tmp_path):
    path = tmp_path / "notes.txt"
    path.write_text("a\nb\nc\n")
    assert m.count_lines(path) == 3, "three lines"

    empty = tmp_path / "empty.txt"
    empty.write_text("")
    assert m.count_lines(empty) == 0, "an empty file has 0 lines"


def test_drill_6_missing_file_is_not_an_error(tmp_path):
    missing = tmp_path / "does_not_exist.txt"
    assert m.count_lines(missing) == 0, "a missing file should give 0, not raise"
