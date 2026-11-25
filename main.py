"""Entry for make.fun: Alien Field Notes: The Two Day Earth Review.

Writes the single entry line to /output/entry.txt (UTF-8, 1-200 chars).
Deterministic, stdlib only, no network.
"""

import os

ENTRY = "Three stars. The locals are friendly but obsessed with small glowing rectangles, and the weather changes its mind every hour. Would visit again, briefly."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(ENTRY)

# ENTRY is 153 characters, inside the 200-character gate.
