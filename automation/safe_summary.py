"""Escape untrusted text for GitHub Actions Markdown summaries.

This is presentation sanitation, not a substitute for authorization or consent.
"""
import html
import re

def markdown_safe(value, max_len=140):
    # Eliminate line, bidirectional and invisible Unicode controls before formatting.
    raw = str(value or "")
    raw = re.sub(r"[\x00-\x1f\x7f-\x9f\u2028\u2029\u200e\u200f\u061c\u202a-\u202e\u2066-\u2069]+", " ", raw)
    raw = raw.strip()[:max_len]
    escaped = html.escape(raw, quote=True).replace("@", "&#64;")
    return re.sub(r"([\\`*_{}\[\]()#+\-.!|>])", lambda m: "\\" + m.group(1), escaped)
