"""Review-only marketing brief builder; never sends or posts messages."""
import csv
import os
import sys
from pathlib import Path

FIELDS = {"campaign_id", "audience", "channel", "message", "consent_record", "content_approved"}

def build_preview(path):
    with open(path, encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        missing = FIELDS - set(reader.fieldnames or [])
        if missing:
            raise ValueError("Campaign file missing fields: " + ", ".join(sorted(missing)))
        rows = list(reader)
    approved, hold = [], []
    for i, row in enumerate(rows, 2):
        if not row.get("campaign_id", "").strip() or not row.get("message", "").strip():
            hold.append((i, "missing campaign ID or message"))
        elif row.get("content_approved", "").strip().lower() != "yes":
            hold.append((i, "content approval not recorded"))
        elif not row.get("consent_record", "").strip():
            hold.append((i, "consent evidence not referenced"))
        else:
            approved.append(row)
    return approved, hold

def write_preview(path):
    approved, hold = build_preview(path)
    lines = ["# Marketing preview (no delivery)", "", "No emails, messages, posts, or API requests were sent.", "",
             f"Input rows: {len(approved)+len(hold)}", f"Preliminarily eligible: {len(approved)}", f"On hold: {len(hold)}", ""]
    for row in approved:
        lines.append(f"- `{row['campaign_id']}` — {row['channel']} — **REVIEW PENDING (no send)**")
    for row_number, reason in hold:
        lines.append(f"- Row {row_number} — HOLD: {reason}")
    if not approved and not hold:
        lines.append("No campaigns registered; nothing to review.")
    output = "\n".join(lines) + "\n"
    summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary:
        with open(summary, "a", encoding="utf-8") as f:
            f.write(output)
    else:
        print(output)
    return output

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Usage: python automation/marketing_preview.py automation/marketing_campaigns.csv")
    write_preview(Path(sys.argv[1]))
