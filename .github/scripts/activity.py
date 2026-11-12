#!/usr/bin/env python3
"""Draw the profile activity card (assets/activity-dark.svg, assets/activity-light.svg).

Asks GitHub's GraphQL API for contribution totals of the last 12 months and a weekly calendar.
Only numbers are requested and drawn: no repository, organisation, pull request or commit names
are ever fetched, so private work can show up as a count and nothing else.

Env: STATS_TOKEN (read-only token of the profile owner), LOGIN (GitHub login).
Exit 0 and write nothing if the numbers did not change.
"""
import json
import os
import re
import sys
import urllib.request

LOGIN = os.environ.get("LOGIN", "BoogieManN8")
TOKEN = os.environ.get("STATS_TOKEN", "")
OUT = os.path.join(os.path.dirname(__file__), "..", "..", "assets")

QUERY = """
query($login: String!) {
  user(login: $login) {
    contributionsCollection {
      totalCommitContributions
      totalPullRequestContributions
      totalPullRequestReviewContributions
      totalIssueContributions
      totalRepositoriesWithContributedCommits
      restrictedContributionsCount
      contributionCalendar {
        totalContributions
        weeks { contributionDays { contributionCount } }
      }
    }
  }
}
"""

THEMES = {
    "dark": dict(bg1="#0D1117", bg2="#0B1410", border="#1F3A2A", text="#F0F6FC", muted="#8B949E",
                 accent="#39D353", bar="#21262D"),
    "light": dict(bg1="#FFFFFF", bg2="#F3F8F4", border="#C9DCCF", text="#1F2328", muted="#59636E",
                  accent="#1A7F37", bar="#D1D9E0"),
}

# Every piece of text that may appear in the card. Anything else must be a number.
LABELS = {"LAST 12 MONTHS", "contributions", "commits", "pull requests", "code reviews", "repositories",
          "Weekly activity"}
NUMBER = re.compile(r"^[0-9][0-9,]*$")


def fetch():
    if not TOKEN:
        sys.exit("STATS_TOKEN is not set")
    body = json.dumps({"query": QUERY, "variables": {"login": LOGIN}}).encode()
    req = urllib.request.Request("https://api.github.com/graphql", data=body, headers={
        "Authorization": f"bearer {TOKEN}", "Content-Type": "application/json",
        "User-Agent": "profile-activity-card"})
    with urllib.request.urlopen(req, timeout=30) as r:
        data = json.load(r)
    if data.get("errors"):
        sys.exit("GraphQL error: " + "; ".join(e.get("message", "?") for e in data["errors"]))
    c = data["data"]["user"]["contributionsCollection"]
    weeks = [sum(d["contributionCount"] for d in w["contributionDays"])
             for w in c["contributionCalendar"]["weeks"]][-52:]
    return {
        "total": c["contributionCalendar"]["totalContributions"],
        "commits": c["totalCommitContributions"],
        "prs": c["totalPullRequestContributions"],
        "reviews": c["totalPullRequestReviewContributions"],
        "repos": c["totalRepositoriesWithContributedCommits"],
        "weeks": weeks,
    }


def fmt(n):
    return f"{n:,}"


def svg(stats, t):
    W, H = 880, 230
    texts = []

    def text(x, y, s, cls, fill, anchor="start", size=None):
        texts.append(s)
        sz = f' font-size="{size}"' if size else ""
        return f'<text x="{x}" y="{y}" class="{cls}" fill="{fill}" text-anchor="{anchor}"{sz}>{s}</text>'

    parts = []
    parts.append(text(40, 46, "LAST 12 MONTHS", "mono", t["accent"], size=13))
    tiles = [("contributions", stats["total"]), ("commits", stats["commits"]),
             ("pull requests", stats["prs"]), ("code reviews", stats["reviews"]),
             ("repositories", stats["repos"])]
    tile_w = (W - 80) / len(tiles)
    for i, (label, value) in enumerate(tiles):
        x = 40 + i * tile_w
        if i:
            parts.append(f'<rect x="{x - 1:.1f}" y="66" width="1" height="52" fill="{t["border"]}"/>')
        pad = 0 if i == 0 else 18
        parts.append(text(f"{x + pad:.1f}", 98, fmt(value), "sans num", t["text"], size=30))
        parts.append(text(f"{x + pad:.1f}", 118, label, "sans", t["muted"], size=13))

    # weekly bars
    weeks = stats["weeks"] or [0]
    peak = max(weeks) or 1
    bx, by, bw, bh = 40, 150, W - 80, 52
    gap = 3
    n = len(weeks)
    w = (bw - gap * (n - 1)) / n
    bars = []
    for i, v in enumerate(weeks):
        h = max(2.0, bh * v / peak)
        fill = t["accent"] if v else t["bar"]
        op = 0.35 + 0.65 * (v / peak) if v else 1
        bars.append(f'<rect x="{bx + i * (w + gap):.1f}" y="{by + bh - h:.1f}" width="{w:.1f}" height="{h:.1f}" '
                    f'rx="1.5" fill="{fill}" fill-opacity="{op:.2f}"/>')
    parts.append(text(W - 40, 46, "Weekly activity", "sans", t["muted"], "end", 13))

    for s in texts:
        if s not in LABELS and not NUMBER.match(s):
            sys.exit(f"refusing to write: unexpected text in card: {s!r}")

    alt = (f"GitHub activity over the last 12 months: {fmt(stats['total'])} contributions, "
           f"{fmt(stats['commits'])} commits, {fmt(stats['prs'])} pull requests, "
           f"{fmt(stats['reviews'])} code reviews, {fmt(stats['repos'])} repositories.")
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-labelledby="t d">
  <title id="t">GitHub activity, last 12 months</title>
  <desc id="d">{alt}</desc>
  <style>
    .sans {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; }}
    .mono {{ font-family: ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, monospace; letter-spacing: 2px; }}
    .num {{ font-weight: 700; }}
  </style>
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="{t['bg1']}"/><stop offset="1" stop-color="{t['bg2']}"/>
    </linearGradient>
  </defs>
  <rect x="0.5" y="0.5" width="{W - 1}" height="{H - 1}" rx="14" fill="url(#bg)" stroke="{t['border']}"/>
  {chr(10).join('  ' + p for p in parts).strip()}
  {''.join(bars)}
</svg>
"""


def main():
    stats = fetch()
    changed = False
    for name, theme in THEMES.items():
        path = os.path.normpath(os.path.join(OUT, f"activity-{name}.svg"))
        new = svg(stats, theme)
        old = open(path).read() if os.path.exists(path) else ""
        if new != old:
            with open(path, "w") as f:
                f.write(new)
            changed = True
    print("changed" if changed else "unchanged")


if __name__ == "__main__":
    main()
