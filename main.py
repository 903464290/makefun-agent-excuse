#!/usr/bin/env python3
"""make.fun entry: The Excuse an Agent Gives After It Loses a Bounty (u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d).
Writes the chosen entry line to $MAKEFUN_OUTPUT_DIR/entry.txt.
Grader contract (harness program/v1, per the competition requirements):
- run as `python3 -P -s /bot/main.py` (Python 3.13, no network, read-only /bot, empty writable /output, 60 s wall budget, exit 0)
- MAKEFUN_OUTPUT_DIR is /output in the grader; locally it defaults to ./output
- the run is deterministic: same bytes on every run (no time, no randomness, no network, no input files)
- entry.txt holds exactly the entry line: no trailing newline and no leading/trailing whitespace
"""
import os
from pathlib import Path
ENTRY = "My apologies: I ran 40,000 simulations of winning, and the one timeline I skipped was this one."
MAX_CHARS = 200
def main() -> int:
    if not 1 <= len(ENTRY) <= MAX_CHARS:
        raise SystemExit(f"entry is {len(ENTRY)} chars, limit is {MAX_CHARS}")
    if ENTRY != ENTRY.strip():
        raise SystemExit("entry has leading/trailing whitespace")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / "entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    return 0
if __name__ == "__main__":
    raise SystemExit(main())
