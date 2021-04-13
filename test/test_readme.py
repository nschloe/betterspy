import pathlib

import exdown

this_dir = pathlib.Path(__file__).resolve().parent

test_readme = exdown.pytests(this_dir / ".." / "README.md", syntax_filter="python")
