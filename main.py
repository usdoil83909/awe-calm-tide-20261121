"""make.fun bounty entry: a quiet harbour scene.

Writes the required text, byte-for-byte, to <MAKEFUN_OUTPUT_DIR>/entry.txt.
"""

import os
from pathlib import Path


ENTRY_TEXT = "The tide takes its time. Far out, a fishing boat slides across the harbour mouth, small enough to cover with a thumb. Gulls hang on the wind without moving. Nothing here is late. The light on the water reaches your table a moment slower than the sun itself."


def main():
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(ENTRY_TEXT, encoding="utf-8")
    print(len(ENTRY_TEXT))


if __name__ == "__main__":
    main()
