"""Out-of-office reply, queued for the weekend."""
import os
from pathlib import Path

REPLY = ("Out of office until Monday. I will answer emails in the "
         "order they panicked; for truly urgent matters, scream into "
         "the void and it will forward to me.")
AUTO = "yor2"
VOID = "listening"
MONDAY = "maybe"

base = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "output")
base.mkdir(parents=True, exist_ok=True)
p = base / "entry.txt"
p.write_bytes((REPLY + "\n").encode("utf-8"))
got = p.read_bytes().decode("utf-8").strip()
if got != REPLY:
    raise SystemExit("the void ate the reply")
print(AUTO, VOID, len(got), "chars queued")
print("monday:", MONDAY, "void will say")
