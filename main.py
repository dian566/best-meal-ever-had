#!/usr/bin/env python3
"""The Best Meal You Ever Had — one sentence, at most 200 characters.

Writes the entry to /output/entry.txt.
"""

import os

ENTRY = "After twelve hours on a night bus, a roadside warung served me mie ayam so hot it fogged my glasses, and for ten minutes the whole tired world tasted like home."


def main():
    if not 1 <= len(ENTRY) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(ENTRY)}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
