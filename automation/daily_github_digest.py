"""Read-only, single-repository GitHub work activity; no notification delivery."""
from datetime import datetime, timedelta, timezone
import html
import json
import os
import re
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen

MAX_API_PAGE = 100
MAX_DISPLAYED = 20

def api_get(path, token):
    req = Request("https://api.github.com" + path, headers={
        "Accept": "application/vnd.github+json",
        "User-Agent": "the-hub-readonly-digest/0.2",
        **({"Authorization": "Bearer " + token} if token else {}),
    })
    with urlopen(req, timeout=15) as response:
        return json.load(response)

def markdown_safe(value, max_len=140):
    raw = re.sub(r"[\r\n\t\x00-\x1f]+", " ", str(value or ""))[:max_len]
    escaped = html.escape(raw, quote=True).replace("@", "&#64;")
    return re.sub(r"([\\\x60*_{}\[\]()#+\-.!|>])",
                  lambda match: "\\" + match.group(1), escaped)

def digest(repository, token, now=None):
    if not isinstance(repository, str) or not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", repository):
        raise ValueError("GITHUB_REPOSITORY must be owner/repository")
    now = now or datetime.now(timezone.utc)
    since_iso = (now - timedelta(days=1)).strftime("%Y-%m-%dT%H:%M:%SZ")
    repo_path = "/repos/" + quote(repository, safe="/")
    lines = [
        f"# Daily GitHub digest — {repository}", "",
        f"Window: {since_iso} through {now.strftime('%Y-%m-%dT%H:%M:%SZ')}", "",
        "**Coverage:** Default-branch commits only, plus this repository's updated issues and PRs. "
        "No claim of activity across all branches, email, calendar, task apps, or offline work.", "",
    ]
    try:
        commits = api_get(repo_path + "/commits?since=" + quote(since_iso) +
                          f"&per_page={MAX_API_PAGE}", token)
        if not isinstance(commits, list):
            raise ValueError("Unexpected commits response")
        lines.append(f"## Default-branch commits ({len(commits)} on first API page)")
        for item in commits[:MAX_DISPLAYED]:
            sha = re.sub(r"[^0-9a-f]", "", str(item.get("sha", "")))[:8]
            message = item.get("commit", {}).get("message", "").split("\n")[0]
            lines.append("- " + sha + " — " + markdown_safe(message))
        if len(commits) > MAX_DISPLAYED:
            lines.append(f"- {len(commits) - MAX_DISPLAYED} additional first-page commits omitted")
        if len(commits) >= MAX_API_PAGE:
            lines.append("- Further pages not fetched; commit coverage is partial")
    except (HTTPError, URLError, TimeoutError, ValueError, TypeError) as exc:
        lines.append(f"Commit source unavailable: {type(exc).__name__}; completeness not claimed.")
    lines.append("")
    try:
        issues = api_get(repo_path + "/issues?state=all&since=" + quote(since_iso) +
                         f"&per_page={MAX_API_PAGE}", token)
        if not isinstance(issues, list):
            raise ValueError("Unexpected issues response")
        relevant = [item for item in issues if item.get("updated_at", "") >= since_iso]
        lines.append(f"## Updated issues and PRs ({len(relevant)} on first API page)")
        for item in relevant[:MAX_DISPLAYED]:
            kind = "PR" if item.get("pull_request") else "Issue"
            number = str(item.get("number", "unknown"))
            lines.append(f"- {kind} #{markdown_safe(number)} — " +
                         markdown_safe(item.get("title", "")))
        if len(relevant) > MAX_DISPLAYED:
            lines.append(f"- {len(relevant) - MAX_DISPLAYED} additional first-page issues/PRs omitted")
        if len(issues) >= MAX_API_PAGE:
            lines.append("- Further pages not fetched; issue/PR coverage is partial")
    except (HTTPError, URLError, TimeoutError, ValueError, TypeError) as exc:
        lines.append(f"Issue/PR source unavailable: {type(exc).__name__}; completeness not claimed.")
    lines += ["", "**Status:** Review-only activity summary. No notification sent.", ""]
    return "\n".join(lines)

if __name__ == "__main__":
    report = digest(os.environ.get("GITHUB_REPOSITORY"), os.environ.get("GITHUB_TOKEN", ""))
    path = os.environ.get("GITHUB_STEP_SUMMARY")
    if path:
        with open(path, "a", encoding="utf-8") as file:
            file.write(report)
    else:
        print(report)
