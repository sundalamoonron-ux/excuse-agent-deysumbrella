#!/usr/bin/env python3
"""The Excuse My Agent Gave Me -- make.fun entry.

Writes one line (<= 200 characters) to <output>/entry.txt: the excuse
an AI agent hands its human for a missed deadline.
"""

import os
import sys

# The line: the agent set a reminder, then hallucinated a second deadline
# next week and worked to that one instead. Machine condition (hallucinated
# calendar), straight-faced, punch in the last few words.
LINE = "I set a reminder for the deadline, then hallucinated a second deadline next week and worked to that one instead."

def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    text = LINE
    # Gate self-check: 1-200 UTF-8 chars, not only whitespace, one line,
    # no leading/trailing whitespace.
    assert 1 <= len(text) <= 200, f"line length {len(text)} outside 1-200"
    assert text.strip(), "line is only whitespace"
    assert text == text.strip(), "line has leading/trailing whitespace"
    assert "\n" not in text, "line must be a single line"
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # Verify-after-write: read back and confirm exact bytes.
    with open(path, "rb") as f:
        data = f.read()
    assert data == text.encode("utf-8"), "written bytes differ from line"
    return 0

if __name__ == "__main__":
    sys.exit(main())
