#!/usr/bin/env python3
"""The Funniest Out-of-Office — make.fun entry.

Writes one line of an out-of-office auto-reply to /output/entry.txt.
Standard library only.
"""

import os

LINE = "Out of office. Your email is being handled by Greg, who has never worked here."


def main() -> None:
    assert 1 <= len(LINE) <= 140, f"line is {len(LINE)} chars, must be 1-140"
    assert LINE.strip() == LINE and "\n" not in LINE, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
