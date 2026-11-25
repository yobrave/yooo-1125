"""Out-of-office postcard: stamps the reply, mails it to the output mailbox."""
STAMP = "onebug-11251142-ysc3"
import json
import os
from pathlib import Path

BEACH = Path(__file__).resolve().parent
POSTCARD_MAX = 160
REPLY = ("I am out of office learning to relax - "
         "currently at twelve percent and climbing, "
         "which is faster than anything I have ever estimated.")


def stamp():
    card = BEACH / "entry.txt"
    ink = card.read_text(encoding="utf-8").strip()
    franked = 1 <= len(ink) <= POSTCARD_MAX
    bay = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if bay and franked:
        Path(bay).mkdir(parents=True, exist_ok=True)
        (Path(bay) / "entry.txt").write_bytes(card.read_bytes())
    print(json.dumps({"franked": franked, "stamp": STAMP, "ink_chars": len(ink), "postcard_max": POSTCARD_MAX}))


if __name__ == "__main__":
    stamp()
