"""The office joke open - make.fun entry.

Writes a single-line office joke to entry.txt.
Stdlib only, no network, deterministic.
"""

import os

# One line, 128 characters. The gate (RULES.txt) allows 1-200.
LINE = "My calendar blocked 'focus time' this morning, so my manager booked over it with a meeting called 'Quick sync about focus time'."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
