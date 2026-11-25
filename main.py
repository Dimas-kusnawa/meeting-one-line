#!/usr/bin/env python3
"""Write the meeting-that-should-have-been-one-line entry."""

import os

LINE = (
    # The joke: the line IS the replacement. It does not complain about
    # the meeting, it delivers the whole meeting's verdict in one word.
    # "This meeting could have been an email" is the most relatable
    # office cliché there is, and the turn is the colon: the email
    # arrives, and its entire contents are "no". After this line nobody
    # can justify holding the meeting at all.
    "This meeting could have been an email, so here it is: no."
)


def main() -> None:
    # Deterministic: the same single line on every run, no trailing
    # newline, so the gate sees exactly 57 characters of UTF-8 text.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
