#!/usr/bin/env python3
"""Validate data/projects.csv. Exit code 1 on any problem.

Usage:  python3 scripts/validate.py
"""
from __future__ import annotations

import csv
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CSV = ROOT / "data" / "projects.csv"

FIELDS = ["id", "year", "competition", "level", "award", "category", "students", "school", "location",
          "title", "title_status", "summary", "methods", "data_sources", "tags", "relevance", "lesson",
          "source_url"]
TITLE_STATUS = {"verbatim", "abbreviated", "paraphrased"}
LEVELS = {"international", "national", "state", "regional"}
RELEVANCE = {"cancer-lead", "evo-leads", "compbio", "acsef-path", "general"}
COMPETITIONS = {"ISEF", "STS", "CSEF", "ACSEF", "JSHS", "Davidson Fellows", "Thermo Fisher JIC",
                "Google Science Fair", "Siemens Competition", "BioGENEius Challenge", "Synopsys Championship"}
ID_RE = re.compile(r"^[A-Z]+-\d{4}-[A-Za-z0-9-]+$")


def main() -> int:
    problems: list[str] = []
    with CSV.open(encoding="utf-8") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames != FIELDS:
            problems.append(f"header mismatch: {reader.fieldnames}")
        rows = list(reader)

    ids = Counter(r["id"] for r in rows)
    for i, n in ids.items():
        if n > 1:
            problems.append(f"duplicate id {i} ({n}x)")

    for r in rows:
        rid = r["id"]
        if not ID_RE.match(rid):
            problems.append(f"{rid}: bad id format")
        if not r["year"].isdigit() or not (2000 <= int(r["year"]) <= 2100):
            problems.append(f"{rid}: bad year {r['year']!r}")
        if r["competition"] not in COMPETITIONS:
            problems.append(f"{rid}: unknown competition {r['competition']!r}")
        if r["level"] not in LEVELS:
            problems.append(f"{rid}: bad level {r['level']!r}")
        if r["title_status"] not in TITLE_STATUS:
            problems.append(f"{rid}: bad title_status {r['title_status']!r}")
        for req in ("award", "category", "students", "title", "source_url"):
            if not r[req].strip():
                problems.append(f"{rid}: empty {req}")
        if not r["source_url"].startswith("http"):
            problems.append(f"{rid}: source_url is not a URL")
        rel = [t for t in r["relevance"].split(";") if t]
        if not rel:
            problems.append(f"{rid}: no relevance tag")
        for t in rel:
            if t not in RELEVANCE:
                problems.append(f"{rid}: unknown relevance tag {t!r}")
        for t in r["tags"].split(";"):
            if t and not re.match(r"^[a-z0-9-]+$", t):
                problems.append(f"{rid}: tag {t!r} must be lowercase kebab-case")
        if r["title_status"] == "abbreviated" and "[...]" not in r["title"]:
            problems.append(f"{rid}: abbreviated title should end with [...]")

    if problems:
        print("\n".join(problems))
        print(f"\n{len(problems)} problem(s) in {len(rows)} rows")
        return 1
    print(f"OK: {len(rows)} rows, {len(ids)} unique ids, all sources present")
    return 0


if __name__ == "__main__":
    sys.exit(main())
