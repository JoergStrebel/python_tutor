"""Step 4 drills -- indexing, slicing, string methods."""


def initials(full_name):
    """Return the initials of a name, uppercase, each followed by a dot.

    initials("Ada Lovelace")          -> "A.L."
    initials("grace brewster hopper") -> "G.B.H."
    initials("Prince")                -> "P."
    initials("")                      -> ""

    Practise: .split(), indexing [0], .upper(), and building a string in a loop.
    """
    raise NotImplementedError("drill 1: initials")


def reverse(text):
    """Return `text` backwards.

    reverse("Python") -> "nohtyP"
    reverse("")       -> ""

    Practise: the [::-1] slice. One line is enough.
    """
    raise NotImplementedError("drill 2: reverse")


def is_palindrome(text):
    """Return True if `text` reads the same backwards, ignoring case and spaces.

    is_palindrome("racecar")          -> True
    is_palindrome("Never odd or even") -> True
    is_palindrome("python")           -> False

    Hint: first make a cleaned version (lowercase, spaces removed), then
    compare it with its own reverse.

    Practise: .lower(), .replace(), and reusing the [::-1] slice.
    """
    raise NotImplementedError("drill 3: is_palindrome")


def title_words(sentence):
    """Capitalise the first letter of every word and normalise the spacing.

    title_words("hello wide world")   -> "Hello Wide World"
    title_words("  the   quick fox ") -> "The Quick Fox"
    title_words("")                   -> ""

    Words are separated by any amount of whitespace in the input, and by exactly
    one space in the output.

    Hint: str has a .capitalize() method that does one word.

    Practise: the split -> transform -> join round trip.
    """
    raise NotImplementedError("drill 4: title_words")


def csv_to_list(line):
    """Split a comma-separated line into a list of values with no stray spaces.

    csv_to_list("apple, pear ,plum") -> ["apple", "pear", "plum"]
    csv_to_list("solo")              -> ["solo"]
    csv_to_list("")                  -> []

    Practise: .split(",") plus .strip() on each piece.
    """
    raise NotImplementedError("drill 5: csv_to_list")


def mask_email(address):
    """Hide most of the local part of an email address.

    Keep the first character before the "@", replace every other character
    before the "@" with a "*", and leave the "@" and the domain untouched.

    mask_email("ada@lovelace.org")  -> "a**@lovelace.org"
    mask_email("bob@example.com")   -> "b**@example.com"
    mask_email("x@y.z")             -> "x@y.z"       (nothing left to mask)

    You may assume there is exactly one "@".

    Practise: .split("@"), indexing, slicing, and "*" * n to repeat a string.
    """
    raise NotImplementedError("drill 6: mask_email")
