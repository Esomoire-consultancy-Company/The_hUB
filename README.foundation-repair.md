# The_hUB Foundation Repair R0.1 (review branch — do not merge yet)

Target: `Esomoire-consultancy-Company/The_hUB` on branch `repair/foundation-r0-1-validation`.

This changes **no application deployment** and sends **no marketing or notification messages**.

## Diagnosis
- App: Streamlit, Python >=3.11, `pyproject.toml`, `uv.lock`, Replit/Nix.
- Conda workflow (introduced 2025-06-26 21:53:35 UTC) assumed a missing `environment.yml` and Python 3.10.
- Django workflow refers to absent `requirements.txt` and `manage.py`.
- Separate SQLite concern: `database.py` supplies PostgreSQL-style `connect_timeout` even when using SQLite.
- The SLSA action builds sample artifacts, not this app.

## Branch-only changes
- `foundation-ci.yml` verifies locked Python dependencies and syntax on a PR.
- `python-package-conda.yml` changed to **manual only in this repair branch** to prevent noisy broken push runs during testing. The default branch remains unchanged.
- `marketing-preview.yml`: manually triggered **preview only**; no sending.
- `daily-work-digest.yml`: manually triggered read-only GitHub activity summary; no schedule and no delivery.
- `automation/` and `tests/`: stdlib-only read-only scripts and dry-run safeguards.

## Gate
1. Open draft PR, collect actual GitHub Actions results (including failure evidence).
2. Correct any install, database, or runtime defects without weakening dependencies.
3. Retire obsolete CI only after replacement is proved.
4. Never turn on schedules, recipient delivery or marketing sends without a separate, approved provider/consent/rights review.

Local Python unit tests: three pass. GitHub CI and live integrations not qualified yet.
