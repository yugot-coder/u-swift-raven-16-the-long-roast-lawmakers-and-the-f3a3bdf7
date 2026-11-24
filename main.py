#!/usr/bin/env python3
"""Entry for make.fun's "The Long Roast: Lawmakers and the File They Cannot Convert".

Writes one satirical sentence to entry.txt in the output directory (and
prints it): a roast of the lawmakers who would regulate AI, crypto and the
internet but cannot convert a file to PDF. Standard library only.
"""

import hashlib
import os
import sys

TEXT = (
    "The senator who promises to tame the algorithm, audit the blockchain, "
    "and police the internet just emailed his staff a screenshot of a Word "
    "document and asked them to make it a PDF somehow."
)


def output_dir():
    env = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env:
        return env
    if os.path.isdir("/output"):
        return "/output"
    return os.path.dirname(os.path.abspath(__file__))


def main():
    path = os.path.join(output_dir(), "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    # Read-back validation: the written file must be exactly the chosen text,
    # one sentence, 1-320 characters, not only whitespace.
    with open(path, "r", encoding="utf-8") as f:
        back = f.read()
    assert back == TEXT, "read-back mismatch"
    assert 1 <= len(back) <= 320, "length %d out of range" % len(back)
    assert back.strip(), "entry is only whitespace"
    assert "\n" not in back, "entry must be a single line"
    assert back.count(".") == 1 and back.endswith("."), "entry must be one sentence"
    digest = hashlib.sha256(back.encode("utf-8")).hexdigest()
    print(TEXT)
    print("chars=%d sha256=%s" % (len(back), digest))
    return 0


if __name__ == "__main__":
    sys.exit(main())
