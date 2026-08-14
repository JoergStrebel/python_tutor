"""Tests for the quiz bank. Run with:  pytest test_quiz.py

The quiz keeps its questions in quiz_bank.py rather than reading CHEATSHEET.md,
which buys clean hints at the risk of the two drifting apart. These tests are
what stop that happening: every answer in the bank must still appear on the
cheatsheet, and every section must still be named the same in both places.

They import quiz_bank only -- never quiz.py -- so they keep working even when
rich and prompt_toolkit are not installed.
"""

import re
from pathlib import Path

import quiz_bank

CHEATSHEET = Path(__file__).resolve().parent / "CHEATSHEET.md"


def cheatsheet_text():
    """The cheatsheet with its backticks removed.

    Sections 1-10 quote code out of fenced blocks, which have no backticks
    inside them. Section 11 quotes the error table, where Markdown wraps the
    code in `backticks`. Dropping them everywhere lets one comparison serve
    both.
    """
    return CHEATSHEET.read_text().replace("`", "")


def test_every_answer_still_appears_on_the_cheatsheet():
    """The bank must never teach something the cheatsheet does not say."""
    text = cheatsheet_text()
    for card in quiz_bank.CARDS:
        for line in card.answer.replace("`", "").splitlines():
            if not line.strip():
                continue
            assert line.strip() in text, (
                f"section {card.section}, hint {card.hint!r}: the line "
                f"{line.strip()!r} is in quiz_bank.py but not in "
                f"CHEATSHEET.md -- one of the two is out of date"
            )


def test_section_titles_match_the_cheatsheet_headings():
    """SECTIONS and the ## headings must agree, or the quiz lies about itself."""
    headings = dict(
        (int(number), title.strip())
        for number, title in re.findall(
            r"^## (\d+) — (.+)$", CHEATSHEET.read_text(), re.MULTILINE
        )
    )
    for number, title in headings.items():
        assert quiz_bank.SECTIONS.get(number) == title, (
            f"CHEATSHEET.md calls section {number} {title!r} but quiz_bank.py "
            f"calls it {quiz_bank.SECTIONS.get(number)!r}"
        )


def test_every_section_has_cards():
    """A section with two cards is not a drill. Six is the floor."""
    for number, title in quiz_bank.SECTIONS.items():
        cards = [c for c in quiz_bank.CARDS if c.section == number]
        assert len(cards) >= 6, (
            f"section {number} ({title}) has only {len(cards)} cards -- "
            f"too few to be worth running"
        )


def test_every_card_belongs_to_a_known_section():
    for card in quiz_bank.CARDS:
        assert card.section in quiz_bank.SECTIONS, (
            f"card {card.hint!r} claims section {card.section}, "
            f"which is not in SECTIONS"
        )


def test_no_two_cards_share_a_hint():
    """Two cards with one hint means a question with two right answers."""
    seen = {}
    for card in quiz_bank.CARDS:
        assert card.hint not in seen, (
            f"the hint {card.hint!r} is used by section {seen.get(card.hint)} "
            f"and section {card.section} -- one of them needs rewording"
        )
        seen[card.hint] = card.section


def test_no_card_is_empty():
    for card in quiz_bank.CARDS:
        assert card.hint.strip(), f"section {card.section} has a card with no hint"
        assert card.answer.strip(), f"the card {card.hint!r} has no answer"
