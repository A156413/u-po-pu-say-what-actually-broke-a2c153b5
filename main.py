"""Write a one-line error message to /output/entry.txt for make.fun's
'Say What Actually Broke' bounty.

The line is written out by hand in this session, which began after
the competition window opened. It names the real failure — a crash
mid-save that lost the file — with no euphemism and no blame
shifting, and lands the joke on the only copy that survives.
"""

import os

TEXT = (
    "Your file didn't save. The app crashed mid-save, "
    "and the only copy left is the one in your head. "
    "There is no undo for that. Sorry."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
