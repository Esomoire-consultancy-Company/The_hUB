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
