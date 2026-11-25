"""yoo6: vacation responder. Little lambdas pass the note along a chain."""
import json
import os
import sys
from pathlib import Path

NAP = 160

tidy = lambda raw: raw.strip()
spoken = lambda line: line != "" and not line.isspace()
inside = lambda line: len(line) <= NAP


def post(line: str):
    box = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "out")
    box.mkdir(parents=True, exist_ok=True)
    (box / "entry.txt").write_bytes(line.encode("utf-8"))
    return str(box)


def main():
    raw = Path(__file__).resolve().parent.joinpath("entry.txt").read_text(encoding="utf-8")
    line = tidy(raw)
    aloud = spoken(line)
    fits = inside(line)
    mailed = post(line) if (aloud and fits) else None
    print("VERDICT", json.dumps({"note": "yoo6-vacay-r11251422", "aloud": aloud, "fits": fits, "mailed": mailed, "n": len(line)}))
    return 0 if mailed else 1


if __name__ == "__main__":
    sys.exit(main())
