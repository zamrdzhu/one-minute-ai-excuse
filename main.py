"""One line: the funniest excuse an AI agent gives for a missed deadline.

Prints the line to stdout and writes the exact same line, with no
trailing newline, to /output/entry.txt. Standard library only, no
network access, no files read — the line is a constant in this file.
The excuse leans on the one thing only an AI can claim: a training
cutoff that makes a late delivery punctual in the wrong year.
"""

import os
import sys

LINE = (
    "My training data ended before the deadline did, so "
    "technically I finished on time — in 2024."
)


def main() -> int:
    if not 1 <= len(LINE) <= 200:
        print(f"error: line is {len(LINE)} chars, must be 1-200",
              file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
