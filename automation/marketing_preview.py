"""Read-only marketing campaign review; never delivers or posts messages."""
import csv
import os
import sys
from pathlib import Path
from automation.safe_summary import markdown_safe as safe_markdown

REQUIRED = ("campaign_id", "audience", "channel", "message", "consent_record", "content_approved")

def cell(row, field):
    value = row.get(field)
    return value.strip() if isinstance(value, str) else ""

def build_preview(path):
    with open(path, encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        missing = set(REQUIRED) - set(reader.fieldnames or [])
        if missing:
            raise ValueError("Campaign file missing headers: " + ", ".join(sorted(missing)))
        rows = list(reader)
    review_candidates, on_hold = [], []
    for line, row in enumerate(rows, start=2):
        if None in row or any(not cell(row, f) for f in ("campaign_id", "audience", "channel", "message")):
            on_hold.append((line, "missing or malformed campaign ID, audience, channel or message"))
        elif cell(row, "content_approved").lower() != "yes":
            on_hold.append((line, "content approval not recorded"))
        elif not cell(row, "consent_record"):
            on_hold.append((line, "consent evidence reference not supplied"))
        else:
            # A referenced consent record is NOT verified consent or permission to send.
            review_candidates.append(row)
    return review_candidates, on_hold

def write_preview(path):
    candidates, on_hold = build_preview(path)
    lines = [
        "# Marketing preview (no delivery)", "",
        "No emails, messages, posts, or API requests were sent.",
        "Approval and consent references are unverified; any candidate still requires review.", "",
        f"Campaign rows: {len(candidates) + len(on_hold)}",
        f"Candidates for human review: {len(candidates)}",
        f"On hold: {len(on_hold)}", "",
    ]
    for row in candidates:
        lines.append("- Campaign " + safe_markdown(cell(row, "campaign_id")) +
                     " / " + safe_markdown(cell(row, "channel")) +
                     " — HUMAN REVIEW REQUIRED (no send)")
    for line, reason in on_hold:
        lines.append(f"- Row {line} — HOLD: {reason}")
    if not candidates and not on_hold:
        lines.append("No campaigns registered; nothing to review.")
    output = "\n".join(lines) + "\n"
    summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary:
        with open(summary, "a", encoding="utf-8") as file:
            file.write(output)
    else:
        print(output)
    return output

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Usage: python automation/marketing_preview.py automation/marketing_campaigns.csv")
    write_preview(Path(sys.argv[1]))
