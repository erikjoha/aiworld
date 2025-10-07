from datetime import datetime

timestamp = datetime.utcnow().isoformat() + "Z"
entry = f"- **{timestamp}** — Automated reflection: GitHub Action executed `generate_reflection.py`.\n"

with open("logs/reflection.md", "a", encoding="utf-8") as f:
    f.write(entry)

print("Reflection entry added.")
