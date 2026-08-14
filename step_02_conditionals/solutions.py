"""Step 2 reference solutions."""


def sign(n):
    if n < 0:
        return -1
    elif n > 0:
        return 1
    else:
        return 0
    # Note: because `return` leaves the function immediately, plain `if`s would
    # work here too. The elif chain still reads better -- it announces "these
    # three cases are alternatives".


def is_even(n):
    # `n % 2 == 0` is ALREADY True or False. Wrapping it in an if/else to return
    # True or False is redundant -- just return the comparison.
    return n % 2 == 0


def grade(score):
    # The order is the whole trick: check the highest band first. Once a branch
    # matches, the rest are skipped, so "score >= 80" implicitly means
    # "between 80 and 89" by the time we reach it.
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
    # Read it as: divisible by 4, and either not a century year, or a
    # 400-multiple. Python evaluates `and` before `or`, so the parentheses
    # here are for the human reader, not strictly required.
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def can_vote(age, is_citizen):
    # `age >= 18` is a bool and `is_citizen` is a bool, so `and` gives a bool.
    return age >= 18 and is_citizen


def describe_empty(value):
    # One rule covers str, list, dict, tuple, set, 0 and None at once. This is
    # why truthiness is worth learning: you write far less code.
    return "empty" if not value else "has content"
