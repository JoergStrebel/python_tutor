"""Test-support loader for the Python tutor drills.

Every step's test file begins with these two lines:

    from pytutor import load
    m = load(__file__)

`load` imports the `exercises.py` that sits next to that test file, so the tests
always check *your* work. Setting the environment variable PYTUTOR_SOLUTIONS=1
makes it import `solutions.py` instead -- that is how the reference answers were
checked against the very same tests.

You do not need to understand this file to do the tutorial. Come back to it after
step 9 if you are curious; it uses `pathlib`, `os.environ` and the import system.
"""

import importlib.util
import os
from pathlib import Path


def load(test_file):
    """Import and return the module under test for the step containing `test_file`.

    Pass `__file__` from inside a test module.
    """
    step_dir = Path(test_file).resolve().parent
    use_solutions = os.environ.get("PYTUTOR_SOLUTIONS") == "1"
    module_name = "solutions" if use_solutions else "exercises"
    path = step_dir / f"{module_name}.py"

    if not path.exists():
        raise FileNotFoundError(f"Expected to find {path}, but it is not there.")

    # A unique module name per step keeps step_03's `exercises` from colliding
    # with step_04's in sys.modules.
    spec = importlib.util.spec_from_file_location(
        f"{step_dir.name}__{module_name}", path
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module
