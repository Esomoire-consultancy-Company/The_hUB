"""Read-only, per-repository GitHub activity digest; no outbound delivery."""
from datetime import datetime, timedelta, timezone
import json
import os
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen

def api_get(path, token):
    req = Request("https://api.github.com" + path, headers={
        "Accept": "application/vnd.github+json",
        "User-Agent": "the-hub-readonly-digest/0.1",
        **({"Authorization": "Bearer " + token} if token else {}),
    })
    with urlopen(req, timeout=15) as response:
        return json.load(response)

def digest(repository, token, now=None):
    if not repository or repository.count("/") != 1:
        raise ValueError("A single GITHUB_REPOSITORY owner/repository is required")
    now = now or datetime.now(timezone.utc)
    since = now - timedelta(days=1)
    since_iso = since.strftime("%Y-%m-%dT%H:%M:%SZ")
    repo_path = "/repos/" + quote(repository, safe="/")
    lines = [f"# Daily GitHub work digest — {repository}", "", f"Window: {since_iso} to {now.strftime('%Y-%m-%dT%H:%M:%SZ')}", "", "**Coverage:** This repository's GitHub data only; not email, calendar, task apps or offline work.", ""]
    try:
        commits = api_get(repo_path + "/commits?since=" + quote(since_iso) + "&per_page=100", token)
        lines.append(f"## Commits ({len(commits)} on first API page)")
        for c in commits[:20]:
            headline = c.get("commit", {}).get("message", "").split("\n")[0].replace("\n", " ")
            lines.append(f"- `{c.get('sha', '')[:8]}` {headline[:140]}")
        if len(commits) >= 100:
            lines.append("- Pagination limit reached; digest is partial")
    except (HTTPError, URLError, ValueError) as exc:
        lines.append(f"Commit source unavailable: {type(exc).__name__}; no completeness claim.")
    lines.append("")
    try:
        issues = api_get(repo_path + "/issues?state=all&since=" + quote(since_iso) + "&per_page=100", token)
        relevant = [x for x in issues if x.get("updated_at", "") >= since_iso]
        lines.append(f"## Updated issues and PRs ({len(relevant)} on first API page)")
        for item in relevant[:20]:
            kind = "PR" if item.get("pull_request") else "Issue"
            lines.append(f"- {kind} #{item.get('number')} — {str(item.get('title', ''))[:140]}")
        if len(issues) >= 100:
            lines.append("- Pagination limit reached; digest is partial")
    except (HTTPError, URLError, ValueError) as exc:
        lines.append(f"Issue/PR source unavailable: {type(exc).__name__}; no completeness claim.")
    lines += ["", "**Status:** Draft activity digest only. No notification sent and no claim of all daily work.", ""]
    return "\n".join(lines)

if __name__ == "__main__":
    report = digest(os.environ.get("GITHUB_REPOSITORY"), os.environ.get("GITHUB_TOKEN", ""))
    path = os.environ.get("GITHUB_STEP_SUMMARY")
    if path:
        with open(path, "a", encoding="utf-8") as f:
            f.write(report)
    else:
        print(report)
