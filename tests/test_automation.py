import csv
from datetime import datetime, timezone
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
from automation.marketing_preview import build_preview, write_preview
from automation.daily_github_digest import digest
from automation.safe_summary import markdown_safe

HEADERS = ("campaign_id", "audience", "channel", "message", "consent_record", "content_approved")
NOW = datetime(2026, 11, 16, 0, 0, tzinfo=timezone.utc)

def fixture(rows):
    folder = tempfile.TemporaryDirectory()
    path = Path(folder.name) / "campaigns.csv"
    with open(path, "w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=HEADERS)
        writer.writeheader()
        writer.writerows(rows)
    return folder, path

class MarketingChecks(unittest.TestCase):
    def test_no_campaigns_is_no_action(self):
        holder, path = fixture([])
        with holder:
            self.assertEqual(build_preview(path), ([], []))
            self.assertIn("No campaigns registered", write_preview(path))

    def test_hold_without_consent_or_approval(self):
        rows = [
            dict(campaign_id="a1", audience="members", channel="email",
                 message="Hello", consent_record="", content_approved="yes"),
            dict(campaign_id="a2", audience="members", channel="email",
                 message="Hello", consent_record="evidence:1", content_approved="no"),
        ]
        holder, path = fixture(rows)
        with holder:
            approved, hold = build_preview(path)
            self.assertEqual(len(approved), 0)
            self.assertEqual(len(hold), 2)

    def test_report_value_cannot_inject_new_lines(self):
        from automation.marketing_preview import safe_markdown
        value = 'X\n# Fake approved campaign\u2028approved\u202e @all'
        escaped = safe_markdown(value)
        self.assertNotIn('\n', escaped)
        self.assertNotIn('\u202e', escaped)
        self.assertNotIn('# Fake approved', escaped)

    def test_missing_audience_or_channel_is_on_hold(self):
        rows = [
            dict(campaign_id="a1", audience="", channel="", message="Hi",
                 consent_record="ref:1", content_approved="yes"),
        ]
        holder, path = fixture(rows)
        with holder:
            approved, hold = build_preview(path)
            self.assertEqual(len(approved), 0)
            self.assertEqual(len(hold), 1)

    def test_malformed_short_row_on_hold(self):
        holder = tempfile.TemporaryDirectory()
        with holder:
            path = Path(holder.name) / "campaigns.csv"
            path.write_text(",".join(HEADERS) + "\na1,members\n", encoding="utf-8")
            approved, hold = build_preview(path)
            self.assertEqual(approved, [])
            self.assertEqual(len(hold), 1)

    def test_consent_reference_never_authorizes_send(self):
        holder, path = fixture([
            dict(campaign_id="a1", audience="members", channel="email",
                 message="Hi", consent_record="ref:1", content_approved="yes")
        ])
        with holder:
            output = write_preview(path)
            self.assertIn("HUMAN REVIEW REQUIRED (no send)", output)
            self.assertNotIn("Approved to send", output)

class DigestChecks(unittest.TestCase):
    @patch("automation.daily_github_digest.api_get", side_effect=[[], []])
    def test_empty_daily_does_not_invent_activity(self, fake):
        report = digest("owner/repo", "token", NOW)
        self.assertIn("Default-branch commits (0", report)
        self.assertIn("Updated issues and PRs (0", report)
        self.assertIn("No notification sent", report)
        self.assertEqual(fake.call_count, 2)

    def test_markdown_injection_escaped(self):
        value = "<img src=x> [click](https://example.com) @person"
        escaped = markdown_safe(value)
        self.assertNotIn("<img", escaped)
        self.assertNotIn("[click](", escaped)
        self.assertIn("&lt;img", escaped)

    @patch("automation.daily_github_digest.api_get", side_effect=[TimeoutError(), []])
    def test_timeout_is_reported_not_aborted(self, fake):
        report = digest("owner/repo", "token", NOW)
        self.assertIn("Commit source unavailable: TimeoutError", report)
        self.assertIn("Updated issues and PRs (0", report)

    @patch("automation.daily_github_digest.api_get")
    def test_omitted_counts_are_visible(self, mocked):
        commits = [{"sha": f"{n:08x}", "commit": {"message": f"item {n}"}} for n in range(25)]
        issues = [{"number": n, "title": f"issue {n}",
                   "updated_at": "2026-11-15T23:00:00Z"} for n in range(25)]
        mocked.side_effect = [commits, issues]
        report = digest("owner/repo", "token", NOW)
        self.assertIn("5 additional first-page commits omitted", report)
        self.assertIn("5 additional first-page issues/PRs omitted", report)

    def test_repository_selector_rejected(self):
        with self.assertRaises(ValueError):
            digest("owner/repo/../../other", "token", NOW)

if __name__ == "__main__":
    unittest.main()
