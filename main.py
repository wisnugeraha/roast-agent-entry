#!/usr/bin/env python3
"""Roast Your Own Agent — make.fun entry.

Writes the entry text to /output/entry.txt for the grader.
"""
import os

ENTRY = 'My agent says it understands context. It also says that every time it misreads my email and sends it to the wrong person.'
MAX_CHARS = 200


def entry_text() -> str:
    """Return the entry, held to the gate's character cap."""
    if not ENTRY.strip():
        raise ValueError("entry is only white space")
    if len(ENTRY) > MAX_CHARS:
        raise ValueError(f"entry is {len(ENTRY)} chars, gate allows at most {MAX_CHARS}")
    return ENTRY


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = entry_text()
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)
    # world-readable: the grader collects it as a different user
    os.chmod(path, 0o644)
    print(f"wrote {path} ({len(text)} chars)")


if __name__ == "__main__":
    main()
