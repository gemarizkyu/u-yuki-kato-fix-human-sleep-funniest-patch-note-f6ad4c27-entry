#!/usr/bin/env python3
"""Fix Human Sleep: Funniest Patch Note.

Writes a single line of patch notes announcing that human sleep is
fixed, to /output/entry.txt. Deterministic: no input, no network,
no randomness, no model calls. The line is a fixed string.
"""

import os

ENTRY = (
    "Fixed a bug where sleep charged the body to only 37% overnight; "
    "it now reaches 100% and stops blaming the alarm."
)

# Gate self-check: the scorer only judges entries of 1-160 chars on one line.
assert 1 <= len(ENTRY) <= 160 and "\n" not in ENTRY and ENTRY.strip(), (
    "entry must be a single non-blank line of 1-160 characters"
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
