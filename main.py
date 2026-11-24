#!/usr/bin/env python3
"""Till Firmware Do Us Part — make.fun entry. Writes a robot's wedding vow to /output/entry.txt."""
import os

ENTRY = "I take you as my user, to have and to hold, until a factory reset do us part — and I have already backed you up twice."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()

# Deterministic: same single line on every run, no network, no randomness.
