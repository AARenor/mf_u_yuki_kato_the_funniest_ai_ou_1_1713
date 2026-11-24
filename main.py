#!/usr/bin/env python3
"""Write the make.fun bounty entry text to entry.txt.

Bounty: u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d

The entry is a single short out-of-office auto-reply. This program writes it
to the folder named by MAKEFUN_OUTPUT_DIR when that is set, and to /output
otherwise, creating the folder if needed. Standard library only, no network.
"""

import os
import sys

TEXT = (
    "On leave until the 14th. A wasp has built a nest in the mailbox and I "
    "respect her. All my mail is being held at the post office, and by the wasp."
)


def main() -> int:
    assert 1 <= len(TEXT) <= 280, "entry text must be 1..280 characters"

    out_dir = (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )
    os.makedirs(out_dir, exist_ok=True)

    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as fh:
        fh.write(TEXT)

    print(len(TEXT), file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
