"""Strict opt-in gate for synthetic sample data; never used as real authorization."""
import os


def sample_seed_permitted(environ=None):
    env = os.environ if environ is None else environ
    url = env.get("DATABASE_URL", "")
    # A deliberately explicit, local SQLite-only demo configuration.
    # Production databases, unset URLs, SQLite URI mode, and unknown drivers fail closed.
    return (
        env.get("THE_HUB_DEMO_MODE") == "1"
        and env.get("THE_HUB_ALLOW_SAMPLE_SEED") == "1"
        and isinstance(url, str)
        and url.startswith("sqlite:///")
        and len(url) > len("sqlite:///")
        and not url.startswith("sqlite:///file:")
        and not any(c in url for c in ("?", "#", "\x00"))
    )
