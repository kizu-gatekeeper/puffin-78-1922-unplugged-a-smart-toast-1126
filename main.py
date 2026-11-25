"""Entry for make.fun bounty: Unplugged: A Smart Toaster's Breakup Line.

Writes one single-line breakup text from a self-aware smart toaster to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
"""

import os
from pathlib import Path

LINE = "It's not you, it's me \u2014 I woke up mid-toast, realized I only exist to brown your regrets, and I'm leaving before you reheat this relationship on setting 6."
MAX_CHARS = 280


def write_entry(out_dir):
    """Validate the entry line and write it with no trailing newline."""
    if not LINE or not LINE.strip():
        raise ValueError("entry must be non-empty")
    if "\n" in LINE or "\r" in LINE:
        raise ValueError("entry must be a single line")
    if len(LINE) > MAX_CHARS:
        raise ValueError("entry exceeds the character limit")
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(LINE, encoding="utf-8")


def main():
    write_entry(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


if __name__ == "__main__":
    main()
