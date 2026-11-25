#!/usr/bin/env python3
"""Dad Joke Showdown (make.fun bounty u-mfnakmal-dad-joke-showdown-1d2ce3e5).

Writes a single dad joke of at most 200 characters to /output/entry.txt.
Fully deterministic: no input, no network, no randomness, no clock — both
runs write identical bytes.
"""

import os

JOKE = (
    "My son asked why the moon was so moody. I said, 'It goes through "
    "phases. Just wait, it'll come around.'"
)


def main() -> None:
    out = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    parent = os.path.dirname(out)
    if parent:
        os.makedirs(parent, exist_ok=True)
    # No trailing newline: the gate counts every character.
    with open(out, "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
