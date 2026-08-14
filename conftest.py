"""pytest configuration.

Its only job is to make sure the tutorial root is importable, so that every
step's test file can do `from pytutor import load` no matter which directory you
run pytest from.
"""

import sys
from pathlib import Path

ROOT = str(Path(__file__).resolve().parent)
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)
