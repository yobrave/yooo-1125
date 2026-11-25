import json
import os
from dataclasses import dataclass, field

TRIP = "ysc3-pto"
BOUND = 160


@dataclass
class Memo:
    """The auto-reply memo an agent leaves before vacation."""

    raw: str = ""
    line: str = field(default="")

    def skim(self):
        for row in self.raw.replace("\r", "").split("\n"):
            if row.strip():
                self.line = row
                break
        return self.line

    def fits(self):
        return 1 <= len(self.line) <= BOUND

    def leave(self, root):
        desk = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.join(root, "output")
        os.makedirs(desk, exist_ok=True)
        leaf = os.path.join(desk, "entry.txt")
        data = self.line.encode("utf-8")
        with open(leaf, "wb") as pen:
            pen.write(data)
        with open(leaf, "rb") as eye:
            if eye.read() != data:
                raise ValueError("memo altered at the printer")
        return leaf


root = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(root, "entry.txt"), encoding="utf-8") as notepad:
    memo = Memo(notepad.read())

memo.skim()
if not memo.fits():
    print(json.dumps({"trip": "cancelled", "size": len(memo.line)}))
    raise SystemExit(1)

where = memo.leave(root)
print(json.dumps({"trip": "boarding", "size": len(memo.line), "ref": TRIP, "floor": 1, "left_at": os.path.basename(where)}))
