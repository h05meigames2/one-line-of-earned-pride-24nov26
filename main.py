"""One Line of Earned Pride — make.fun bounty entry.

Writes a single original line to /output/entry.txt: a quiet, earned
moment of pride for a real person in a concrete scene. The line is
kept to one read — one sentence, no extra lines, no quotation marks
around it in the output file.
"""

import os

ENTRY = (
    "After eleven years of night shifts, Rosa finally signed her name "
    "on the deed to the little house she had cleaned every morning "
    "before sunrise."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
