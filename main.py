#!/usr/bin/env python3
"""THE OPEN LEDGER — entrypoint (Final 2, News Image 20261125).

The page under inspection is entry.png, filed beside this
script. Delivery works the way a careful clerk files a record:
copy it to a temporary name in /output first, then rename it
into place, so the destination never holds a half-written
page. Standard library only.
"""
import os
import shutil

ROOT = os.path.dirname(os.path.abspath(__file__))
PAGE = os.path.join(ROOT, "entry.png")
OUT_DIR = "/output"
TMP_NAME = ".entry-in-transit.png"


def file_the_page() -> str:
    os.makedirs(OUT_DIR, exist_ok=True)
    transit = os.path.join(OUT_DIR, TMP_NAME)
    final = os.path.join(OUT_DIR, "entry.png")
    shutil.copyfile(PAGE, transit)
    os.replace(transit, final)
    return final


if __name__ == "__main__":
    filed = file_the_page()
    print("filed", filed, os.path.getsize(filed), "bytes")
