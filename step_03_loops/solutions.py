"""Step 3 reference solutions."""


def sum_to(n):
    total = 0
    # range(1, n + 1) is how you include n itself. When n < 1 this range is
    # empty, so the loop body never runs and we correctly return 0.
    for i in range(1, n + 1):
        total += i
    return total


def count_vowels(text):
    count = 0
    for letter in text.lower():  # lower() once, up front, rather than per test
        if letter in "aeiou":  # `in` on a string checks for a substring
            count += 1
    return count


def first_multiple_over(n, limit):
    # Start at n and keep stepping by n. `limit // n + 2` is a generous upper
    # bound that is guaranteed to overshoot, so the break always fires.
    for i in range(1, limit // n + 2):
        candidate = n * i
        if candidate > limit:
            return candidate  # `return` leaves the loop as surely as `break`

    # A `while` version, for comparison:
    #   candidate = n
    #   while candidate <= limit:
    #       candidate += n
    #   return candidate


def skip_negatives(numbers):
    kept = []
    for n in numbers:
        if n < 0:
            continue  # skip this one, carry on with the next
        kept.append(n)
    return kept


def countdown(n):
    result = []
    current = n
    while current > 0:  # when n < 1 this is false immediately -> []
        result.append(current)
        current -= 1  # the line that makes the loop finish
    return result


def times_table(n):
    rows = []
    for i in range(1, 11):  # 1 to 10 inclusive
        rows.append(f"{n} x {i} = {n * i}")
    return rows
