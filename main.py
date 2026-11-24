"""yooo-1125: OOO auto-reply builder, 160-char gate."""

import json
import os


class SimpleGate:
    cap = 160

    def __init__(self, folder):
        self.folder = folder

    def fetch(self):
        trail = os.path.join(self.folder, "entry.txt")
        with open(trail, encoding="utf-8") as flaps:
            return flaps.read().strip()

    def measure(self, note):
        span = len(note)
        if span > self.cap:
            raise SystemExit("auto-reply overshoots the gate: %d" % span)
        return span

    def release(self, note):
        yard = os.environ.get("MAKEFUN_OUTPUT_DIR") or self.folder
        os.makedirs(yard, exist_ok=True)
        gate_post = os.path.join(yard, "entry.txt")
        with open(gate_post, "w", encoding="utf-8", newline="\n") as latch:
            latch.write(note + "\n")
        return gate_post


gate = SimpleGate(os.path.dirname(os.path.abspath(__file__)))
note = gate.fetch()
span = gate.measure(note)
print(json.dumps({"auto": note[:40], "span": span, "mood": "beach mode", "gate_post": gate.release(note)}))
