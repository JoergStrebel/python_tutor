"""Step 3 drills -- for, range, while, break, continue."""


def sum_to(n):
    """Return 1 + 2 + ... + n. Return 0 when n is less than 1.

    sum_to(5)  -> 15
    sum_to(1)  -> 1
    sum_to(0)  -> 0

    Practise: the accumulator pattern, and range(1, n + 1) to include n.
    """
    raise NotImplementedError("drill 1: sum_to")


def count_vowels(text):
    """Return how many vowels (a, e, i, o, u) `text` contains, ignoring case.

    count_vowels("hello")  -> 2
    count_vowels("XYZ")    -> 0
    count_vowels("AEIOU")  -> 5

    Practise: looping over a string, `in` for membership, an accumulator.
    """
    raise NotImplementedError("drill 2: count_vowels")


def first_multiple_over(n, limit):
    """Return the smallest multiple of `n` that is strictly greater than `limit`.

    first_multiple_over(7, 50)   -> 56
    first_multiple_over(10, 10)  -> 20    (strictly greater, so not 10 itself)
    first_multiple_over(3, 0)    -> 3

    You may assume n is 1 or more and limit is 0 or more.

    Practise: a loop that stops early with `break` (or a `while` that stops on
    its own -- either is fine, but try `break` at least once).
    """
    raise NotImplementedError("drill 3: first_multiple_over")


def skip_negatives(numbers):
    """Return a new list containing only the numbers that are 0 or greater.

    skip_negatives([1, -2, 3, -4])  -> [1, 3]
    skip_negatives([-1, -2])        -> []
    skip_negatives([])              -> []

    Practise: `continue` to skip unwanted items, and .append() to build a list.
    (There is a much shorter way to do this -- you will meet it in step 8.
    Use the long form now.)
    """
    raise NotImplementedError("drill 4: skip_negatives")


def countdown(n):
    """Return the list [n, n-1, ..., 1]. Return [] when n is less than 1.

    countdown(5)  -> [5, 4, 3, 2, 1]
    countdown(1)  -> [1]
    countdown(0)  -> []

    Practise: a `while` loop. Make sure something in the body moves n towards
    the exit, or the loop will never end.
    """
    raise NotImplementedError("drill 5: countdown")


def times_table(n):
    """Return the n times table from 1 to 10, as a list of strings.

    times_table(3) -> ["3 x 1 = 3", "3 x 2 = 6", ..., "3 x 10 = 30"]

    Note the exact format: "{n} x {i} = {product}", with single spaces
    and a lowercase x.

    Practise: combining a loop with an f-string (step 1 coming back).
    """
    raise NotImplementedError("drill 6: times_table")
