from datetime import datetime
with open("README.md", "a", encoding="utf-8") as f:
    f.write(f"\n\n_Updated: {datetime.utcnow().isoformat()}Z_")
print("README updated.")
