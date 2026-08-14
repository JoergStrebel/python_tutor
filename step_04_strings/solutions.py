"""Step 4 reference solutions."""


def initials(full_name):
    result = ""
    # .split() with no argument handles any spacing and skips empty pieces,
    # so "" produces [] and the loop simply never runs.
    for word in full_name.split():
        result += word[0].upper() + "."
    return result


def reverse(text):
    # A step of -1 walks the string from the end to the start.
    return text[::-1]


def is_palindrome(text):
    # Normalise first, compare second. Doing both at once is where bugs live.
    cleaned = text.lower().replace(" ", "")
    return cleaned == cleaned[::-1]


def title_words(sentence):
    words = sentence.split()  # -> list, spacing normalised
    capitalised = []
    for word in words:
        # .capitalize() uppercases the first letter AND lowercases the rest,
        # which is usually what you want. "hELLO" -> "Hello".
        capitalised.append(word.capitalize())
    return " ".join(capitalised)  # -> back to a string


def csv_to_list(line):
    if not line:  # "".split(",") gives [""], not [] -- so handle it explicitly
        return []
    values = []
    for piece in line.split(","):
        values.append(piece.strip())
    return values


def mask_email(address):
    local, domain = address.split("@")  # unpacking a 2-item list into 2 names
    # local[0] keeps the first character; len(local) - 1 stars replace the rest.
    # "*" * 0 is "", so a one-character local part is left alone automatically.
    masked = local[0] + "*" * (len(local) - 1)
    return f"{masked}@{domain}"
