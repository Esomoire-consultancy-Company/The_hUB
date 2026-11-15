import csv
from pathlib import Path
import tempfile
import unittest
from datetime import datetime, timezone
from unittest.mock import patch
from automation.marketing_preview import build_preview
from automation.daily_github_digest import digest

class MarketingChecks(unittest.TestCase):
    def test_no_campaigns_is_no_action(self):
        with tempfile.TemporaryDirectory() as folder:
            file = Path(folder) / "campaigns.csv"
            file.write_text("campaign_id,audience,channel,message,consent_record,content_approved\n", encoding="utf-8")
            self.assertEqual(build_preview(file), ([], []))
    def test_hold_without_consent_or_approval(self):
        with tempfile.TemporaryDirectory() as folder:
            file = Path(folder) / "campaigns.csv"
            with open(file, "w", encoding="utf-8", newline="") as out:
                w = csv.DictWriter(out, fieldnames=["campaign_id", "audience", "channel", "message", "consent_record", "content_approved"])
                w.writeheader()
                w.writerow({"campaign_id":"a1", "audience":"members", "channel":"email", "message":"Hello", "consent_record":"", "content_approved":"yes"})
                w.writerow({"campaign_id":"a2", "audience":"members", "channel":"email", "message":"Hello", "consent_record":"evidence:1", "content_approved":"no"})
            approved, hold = build_preview(file)
            self.assertEqual(len(approved), 0)
            self.assertEqual(len(hold), 2)

class DigestChecks(unittest.TestCase):
    @patch("automation.daily_github_digest.api_get", side_effect=[[], []])
    def test_empty_daily_does_not_invent_activity(self, fake):
        report = digest("owner/repo", "token", datetime(2026, 11, 15, tzinfo=timezone.utc))
        self.assertIn("Commits (0", report)
        self.assertIn("Draft activity digest only", report)
        self.assertEqual(fake.call_count, 2)
if __name__ == "__main__":
    unittest.main()
