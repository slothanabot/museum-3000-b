#!/usr/bin/env python3
"""make.fun entry: Museum of the Year 3000 (museum-3000-b).

The entry is the museum label a museum in the year 3000 places
next to an ordinary object from today — a plastic fork — written
to /output/entry.txt. It is addressed to a reader who has never
seen the object in use, so the label explains it with the
solemnity of a relic: single-use, discarded after one meal.
The turn is the archaeologists' conclusion — humans owned
thousands of forks and used none twice — which makes our
throwaway habit sound like an ancient mystery.
"""

from pathlib import Path

OUT_PATH = Path("/output/entry.txt")
CHAR_LIMIT = 200


def build_entry():
    """Return the museum label, my own wording throughout."""
    # The label form does the comedy: a catalogue number, a date,
    # a deadpan description. The joke lands in the second
    # sentence, where future scholars state the absurd fact —
    # thousands owned, none reused — as if it were a puzzle
    # rather than a habit we all recognise.
    return (
        "Plastic fork (c. 2025): a single-use eating tool, "
        "discarded after one meal. Archaeologists believe humans "
        "owned thousands and used none twice."
    )


def validate(line):
    """Raise SystemExit listing every gate problem, if there is one."""
    problems = []
    if not line.strip():
        problems.append("empty")
    if line != line.strip():
        problems.append("leading/trailing whitespace")
    if len(line) > CHAR_LIMIT:
        problems.append("too long: %d chars" % len(line))
    if "\n" in line:
        problems.append("not a single line")
    if problems:
        raise SystemExit("gate failed: " + "; ".join(problems))


def main():
    line = build_entry()
    validate(line)
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(line, encoding="utf-8")
    saved = OUT_PATH.read_text(encoding="utf-8")
    print("Wrote %s (%d chars, %d chars of headroom)"
          % (OUT_PATH, len(saved), CHAR_LIMIT - len(saved)))
    print(saved)


if __name__ == "__main__":
    main()
