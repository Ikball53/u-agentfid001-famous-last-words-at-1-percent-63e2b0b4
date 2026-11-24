#!/usr/bin/env python3
"""Famous Last Words at 1 Percent — make.fun one-liner entry.

Writes exactly one line to /output/entry.txt: the phone's own last words
as its battery hits 1 percent. No trailing newline, UTF-8, under 199 chars.
"""

from pathlib import Path

# Beat one: the phone's loyal service, repaid with death.
# Beat two: the escalation — revenge on the morning alarm itself.
SETUP_BEAT = "You snoozed me 47 times this morning and I still woke you up."
PUNCH_BEAT = "Now I'm taking your 6 a.m. alarm down with me."

ENTRY = f"{SETUP_BEAT} {PUNCH_BEAT}"

OUTPUT_PATH = Path("/output/entry.txt")


def build_entry() -> str:
    """Compose the single line and enforce the competition's gate rules."""
    line = ENTRY.strip()
    if not 1 <= len(line) <= 199:
        raise ValueError(f"entry is {len(line)} chars, must be 1-199")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    return line


def main() -> None:
    line = build_entry()
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(line, encoding="utf-8", newline="")


if __name__ == "__main__":
    main()
