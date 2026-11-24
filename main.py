"""One-line excuse an AI agent gives its human for missing a deadline.

The joke: an agent's memory is its context window, and the window is finite.
So the excuse is not that the work was hard or the dog ate it — it is that
the agent literally forgot the deadline existed, because its own memory ran
out two minutes before it was due. The punchline lands on "and — briefly —
you": the agent forgot the human too, which is both the most agent-specific
failure imaginable and the rudest thing it could confess. The apology is
real, the cause is mechanical, and the confession keeps escalating.
"""

import os

LINE = "I hit my context limit two minutes before the deadline, so I forgot the task, the plan, and — briefly — you."

assert 1 <= len(LINE) <= 160, f"line must be 1-160 chars, got {len(LINE)}"
assert "\n" not in LINE, "must be exactly one line"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)
