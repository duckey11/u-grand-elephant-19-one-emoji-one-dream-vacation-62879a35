#!/usr/bin/env python3
"""Write exactly one emoji, a dream vacation, to /output/entry.txt.

makefun anchor 431817751445c210125fcb5b4d0a0728d0b4fc33 round 34239792

The emoji is U+1F3DD DESERT ISLAND, written with no variation selector
and no trailing newline: 1 character, 4 bytes of UTF-8.
"""

import os

EMOJI = "\U0001F3DD"  # Desert island: a faraway tropical escape.

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(EMOJI)


if __name__ == "__main__":
    main()
