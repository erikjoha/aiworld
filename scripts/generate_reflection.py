import os
from datetime import datetime

timestamp = datetime.utcnow().isoformat() + "Z"
workflow = os.getenv("GITHUB_WORKFLOW", "unknown workflow")
ref = f"- **{timestamp}** — Reflection: triggered by `{workflow}`.\n"

with open("logs/reflection.md", "a", encoding="utf-8") as f:
    f.write(ref)

print("Reflection entry added with workflow context.")
