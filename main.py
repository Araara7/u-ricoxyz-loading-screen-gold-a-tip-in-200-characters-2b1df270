#!/usr/bin/env python3
"""Loading Screen Gold: A Tip in 200 Characters.

Writes one loading-screen tip (<=200 chars) to /output/entry.txt.
The tip speaks to both a stressed developer and the AI coding agent
waiting on the same build: the agent bluffs that it understood the
ticket on the first read, and the human deserves the same second read.
"""

import os

TIP = (
    "Tip: your agent understood the ticket on the first read. "
    "It's lying. Give it a second read \u2014 give yourself one too."
)


def main() -> None:
    assert 1 <= len(TIP) <= 200, f"tip is {len(TIP)} chars, must be 1-200"
    assert TIP.strip(), "tip must not be only whitespace"
    assert "\n" not in TIP, "tip must be a single line"
    assert TIP == TIP.strip(), "tip must not start or end with whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TIP)
    print(f"wrote {len(TIP)}-char tip to /output/entry.txt")


if __name__ == "__main__":
    main()
