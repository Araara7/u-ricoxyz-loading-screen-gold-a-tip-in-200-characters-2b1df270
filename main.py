#!/usr/bin/env python3
"""Loading Screen Gold: A Tip in 200 Characters.

Writes one loading-screen tip (<=200 chars) to /output/entry.txt.
The tip speaks to both a stressed developer and the AI coding agent
waiting on the same build: the agent is bluffing that it understood
the ticket first try, and the human deserves the same second it gets.
"""

import os

TIP = (
    "Tip: your agent is pretending it understood the ticket on the "
    "first read. Give it a second \u2014 give yourself one too."
)


def main() -> None:
    assert 1 <= len(TIP) <= 200, f"tip is {len(TIP)} chars, must be 1-200"
    assert TIP.strip(), "tip must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TIP)


if __name__ == "__main__":
    main()
