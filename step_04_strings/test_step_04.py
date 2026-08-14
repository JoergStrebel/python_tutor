"""Tests for step 4. Run with:  pytest step_04_strings/"""

from pytutor import load

m = load(__file__)


def test_drill_1_initials():
    assert m.initials("Ada Lovelace") == "A.L.", "two names -> two initials"
    assert m.initials("grace brewster hopper") == "G.B.H.", "initials are uppercased"
    assert m.initials("Prince") == "P.", "a single name still gets its dot"
    assert m.initials("") == "", "no name -> no initials"
    assert m.initials("  spaced   out  ") == "S.O.", "extra spacing is ignored"


def test_drill_2_reverse():
    assert m.reverse("Python") == "nohtyP", "reversed character by character"
    assert m.reverse("") == "", "an empty string reverses to itself"
    assert m.reverse("a") == "a", "a single character reverses to itself"
    assert m.reverse("ab cd") == "dc ba", "spaces move too"


def test_drill_3_is_palindrome():
    assert m.is_palindrome("racecar") is True, "racecar is a palindrome"
    assert m.is_palindrome("Never odd or even") is True, "ignore case and spaces"
    assert m.is_palindrome("python") is False, "python is not a palindrome"
    assert m.is_palindrome("") is True, "an empty string counts as a palindrome"
    assert m.is_palindrome("Anna") is True, "case must be ignored"


def test_drill_4_title_words():
    assert m.title_words("hello wide world") == "Hello Wide World", "capitalise each"
    assert m.title_words("  the   quick fox ") == "The Quick Fox", "normalise spacing"
    assert m.title_words("") == "", "empty in, empty out"
    assert m.title_words("one") == "One", "a single word works"
    assert m.title_words("hELLO wORLD") == "Hello World", "the rest is lowercased"


def test_drill_5_csv_to_list():
    assert m.csv_to_list("apple, pear ,plum") == ["apple", "pear", "plum"], "strip each"
    assert m.csv_to_list("solo") == ["solo"], "no comma -> one item"
    assert m.csv_to_list("") == [], 'empty line -> [], not [""]'
    assert m.csv_to_list("a,b,c") == ["a", "b", "c"], "no spaces to strip is fine"


def test_drill_6_mask_email():
    assert m.mask_email("ada@lovelace.org") == "a**@lovelace.org", "keep 1st, star 2"
    assert m.mask_email("bob@example.com") == "b**@example.com", "same shape"
    assert m.mask_email("x@y.z") == "x@y.z", "one character -> nothing to mask"
    assert (
        m.mask_email("verylongname@d.io") == "v***********@d.io"
    ), "11 stars for the 11 remaining characters"
