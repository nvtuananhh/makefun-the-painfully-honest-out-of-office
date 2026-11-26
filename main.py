"""The Painfully Honest Out-of-Office.

Entry (one sentence, painfully honest but still polite):
I'm away until Monday, and your email is currently 214th in my inbox, so I will answer it with exactly the enthusiasm it deserves.

The program writes exactly that line to entry.txt in the output
directory given by MAKEFUN_OUTPUT_DIR (default "."). No network,
no randomness, deterministic: the same bytes every run.
"""

import os
import sys

ENTRY = (
    "I'm away until Monday, and your email is currently "
    "214th in my inbox, so I will answer it with exactly "
    "the enthusiasm it deserves."
)


def main() -> int:
    # Gate: 1-200 chars, single line, not only whitespace.
    # The entry is exactly 130 characters.
    assert len(ENTRY) == 130, f"entry length {len(ENTRY)} != 130"
    assert 1 <= len(ENTRY) <= 200, f"entry length {len(ENTRY)} out of range"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be a single line"
    assert ENTRY.strip(), "entry must not be only whitespace"

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", ".")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
