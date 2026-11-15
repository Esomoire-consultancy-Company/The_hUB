"""Synthetic data seeding must fail closed without two explicit demo flags."""
import unittest
from demo_seed_policy import sample_seed_permitted


class DemoSeedPolicyTests(unittest.TestCase):
    def test_disabled_by_default(self):
        self.assertFalse(sample_seed_permitted({}))
        self.assertFalse(sample_seed_permitted({"DATABASE_URL": "sqlite:///example.db"}))

    def test_requires_both_explicit_flags_and_sqlite(self):
        base = {"DATABASE_URL": "sqlite:///sandbox.db",
                "THE_HUB_DEMO_MODE": "1",
                "THE_HUB_ALLOW_SAMPLE_SEED": "1"}
        self.assertTrue(sample_seed_permitted(base))
        for key in ("THE_HUB_DEMO_MODE", "THE_HUB_ALLOW_SAMPLE_SEED"):
            altered = base.copy()
            altered.pop(key)
            self.assertFalse(sample_seed_permitted(altered))

    def test_rejects_postgres_and_sqlite_uri(self):
        for url in ("postgresql://user@example.com/db",
                    "sqlite:///file:db?mode=rw",
                    "sqlite://", "sqlite:///"):
            self.assertFalse(sample_seed_permitted({
                "DATABASE_URL": url,
                "THE_HUB_DEMO_MODE": "1",
                "THE_HUB_ALLOW_SAMPLE_SEED": "1"
            }))

    def test_explicit_synthetic_in_memory_sqlite_allowed(self):
        self.assertTrue(sample_seed_permitted({
            "DATABASE_URL": "sqlite:///:memory:",
            "THE_HUB_DEMO_MODE": "1",
            "THE_HUB_ALLOW_SAMPLE_SEED": "1"
        }))


if __name__ == "__main__":
    unittest.main()
