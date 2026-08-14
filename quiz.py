#!/usr/bin/env python3
"""The recall drill: the quiz side of CHEATSHEET.md.

Run it the day after a step, before starting the next one:

    python3 quiz.py 3

It tells you what you are trying to do and you write how you do it. Then it
shows you the card and you say whether you had it. Nobody compares your text
to the answer -- there are five right ways to write most of these, and you are
a better judge of your own recall than any string comparison would be.

    python3 quiz.py 3            one section
    python3 quiz.py 1 2 3        several
    python3 quiz.py --all -n 12  twelve cards from anywhere -- the two minutes
    python3 quiz.py --list       what the sections are

The questions live in quiz_bank.py.
"""

import argparse
import random
import sys

MISSING = """
  The quiz needs a couple of packages that are not installed yet
  (it could not find {name}).

      cd python_tutor
      ./.venv/bin/pip install -r requirements.txt

  Or, with the virtual environment active:  pip install -r requirements.txt
"""

try:
    from prompt_toolkit import PromptSession
    from prompt_toolkit.formatted_text import HTML
    from prompt_toolkit.key_binding import KeyBindings
    from prompt_toolkit.lexers import PygmentsLexer, SimpleLexer
    from pygments.lexers.python import PythonLexer
    from rich.box import ROUNDED, SIMPLE
    from rich.console import Console
    from rich.panel import Panel
    from rich.syntax import Syntax
    from rich.table import Table
    from rich.text import Text
except ImportError as err:
    sys.exit(MISSING.format(name=err.name))

import quiz_bank

# ansi_dark paints with the terminal's own sixteen colours instead of a fixed
# palette, so the cards stay readable on a light background too.
THEME = "ansi_dark"
INDENT = "    "
BAR_WIDTH = 12

console = Console()


# --- putting a card on the screen ------------------------------------------

def is_code(card):
    """Section 11 answers are English. Everything else is Python."""
    return card.section != quiz_bank.PROSE_SECTION


def render(card):
    """The answer as a renderable -- highlighted Python, or plain text."""
    if is_code(card):
        # background_color="default" stops rich painting a dark box behind the
        # code on a light terminal.
        return Syntax(card.answer, "python", theme=THEME,
                      background_color="default")
    return Text(card.answer)


def print_header(card, position, total):
    """The section name on the left, how far along you are on the right."""
    done = round(BAR_WIDTH * (position - 1) / total)
    bar = "█" * done + "░" * (BAR_WIDTH - done)

    grid = Table.grid(expand=True)
    grid.add_column(justify="left")
    grid.add_column(justify="right")
    grid.add_row(
        Text(f"Section {card.section} — {quiz_bank.SECTIONS[card.section]}",
             style="bold"),
        Text(f"{bar}  {position}/{total}", style="dim"),
    )
    console.print()
    console.print(grid)


def print_hint(card):
    label = "you see" if card.section == quiz_bank.PROSE_SECTION else "hint"
    console.print(Panel(Text(card.hint), title=label, title_align="left",
                        border_style="cyan", box=ROUNDED, expand=False))


def print_answer(card):
    console.print(Panel(render(card), title="answer", title_align="left",
                        border_style="blue", box=ROUNDED, expand=False))
    if card.note:
        # Assembled rather than marked up, so a note containing brackets or
        # angle brackets is printed and not parsed.
        console.print(Text.assemble(("  note  ", "dim"), (card.note, "italic")))


# --- reading what the learner types -----------------------------------------

def gutter(width, line_number, is_soft_wrap):
    """The line numbers down the left of a multi-line answer."""
    return f"{line_number + 1:>3} │ "


# prompt_toolkit's PromptSession stores what you pass to .prompt() -- those
# are settings on the session, not arguments to one call -- and an argument
# left at None means "keep the old value", not "none of these". That is why
# the y/n/q keys read_grade() binds used to stay bound: typing "n" as the
# first letter of the next answer exited the prompt instead of writing an n.
# read_line() is the cure: it states every sticky setting on every call.
PLAIN = SimpleLexer()      # plain text; None would mean "keep the old lexer"
NO_KEYS = KeyBindings()    # nothing beyond prompt_toolkit's own editing keys


def read_line(session, message, *, lexer=PLAIN, keys=NO_KEYS,
              multiline=False, continuation=gutter):
    """One prompt, with nothing inherited from the prompt before it."""
    return session.prompt(
        message,
        lexer=lexer,
        key_bindings=keys,
        multiline=multiline,
        prompt_continuation=continuation,
    )


def editing_keys():
    """Enter opens an indented new line; Esc then Enter hands the answer in.

    prompt_toolkit has no auto-indent of its own, and typing a class body
    without one is miserable, so this supplies it: a new line starts at the
    same indentation as the one you just left, four spaces deeper if that line
    ended in a colon.
    """
    keys = KeyBindings()

    @keys.add("enter")
    def _(event):
        line = event.current_buffer.document.current_line_before_cursor
        indent = line[:len(line) - len(line.lstrip())]
        if line.rstrip().endswith(":"):
            indent += INDENT
        event.current_buffer.insert_text("\n" + indent)

    @keys.add("escape", "enter")
    def _(event):
        event.current_buffer.validate_and_handle()

    return keys


def read_answer(session, card):
    """Read the attempt, syntax-highlighted as it is typed.

    One-line answers end at Enter, so the common case stays one keystroke.
    Multi-line answers free Enter up for opening a new line, which is what
    makes going back and fixing line 2 possible.
    """
    multiline = "\n" in card.answer
    lexer = PygmentsLexer(PythonLexer) if is_code(card) else PLAIN

    if multiline:
        console.print(Text("  several lines — press Esc then Enter to hand it in",
                           style="dim"))

    return read_line(
        session,
        "  1 │ " if multiline else "  > ",
        lexer=lexer,
        keys=editing_keys() if multiline else NO_KEYS,
        multiline=multiline,
    )


def read_grade(session):
    """Wait for a single y, n or q. No Enter needed."""
    keys = KeyBindings()
    for key in ("y", "n", "q"):
        keys.add(key)(lambda event, key=key: event.app.exit(result=key))

    message = HTML("  got it?  <b>y</b> yes   <b>n</b> no   <b>q</b> stop  ")
    while True:
        answer = read_line(session, message, keys=keys)
        if answer in ("y", "n", "q"):
            return answer


def confirm(session, question):
    answer = read_line(session, f"  {question} [y/N] ")
    return answer.strip().lower().startswith("y")


# --- the session ------------------------------------------------------------

def ask(session, card, position, total):
    """Put one card. True if recalled, False if not, None if you stopped."""
    print_header(card, position, total)
    print_hint(card)
    # What you type is deliberately thrown away. Typing it is the exercise;
    # judging it is your job, not the program's.
    read_answer(session, card)
    print_answer(card)

    grade = read_grade(session)
    if grade == "q":
        return None

    recalled = grade == "y"
    console.print(Text("  ✓ recalled" if recalled else "  ✗ look at it again",
                       style="green" if recalled else "yellow"))
    return recalled


def first_line(answer):
    lines = answer.splitlines()
    return lines[0] + (" ..." if len(lines) > 1 else "")


def print_summary(asked, recalled, missed):
    console.print()
    console.rule(style="dim")
    if not asked:
        console.print("  Nothing asked yet.")
        return

    console.print(Text(f"  {recalled} of {asked} recalled.", style="bold"))
    if not missed:
        console.print(Text("  Nothing to revisit. Go and do the next step.",
                           style="green"))
        return

    table = Table(box=SIMPLE, show_header=False, padding=(0, 2))
    table.add_column(style="cyan", no_wrap=False)
    table.add_column()
    for card in missed:
        table.add_row(card.hint, first_line(card.answer))
    console.print(Panel(table, title="worth another look", title_align="left",
                        border_style="yellow", box=ROUNDED, expand=False))


def run(session, cards):
    """Ask every card, print the score, and hand back the ones that missed."""
    asked = 0
    recalled = 0
    missed = []

    try:
        for position, card in enumerate(cards, start=1):
            outcome = ask(session, card, position, len(cards))
            if outcome is None:
                break
            asked += 1
            if outcome:
                recalled += 1
            else:
                missed.append(card)
    except (KeyboardInterrupt, EOFError):
        # Ctrl-C is a legitimate way to stop. You still get your score.
        console.print()

    print_summary(asked, recalled, missed)
    return missed


# --- choosing what to be asked ----------------------------------------------

def cards_in(section):
    return [card for card in quiz_bank.CARDS if card.section == section]


def select(sections, shuffle, count):
    """Pick the cards to ask, out of quiz_bank.CARDS."""
    cards = [card for card in quiz_bank.CARDS if card.section in sections]

    if count and count < len(cards):
        chosen = random.sample(cards, count)
        # A sample comes back in random order; put it back into cheatsheet
        # order unless a shuffle was asked for.
        chosen.sort(key=cards.index)
        cards = chosen

    if shuffle:
        random.shuffle(cards)

    return cards


def print_sections():
    table = Table(box=SIMPLE, header_style="bold")
    table.add_column("", justify="right")
    table.add_column("section")
    table.add_column("cards", justify="right")
    for number, title in quiz_bank.SECTIONS.items():
        table.add_row(str(number), title, str(len(cards_in(number))))
    console.print(table)


def choose_section(session):
    """The menu, for a bare `python3 quiz.py`."""
    print_sections()
    while True:
        answer = read_line(session, "  which section? ")
        answer = answer.strip()
        if answer.isdigit() and int(answer) in quiz_bank.SECTIONS:
            return int(answer)
        console.print(Text("  pick one of the numbers above.", style="yellow"))


EXAMPLES = """examples:
  python3 quiz.py 3            drill section 3
  python3 quiz.py 1 2 3        drill several sections
  python3 quiz.py --all        every card, in order
  python3 quiz.py 4 --shuffle  section 4 in random order
  python3 quiz.py --all -n 12  twelve cards from anywhere
  python3 quiz.py --list       the sections and their card counts
"""


def parse_args(argv):
    parser = argparse.ArgumentParser(
        prog="quiz.py",
        description="Recall drill for the syntax cards in CHEATSHEET.md.",
        epilog=EXAMPLES,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("sections", nargs="*", type=int, metavar="N",
                        help="section numbers to drill (1-11)")
    parser.add_argument("-a", "--all", action="store_true",
                        help="drill every section")
    parser.add_argument("-s", "--shuffle", action="store_true",
                        help="ask the cards in random order")
    parser.add_argument("-n", "--count", type=int, metavar="N",
                        help="stop after N cards, chosen at random")
    parser.add_argument("-l", "--list", action="store_true",
                        help="list the sections and exit")

    args = parser.parse_args(argv)
    unknown = [n for n in args.sections if n not in quiz_bank.SECTIONS]
    if unknown:
        parser.error(
            f"no such section: {', '.join(str(n) for n in unknown)}. "
            f"Try --list."
        )
    if args.count is not None and args.count < 1:
        parser.error("--count needs to be at least 1")
    return args


def main(argv=None):
    args = parse_args(argv)

    if args.list:
        print_sections()
        return 0

    session = PromptSession()

    try:
        if args.all:
            sections = list(quiz_bank.SECTIONS)
        elif args.sections:
            sections = args.sections
        else:
            sections = [choose_section(session)]

        cards = select(sections, args.shuffle, args.count)
        missed = run(session, cards)
        while missed and confirm(session,
                                 f"Run the {len(missed)} you missed again?"):
            missed = run(session, missed)
    except (KeyboardInterrupt, EOFError):
        console.print(Text("\n  Stopped. Come back tomorrow.", style="dim"))
        return 0

    console.print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
