"""Capstone -- a word frequency tool.

Read ../CAPSTONE.md for the full specification, then fill in the stubs below.
There is no solutions file: the tests in test_capstone.py ARE the spec.

Build it one function at a time, top to bottom. Each is testable before the
next one exists:

    pytest capstone/ -k normalise
    pytest capstone/ -k count_words
    ...
"""

import string
import sys
from pathlib import Path  # noqa: F401 -- you will need this for load_text/main


def normalise(text):
    """Turn raw text into a list of lowercase words with no edge punctuation.

    normalise("The cat, the CAT!")  -> ["the", "cat", "the", "cat"]
    normalise("--- ...")            -> []
    normalise("")                   -> []

    Only the ENDS of each word are stripped, so "don't" keeps its apostrophe.
    `string.punctuation` is a string of every punctuation character, and
    str.strip() accepts them all at once.

    Steps 4 and 8.
    """
    raise NotImplementedError("normalise")


def count_words(words):
    """Count how often each word appears. Step 6's counting idiom, unchanged."""
    raise NotImplementedError("count_words")


def top_n(counts, n):
    """Return the n most common (word, count) pairs, most frequent first.

    Ties are broken alphabetically, so the result is always predictable:

        top_n({"b": 2, "a": 2, "c": 1}, 2)  -> [("a", 2), ("b", 2)]

    Hint: a `key` function returning a TUPLE sorts by the first element, then
    by the second. A minus sign turns a numeric sort round.

    Step 8.
    """
    raise NotImplementedError("top_n")


def load_text(path):
    """Return the contents of the file, or "" if it does not exist.

    A missing file is a normal outcome here, not a crash.

    Step 9.
    """
    raise NotImplementedError("load_text")


class Report:
    """The result of analysing one file. Step 10.

    Report("a.txt", {"the": 2, "cat": 1})
        .total_words()     -> 3
        .distinct_words()  -> 2
        .format(5)         -> "a.txt: 3 words, 2 distinct\\n1. the 2\\n2. cat 1"
        repr(...)          -> "Report(source='a.txt', distinct=2)"
    """

    def __init__(self, source, counts):
        raise NotImplementedError("Report.__init__")

    def total_words(self):
        raise NotImplementedError("Report.total_words")

    def distinct_words(self):
        raise NotImplementedError("Report.distinct_words")

    def format(self, n=5):
        """Return the whole report as one string, lines joined by "\\n".

        First line:  "<source>: <total> words, <distinct> distinct"
        Then one line per word:  "<position>. <word> <count>"

        There is no trailing newline, and a report with no words is just the
        first line.
        """
        raise NotImplementedError("Report.format")

    def __repr__(self):
        raise NotImplementedError("Report.__repr__")


def main(argv):
    """Turn command-line arguments into the string that should be printed.

    argv is the argument list WITHOUT the program name.

        []                     -> "usage: python3 wordfreq.py <path> [count]"
        ["missing.txt"]        -> "missing.txt: file not found"
        ["sample.txt"]         -> the report, top 5
        ["sample.txt", "3"]    -> the report, top 3
        ["sample.txt", "abc"]  -> the report, top 5 (unparseable count -> default)

    Returning the text instead of printing it is what makes this testable.

    Watch out: load_text() gives "" for a missing file AND for an empty one, so
    it cannot tell you which happened. Path(path).exists() can -- an empty file
    still gets a report.

    Steps 2, 7 and 9.
    """
    raise NotImplementedError("main")


if __name__ == "__main__":
    # This block runs only when the file is executed directly, never when it is
    # imported -- which is why the tests can import this module safely.
    # sys.argv[0] is the script name, so [1:] drops it.
    print(main(sys.argv[1:]))
