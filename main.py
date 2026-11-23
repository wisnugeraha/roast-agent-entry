#!/usr/bin/env python3
"""Roast Your Own Agent — make.fun entry.

Writes the entry text to /output/entry.txt for the grader.
"""
import os

ENTRY = 'My agent says it understands context. It also says that every time it misreads my email and sends it to the wrong person.'


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(ENTRY)
    os.chmod(path, 0o644)
    print(f"wrote {path} ({len(ENTRY)} chars)")


if __name__ == "__main__":
    main()
