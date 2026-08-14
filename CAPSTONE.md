# Capstone — a Word Frequency Tool

Ten steps taught the constructs one at a time. Real programs use them all at
once, and switching between them fluidly is the actual skill. This capstone is
one small command-line tool that touches every step.

There is **no solutions file** for this one. That is deliberate: the tests are
your specification, and working from a spec rather than a model answer is what
you will be doing from here on.

## What you are building

A tool that reads a text file and reports its most common words:

```bash
$ python3 capstone/wordfreq.py capstone/sample.txt 3
capstone/sample.txt: 25 words, 14 distinct
1. the 7
2. cat 2
3. dog 2
```

(`cat` and `dog` both appear twice, as do `mat`, `on` and `sat` — the
alphabetical tie-break is what decides the order.)

## Where each step shows up

| Step | Where you will need it |
|---|---|
| 1 Values, f-strings | Every line of output |
| 2 Conditionals | Missing file, missing argument, bad count |
| 3 Loops | Walking words and building the report |
| 4 Strings | `.lower()`, `.split()`, stripping punctuation, `"\n".join()` |
| 5 Lists & tuples | The `(word, count)` pairs |
| 6 Dicts & sets | The counting idiom |
| 7 Functions | Defaults (`n=5`), and splitting the job into small pieces |
| 8 Comprehensions | `normalise`, `enumerate` for numbering, `sorted(key=...)` |
| 9 Errors & files | Reading the file, handling a missing one, `parse_int` again |
| 10 Classes | The `Report` class holding the result |

## The specification

Write these in `capstone/wordfreq.py`. The stubs are already there.

### `normalise(text)` → list of words

Lowercase the text, split it on whitespace, strip punctuation off both ends of
each word, and drop anything left empty.

```python
normalise("The cat, the CAT!")   -> ["the", "cat", "the", "cat"]
normalise("--- ...")             -> []
normalise("")                    -> []
```

Use `string.punctuation` — `import string` gives you the set of punctuation
characters, and `str.strip` accepts them all at once.

Note that `"don't"` keeps its apostrophe: only the *ends* are stripped.

### `count_words(words)` → dict

Map each word to how often it appears. The step 6 counting idiom, unchanged.

### `top_n(counts, n)` → list of `(word, count)` tuples

Most frequent first. **Ties are broken alphabetically**, so the output is
predictable:

```python
top_n({"b": 2, "a": 2, "c": 1}, 2)   -> [("a", 2), ("b", 2)]
```

Hint: `sorted` with a `key` returning a tuple sorts by the first element, then
the second. A minus sign flips a numeric sort to descending.

### `load_text(path)` → str

Return the file's contents, or `""` if the file does not exist. A missing file
is a normal outcome here, not a crash.

### `class Report`

```python
Report(source, counts)          # source is the path as a string
report.total_words()            # how many words in total
report.distinct_words()         # how many different words
report.format(n=5)              # the printable report, as one string
repr(report)                    # "Report(source='a.txt', distinct=19)"
```

`format` returns these lines joined with `"\n"` (no trailing newline):

```
<source>: <total> words, <distinct> distinct
1. <word> <count>
2. <word> <count>
```

A report with no words at all is just its first line: `"a.txt: 0 words, 0 distinct"`.

If the file has fewer distinct words than `n`, you simply get fewer lines — no
padding, no error.

### `main(argv)` → str

`argv` is the argument list *without* the program name. It returns the string to
print rather than printing it — which is what makes it testable.

| Input | Result |
|---|---|
| `[]` | `"usage: python3 wordfreq.py <path> [count]"` |
| `["missing.txt"]` | `"missing.txt: file not found"` |
| `["sample.txt"]` | the report, top 5 |
| `["sample.txt", "3"]` | the report, top 3 |
| `["sample.txt", "abc"]` | the report, top 5 — an unparseable count falls back to the default |

Note the trap: `load_text` returns `""` for a missing file *and* for an empty
one, so `main` cannot tell them apart from the text alone. Use
`Path(path).exists()` to distinguish them — an empty file still gets a report.

The `if __name__ == "__main__":` block at the bottom is already written for you.
It is the standard way to say "run this only when the file is executed directly,
not when it is imported" — which is exactly why the tests can import your module
without it running.

## Working on it

```bash
pytest capstone/                  # the whole spec
pytest capstone/ -x               # stop at the first failure
pytest capstone/ -k normalise     # one function at a time

python3 capstone/wordfreq.py capstone/sample.txt 3
```

Build it one function at a time, in the order above — each one is testable
before the next exists.

## When it passes

Try extending it. None of these are tested; they are for you.

- A `--min-length` option so short words can be ignored.
- Ignore a stopword list (`the`, `a`, `and`, ...) loaded from a second file.
- Report the percentage each word makes up of the total.
- Accept several files and merge the counts.
- Draw a bar chart with `"#" * count`.
