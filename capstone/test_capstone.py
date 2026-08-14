"""Tests for the capstone. Run with:  pytest capstone/

These tests ARE the specification -- there is no solutions file. When a test
fails, read what it expected and work backwards.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import wordfreq as w  # noqa: E402 -- the sys.path line above must come first

SAMPLE = Path(__file__).resolve().parent / "sample.txt"


# --- normalise --------------------------------------------------------------


def test_normalise_lowercases_and_splits():
    assert w.normalise("The cat THE Cat") == ["the", "cat", "the", "cat"]


def test_normalise_strips_edge_punctuation():
    assert w.normalise("cat, mat. dog!") == ["cat", "mat", "dog"]
    assert w.normalise("(hello) [world];") == ["hello", "world"]


def test_normalise_keeps_inner_punctuation():
    assert w.normalise("don't") == ["don't"], "only the ENDS are stripped"


def test_normalise_drops_empties():
    assert w.normalise("--- ...") == [], "punctuation-only words disappear"
    assert w.normalise("") == [], "empty text -> no words"
    assert w.normalise("   ") == [], "whitespace only -> no words"


def test_normalise_handles_newlines():
    assert w.normalise("a\nb\tc") == ["a", "b", "c"], "split() handles any whitespace"


# --- count_words ------------------------------------------------------------


def test_count_words():
    assert w.count_words(["a", "b", "a"]) == {"a": 2, "b": 1}
    assert w.count_words([]) == {}, "no words -> empty dict"
    assert w.count_words(["solo"]) == {"solo": 1}


# --- top_n ------------------------------------------------------------------


def test_top_n_orders_by_count_descending():
    counts = {"a": 1, "b": 3, "c": 2}
    assert w.top_n(counts, 3) == [("b", 3), ("c", 2), ("a", 1)]


def test_top_n_breaks_ties_alphabetically():
    assert w.top_n({"b": 2, "a": 2, "c": 1}, 2) == [("a", 2), ("b", 2)]


def test_top_n_limits_the_result():
    counts = {"a": 1, "b": 3, "c": 2}
    assert w.top_n(counts, 1) == [("b", 3)], "only the top one"
    assert w.top_n(counts, 0) == [], "top 0 is nothing"


def test_top_n_copes_with_asking_for_too_many():
    assert w.top_n({"a": 1}, 10) == [("a", 1)], "fewer words than asked for is fine"
    assert w.top_n({}, 5) == [], "no words at all"


# --- load_text --------------------------------------------------------------


def test_load_text_reads_a_file(tmp_path):
    path = tmp_path / "f.txt"
    path.write_text("hello\n")
    assert w.load_text(path) == "hello\n"


def test_load_text_returns_empty_for_a_missing_file(tmp_path):
    assert w.load_text(tmp_path / "nope.txt") == "", "missing file -> '', not a crash"


# --- Report -----------------------------------------------------------------


def test_report_counts():
    r = w.Report("a.txt", {"the": 2, "cat": 1})
    assert r.total_words() == 3, "2 + 1"
    assert r.distinct_words() == 2, "two different words"


def test_report_format():
    r = w.Report("a.txt", {"the": 2, "cat": 1})
    assert r.format(5) == "a.txt: 3 words, 2 distinct\n1. the 2\n2. cat 1"


def test_report_format_respects_n():
    r = w.Report("a.txt", {"the": 3, "cat": 2, "dog": 1})
    assert r.format(1) == "a.txt: 6 words, 3 distinct\n1. the 3"


def test_report_format_defaults_to_five():
    counts = {c: i for i, c in enumerate("abcdefg", start=1)}
    lines = w.Report("a.txt", counts).format().split("\n")
    assert len(lines) == 6, "one header line plus five words, by default"


def test_report_format_when_empty():
    r = w.Report("a.txt", {})
    assert r.format(5) == "a.txt: 0 words, 0 distinct", "just the header line"


def test_report_repr():
    r = w.Report("a.txt", {"the": 2, "cat": 1})
    assert repr(r) == "Report(source='a.txt', distinct=2)"


# --- main -------------------------------------------------------------------


def test_main_with_no_arguments():
    assert w.main([]) == "usage: python3 wordfreq.py <path> [count]"


def test_main_with_a_missing_file():
    assert w.main(["missing.txt"]) == "missing.txt: file not found"


def test_main_reports_the_sample_file():
    output = w.main([str(SAMPLE), "3"])
    lines = output.split("\n")
    assert lines[0].endswith(": 25 words, 14 distinct"), "check your normalise()"
    assert lines[0].startswith(str(SAMPLE)), "the first line names the source"
    assert lines[1] == "1. the 7", "'the' appears 7 times"
    assert lines[2] == "2. cat 2", "cat and dog tie on 2; cat comes first"
    assert lines[3] == "3. dog 2"
    assert len(lines) == 4, "a header plus the 3 requested words"


def test_main_defaults_to_five_words():
    assert len(w.main([str(SAMPLE)]).split("\n")) == 6, "header plus 5 words"


def test_main_falls_back_when_the_count_is_not_a_number():
    assert w.main([str(SAMPLE), "abc"]) == w.main([str(SAMPLE)]), "fall back to 5"


def test_main_handles_an_empty_file(tmp_path):
    path = tmp_path / "empty.txt"
    path.write_text("")
    assert w.main([str(path)]) == f"{path}: 0 words, 0 distinct"
