# The_hUB Foundation Repair R0.2 — isolated review branch

**Scope:** GitHub-only review branch, no changes to default branch, no deployment, no schedules, no outbound marketing messages or notifications.

## Root cause
Original Streamlit/Replit application uses Python >=3.11 and uv lockfile.
GitHub legacy Conda file (2025-06-26) attempted to run a missing Conda executable, and references a missing environment.yml.
Historic failed job: https://github.com/Esomoire-consultancy-Company/The_hUB/actions/runs/43713296321

## Changes
- Build with Python 3.11 and locked uv dependencies; compile and import smoke checks.
- Test SQLite explicitly and with DATABASE_URL absent in a temporary directory; never use the configured production DB.
- Run the non-sending marketing campaign preview and standard-library tests.
- Manual-only Conda legacy template remains available for historical inspection **after merge to default only**.
- Marketing/digest workflows have safe pull_request test triggers for same-repository branches only, plus manual workflow_dispatch available **after they reach the default branch**. Note: GitHub cannot manually dispatch a new workflow defined on an unmerged review branch.
- Read-only daily digest covers **default-branch commits and repository updated issues/PRs only**, first 100 records per source (displaying up to 20 with an explicit omitted count). It does not claim all work or all branches.
- All campaign data is placeholder/empty. Do not commit sensitive recipients or personal campaign lists to this public repository. Consent references are not verified. Never send based on a preview.
- Escape untrusted API field strings in summaries; handle API timeouts and incomplete results.

## Gates
1. Inspect all GitHub Actions run logs, PR review comments, and tests.
2. Test Streamlit first render in a disposable environment before considering runtime-qualified.
3. Review external provider, database and licensing representations: the demo HTML advertises a licence valid through April 2026, which should not be represented as a currently verified entitlement.
4. Retire Conda/Django templates and review sample SLSA workflow in a separate, authorized deployment PR.
5. Marketing: confirm recipients, records of consent, creative approval, suppression/opt-out and provider before any delivery.
6. Daily notification: confirm scope, timezone, time, destination and access permissions before any schedule or sending.

**Current status:** Branch-only PRE-PRODUCTION REVIEW. Draft PR must remain unmerged until gates pass.

## R0.3 additional controls (review branch)
- Centralize Markdown summary escaping; strip newline, Unicode bidi and control characters. Nothing is sent.
- Make demo-only company/role selection explicit. It must never mark a person as authenticated.
- Replace unverified live-licence claims with clearly historical demo references.
- Run a UI interaction smoke to verify demo navigation does not establish real authorization.
- This is **not** a replacement for real SSO, DigitalMe, Warden, or externally effective authorization.

## R0.4 sample-data safety and activation boundary

- The prior `app.py` automatically invoked `initialize_database()` on first render. This could create tables and insert demonstration records into any configured database that lacked buyers.
- In the review branch, sample-data seeding fails closed unless **all** of `THE_HUB_DEMO_MODE=1`, `THE_HUB_ALLOW_SAMPLE_SEED=1`, and an explicit `DATABASE_URL=sqlite:///...` are present. Unset URLs and PostgreSQL cannot be seeded by this demo path.
- The database management UI cannot operate unless the same demo-only gate passes.
- The destructive browser "Reset Database" control has been removed; no browser-triggered table dropping is offered.
- CI tests normal app first render with a disposable SQLite file path and verifies that no file is created. Separately, the demo navigation test opts in with disposable SQLite synthetic data.
- These safeguards are deliberately separate from actual identity, regulated data, company access or licence governance.

## R0.4 review fixes
- The earlier notice overstated safety by claiming "no external execution"; it now warns that **this is a demo and only disposable SQLite should be connected**. A UI notice is not an isolation boundary.
- The demo selector clears the keys used by the old pseudo-login (`authenticated`, `company`, `role`) before navigation.
- The selected company and role appear only as **example context** on the static VOI demo; this cannot confer access to the selected organization.
- UI smoke deliberately injects a truthy legacy authentication value and verifies it is cleared.
- Report sanitizer now removes U+200E/U+200F/U+061C directional marks; regression tests assert Unicode separators are removed.

## R0.5 database release gate

- Database-backed routes now display a clear unavailable state when explicit SQLite demo configuration is absent. The routes are `manufacturing_dashboard`, `order_style_management`, `material_tracker`, `production_timeline`, `line_plan`, `reports`, `db_initialization`, `supply_chain_visualization` and `inventory_export`.
- The optional demo-seeding caption distinguishes newly added records from previously existing records.
- Tests cover default `os.environ` lookup and all nine routes in an unseeded disposable SQLite environment.
- Known write paths remain in `db_operations.py`, `order_style_management.py`, `material_tracker.py`, `line_plan.py` and schema creation in `manufacturing_dashboard.py`. They are **not production-authorized**; see `README.database-write-inventory.md`.
