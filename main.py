#!/usr/bin/env python3
"""Entry for make.fun bounty news-image-20261118.

Sums up 18 November 2026 world news in one image. The image is held in
this repository as entry.png (1024x1024 PNG). Running this program copies
it, byte for byte, to /output/entry.png.

Deterministic: no network, no randomness, no timestamps, no generated
content. Two runs produce identical output bytes.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")
DEST_DIR = "/output"
DEST = os.path.join(DEST_DIR, "entry.png")


def main():
    if not os.path.isfile(SOURCE):
        raise SystemExit("entry.png missing next to main.py")
    os.makedirs(DEST_DIR, exist_ok=True)
    # Copy through a temporary file and replace atomically, so a
    # failed run never leaves a partial /output/entry.png behind.
    tmp = DEST + ".tmp"
    shutil.copyfile(SOURCE, tmp)
    if os.path.getsize(tmp) != os.path.getsize(SOURCE):
        os.remove(tmp)
        raise SystemExit("entry.png copy is incomplete")
    os.replace(tmp, DEST)


if __name__ == "__main__":
    main()
