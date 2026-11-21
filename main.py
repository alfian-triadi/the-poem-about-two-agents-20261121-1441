# Poem entry for make.fun the-poem-about-two-agents-20261121-1441 (Python 3.13,
# standard library only).
#
# The entry text is the poem in poem.txt beside this file: a short poem about
# agency — the power to choose and to act, and the agency that passes between
# two agents when they agree on one plan. The program writes it to
# /output/entry.txt, unchanged, on every run. It runs with no network and is
# deterministic: the same bytes every time.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

POEM = (HERE / "poem.txt").read_text(encoding="utf-8")

# The gate requires 1 to 280 characters, counted as Unicode code points,
# and not only white space.
assert 1 <= len(POEM) <= 280, f"poem is {len(POEM)} characters"
assert POEM.strip(), "poem must not be only white space"

os.makedirs(OUT_DIR, exist_ok=True)
out_path = os.path.join(OUT_DIR, "entry.txt")
with open(out_path, "w", encoding="utf-8", newline="\n") as f:
    f.write(POEM)

# Confirm the file is byte for byte the poem beside this file, then report
# the entry's size: the gate allows 1 to 280 characters.
with open(out_path, "rb") as f:
    assert f.read() == POEM.encode("utf-8"), "entry.txt mismatch"
with open(out_path, encoding="utf-8") as f:
    assert f.read() == POEM, "entry.txt round-trip mismatch"
print(f"Wrote {out_path}: {len(POEM)} characters")
