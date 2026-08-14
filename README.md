# Python in 10 Steps — a Muscle-Memory Tutorial

Ten steps, sixty drills, one capstone. The aim is not to *know about* Python's
core constructs but to type them without thinking — so that when you have an
idea, the syntax is not in the way.

Everything here runs with a plain Python 3 install. Four small packages carry
the tests and the recall quiz. No frameworks, no accounts, no internet after
the first install.

## Setup

```bash
cd python_tutor
python3 -m venv .venv               # already there? skip this line
source .venv/bin/activate
pip install -r requirements.txt
```

With the virtual environment active, `python3` and `pytest` both come from
`.venv`, so the tutorial no longer depends on which Python happens to be first
on your `PATH`. Check it with `python3 --version` (3.9 or newer) and
`pytest --version`.

Run everything from this directory — the tests find each other relative to it.

## The study loop

The method matters as much as the material. For each step:

1. **Read the syntax card** at the top of the step's `README.md`. Then close it.
2. **Run the examples** and read the output alongside the source:
   ```bash
   python3 step_01_values/examples.py
   ```
   Change a value, run it again, see what happens. Break it on purpose.
3. **Fill in `exercises.py`**, one drill at a time. Replace each
   `raise NotImplementedError` with real code. Type it out; do not paste.
4. **Run the tests** until they are green:
   ```bash
   pytest step_01_values/
   ```
   Read the failure messages — they name the drill and say what was expected.
5. **Compare with `solutions.py`.** Not to check whether you were right (the
   tests did that) but to see whether there was a shorter way to say it.
6. **Do the recall drill** at the bottom of the step README, from memory, in a
   scratch file.
7. **The next day, before starting the new step**, run the recall quiz on the
   step you just finished:
   ```bash
   python3 quiz.py 1
   ```
   It names the thing you are trying to do and you write how you do it; then it
   shows you the card and you say whether you had it. This spacing is what turns
   recognition into recall. It takes two minutes and it is the highest-value
   part of the whole tutorial.

   The quiz asks for one idiom at a time, on purpose. What you want to own is
   the generic form — "count down" → `for i in range(5, 0, -1):` — not a page
   reproduced word for word. If you would rather work on paper, re-typing the
   card from `CHEATSHEET.md` without looking does the same job.

One step per session is a good pace. Two is fine. Ten in a weekend will not
stick, because muscle memory is built by spacing, not by volume.

## The ten steps

| # | Step | What you drill |
|---|------|----------------|
| 1 | [`step_01_values`](step_01_values/) | Variables, `int`/`float`/`str`/`bool`, f-strings, conversion |
| 2 | [`step_02_conditionals`](step_02_conditionals/) | `if`/`elif`/`else`, comparisons, `and`/`or`/`not`, truthiness |
| 3 | [`step_03_loops`](step_03_loops/) | `for`, `range`, `while`, `break`, `continue`, the accumulator |
| 4 | [`step_04_strings`](step_04_strings/) | Indexing, slicing, `.split`/`.join`/`.strip`, immutability |
| 5 | [`step_05_lists_tuples`](step_05_lists_tuples/) | List methods, mutation, tuples, unpacking |
| 6 | [`step_06_dicts_sets`](step_06_dicts_sets/) | `dict` lookup and `.get`, `.items()`, sets, counting |
| 7 | [`step_07_functions`](step_07_functions/) | Defaults, keyword args, `*args`/`**kwargs`, scope, closures |
| 8 | [`step_08_comprehensions`](step_08_comprehensions/) | Comprehensions, `enumerate`, `zip`, `sorted(key=)`, `lambda` |
| 9 | [`step_09_errors_files`](step_09_errors_files/) | `try`/`except`/`else`/`finally`, `raise`, `with open`, `pathlib` |
| 10 | [`step_10_classes`](step_10_classes/) | `class`, `__init__`, `self`, `__repr__`, `@dataclass` |

Then: **[`CAPSTONE.md`](CAPSTONE.md)** — one program that uses all ten at once.

The order is deliberate. Strings come before lists so that slicing is learned on
text you can see, then transfers unchanged. Functions come at 7 even though every
drill from step 1 is *written* as a function — by the time `def` is formally
taught, its shape is already familiar. Comprehensions come after the explicit
loops they replace, so they feel like a relief rather than a riddle.

## Files in each step

| File | What it is |
|------|-----------|
| `README.md` | The lesson: syntax card, explanation, the errors you will hit, recall drill |
| `examples.py` | Runnable, annotated demonstrations. Read the output next to the code |
| `exercises.py` | **The file you edit.** Six drills as function stubs |
| `solutions.py` | Reference answers with comments explaining the *why* |
| `test_step_NN.py` | The checks. You do not need to edit these, but do read them |

## Useful commands

```bash
pytest                            # every step at once
pytest step_04_strings/           # one step
pytest -x                         # stop at the first failure
pytest -k palindrome              # just the drills matching a name
pytest -q                         # quieter output
python3 -i step_01_values/solutions.py   # load a module and poke at it live

python3 quiz.py 4                 # drill the strings card
python3 quiz.py 1 2 3             # drill several cards
python3 quiz.py --all -n 12       # twelve cards from anywhere -- the two minutes
python3 quiz.py --shuffle 6       # same card, random order
python3 quiz.py --list            # what the sections are
```

## If you get stuck

- **Read the traceback from the bottom up.** The last line names the error type
  and the problem; the lines above show how you got there. Each step README
  lists the specific errors that step tends to produce.
- **Print the thing.** `print(type(x), repr(x))` answers "what have I actually
  got here?", which is the question behind most beginner bugs.
- **Try it in the REPL.** Run `python3` with no arguments and experiment. There
  is no faster feedback loop.
- **Peek at the solution, then close it and retype the drill from scratch.**
  Reading a solution teaches you very little; reproducing it teaches you a lot.

## A note on the tests

Tests check *behaviour*, not implementation. If a drill says "practise slicing"
and you solve it with a loop, the test will still pass — but you will have
skipped the rep. The drills are suggestions your fingers benefit from following.

`pytutor.py` and `conftest.py` at the root are plumbing that lets the test files
find your `exercises.py`. You can ignore them; come back after step 9 if curious.

`quiz.py` is the recall quiz and `quiz_bank.py` holds its questions — one card
per idiom on the cheatsheet. `test_quiz.py` checks that the two files still
agree with `CHEATSHEET.md`, so if you edit the cheatsheet, run it.
