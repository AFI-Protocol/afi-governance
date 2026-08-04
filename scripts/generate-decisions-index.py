#!/usr/bin/env python3
"""Regenerate decisions/INDEX.md from Status lines in decisions/*.md.

Does not rewrite accepted decisions. Exit 0 always when decisions/ exists.
"""
from __future__ import annotations

import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DECISIONS = ROOT / "decisions"
OUT = DECISIONS / "INDEX.md"


def main() -> None:
    rows = []
    for p in sorted(DECISIONS.glob("*.md")):
        if p.name == "INDEX.md":
            continue
        t = p.read_text(encoding="utf-8")
        m = re.search(r"\*\*Status:\*\*\s*(.+)", t)
        status_raw = m.group(1).strip() if m else "UNKNOWN"
        # Prefer an explicit bold token immediately after Status; never treat
        # prose like "not accepted until…" as Accepted.
        token_m = re.match(r"\*\*(Accepted|Proposed)\*\*", status_raw, re.I)
        if token_m:
            status = token_m.group(1).capitalize()
            if status.lower() == "accepted":
                status = "Accepted"
            elif status.lower() == "proposed":
                status = "Proposed"
        elif re.match(r"Proposed\b", status_raw, re.I):
            status = "Proposed"
        elif re.match(r"Accepted\b", status_raw, re.I):
            status = "Accepted"
        else:
            status = status_raw[:80]
        title = t.splitlines()[0].lstrip("#").strip() if t.splitlines() else p.name
        gov_m = re.search(r"\(([A-Z0-9]+-GOV)\)", title)
        gov = gov_m.group(1) if gov_m else "—"
        date_m = re.search(r"\*\*Date:\*\*\s*(\S+)", t)
        date = date_m.group(1) if date_m else ""
        rows.append(
            {
                "file": p.name,
                "title": title,
                "gov": gov,
                "status": status,
                "date": date,
                "bytes": len(t.encode("utf-8")),
            }
        )

    lines = [
        "# AFI Governance Decisions Index",
        "",
        "> **Generated register.** Machine-readable companion to `decisions/`.",
        "> Status values are taken from each file's Status line.",
        "> This index does **not** rewrite accepted decisions; it only lists them.",
        "> Regeneration: `python3 scripts/generate-decisions-index.py`.",
        "",
        f"**Count:** {len(rows)} decision files.",
        "",
        "| File | GOV | Status | Date | Bytes | Title |",
        "|---|---|---|---|---:|---|",
    ]
    for r in rows:
        title = r["title"][:80]
        lines.append(
            f"| `{r['file']}` | {r['gov']} | {r['status']} | {r['date']} | {r['bytes']} | {title} |"
        )
    lines.append("")
    lines.append("## Status summary")
    for k, v in sorted(Counter(r["status"] for r in rows).items()):
        lines.append(f"- **{k}:** {v}")
    lines.append("")
    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {OUT} ({len(rows)} decisions)")


if __name__ == "__main__":
    main()
