"""Step 2 drills -- if / elif / else, comparisons, truthiness."""


def sign(n):
    """Return -1 if n is negative, 0 if it is zero, 1 if it is positive.

    Practise: a three-way if / elif / else.
    """
    if n > 0:
        return 1
    elif n == 0 or n == 0.0:
        return 0
    else:
        return -1


def is_even(n):
    """Return True if n is even, False if it is odd.

    Hint: the remainder operator is %. `n % 2` is 0 for even numbers.
    Try to return the comparison directly rather than writing
    `if ...: return True else: return False`.
    """
    return n % 2 == 0


def grade(score):
    """Turn a 0-100 score into a letter grade.

    90 and above -> "A"
    80 to 89     -> "B"
    70 to 79     -> "C"
    60 to 69     -> "D"
    below 60     -> "F"

    Practise: an elif chain, ordered so the first match is the right one.
    """
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


def is_leap_year(year):
    """Return True if `year` is a leap year in the Gregorian calendar.

    The rule has three parts:
      - divisible by 4        -> leap
      - unless divisible by 100 -> not leap
      - unless divisible by 400 -> leap after all

    So 2024 is a leap year, 1900 is not, 2000 is.

    Practise: combining conditions with and / or.
    """
    divisibleby4 = year % 4 == 0
    divisibleby100 = year % 100 == 0
    divisibleby400 = year % 400 == 0
    return divisibleby4 and (not divisibleby100 or divisibleby400)


def can_vote(age, is_citizen):
    """Return True only if the person is at least 18 AND a citizen.

    Practise: `and`, and returning a boolean expression directly.
    """
    return age >= 18 and is_citizen


def describe_empty(value):
    """Return "empty" if `value` is falsy, otherwise "has content".

    describe_empty("")      -> "empty"
    describe_empty([])      -> "empty"
    describe_empty(0)       -> "empty"
    describe_empty("hi")    -> "has content"
    describe_empty([0])     -> "has content"   (a list holding a 0 is not empty!)

    Practise: truthiness. Do NOT test each type separately -- let Python's own
    rule do the work with `if not value:` or a conditional expression.
    """
    return "empty" if not value else "has content"

def sign(a):
    if a>0:
        return "positive"
    elif a == 0:
        return "zero"
    else:
        return "negative"
# False, 0, 0.0 , [], {} , "", None, (), set()
