#!/usr/bin/env python3
"""Regenerate every table in the repo from data/projects.csv.

Usage:  python3 scripts/build_readme.py

Each Markdown page keeps its hand-written text and has one or more blocks like

    <!-- BEGIN GENERATED: <block-name> -->
    ...
    <!-- END GENERATED -->

This script rewrites only what is between the markers. Edit the CSV, run the
script, commit both. Stdlib only.
"""
from __future__ import annotations

import csv
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CSV = ROOT / "data" / "projects.csv"
JSON = ROOT / "data" / "projects.json"

AWARD_RANK = [
    ("yancopoulos", 0), ("gordon e. moore", 0), ("1st place", 0), ("first", 0),
    ("young scientist", 1), ("barrett", 1), ("horvitz", 1), ("scripps", 1), ("coleman", 1),
    ("siyss", 1), ("laureate", 1), ("grand prize", 1), ("best of category", 1), ("1st award", 1),
    ("2nd", 2), ("second", 2), ("3rd", 3), ("third", 3), ("4th", 4), ("fourth", 4),
    ("5th", 5), ("6th", 6), ("7th", 7), ("8th", 8), ("9th", 9), ("10th", 10),
]


def load() -> list[dict]:
    with CSV.open(encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    for r in rows:
        r["year_i"] = int(r["year"])
        r["tag_set"] = set(t for t in r["tags"].split(";") if t)
        r["rel_set"] = set(t for t in r["relevance"].split(";") if t)
    return rows


def award_rank(award: str) -> int:
    a = award.lower()
    for key, rank in AWARD_RANK:
        if key in a:
            return rank
    return 50


def esc(s: str) -> str:
    return s.replace("|", "\\|").replace("\n", " ").strip()


def link(r: dict, text: str | None = None) -> str:
    return f"[{esc(text or r['title'])}]({r['source_url']})"


def title_cell(r: dict) -> str:
    t = link(r)
    if r["title_status"] == "abbreviated":
        t += " *(title cut in source)*"
    elif r["title_status"] == "paraphrased":
        t += " *(paraphrased)*"
    return t


def table(rows: list[dict], cols: list[str]) -> str:
    headers = {
        "year": "Year", "competition": "Competition", "award": "Award", "category": "Category",
        "students": "Student(s)", "school": "School", "location": "Where", "title": "Project",
        "summary": "What they did", "data_sources": "Data", "lesson": "Takeaway for us", "methods": "Methods",
    }
    out = ["| " + " | ".join(headers[c] for c in cols) + " |", "|" + "---|" * len(cols)]
    for r in rows:
        cells = []
        for c in cols:
            if c == "title":
                cells.append(title_cell(r))
            else:
                cells.append(esc(r[c]))
        out.append("| " + " | ".join(cells) + " |")
    return "\n".join(out)


def sort_rows(rows: list[dict]) -> list[dict]:
    return sorted(rows, key=lambda r: (-r["year_i"], award_rank(r["award"]), r["competition"], r["students"]))


# ---------------------------------------------------------------- blocks ----
def block_readme_stats(rows):
    comps = Counter(r["competition"] for r in rows)
    years = sorted({r["year_i"] for r in rows})
    rel = Counter(t for r in rows for t in r["rel_set"])
    lines = [
        f"**{len(rows)} catalogued projects** from {years[0]} to {years[-1]}, across {len(comps)} competitions.",
        "",
        "| Competition | Entries |", "|---|---|",
    ]
    for c, n in comps.most_common():
        lines.append(f"| {c} | {n} |")
    lines += ["", "| Relevance tag | Entries | Meaning |", "|---|---|---|"]
    meaning = {
        "cancer-lead": "informs the cancer-dependency / model-fidelity lead (PD1-CAN-01)",
        "evo-leads": "informs the urban-evolution snail and pigeon leads (PD1-EVO-01/02)",
        "compbio": "computational biology in general",
        "acsef-path": "Alameda County / Quarry Lane / Dublin pathway precedents",
        "general": "context: what top awards look like outside comp bio",
    }
    for t in ["cancer-lead", "evo-leads", "compbio", "acsef-path", "general"]:
        lines.append(f"| `{t}` | {rel.get(t, 0)} | {meaning[t]} |")
    return "\n".join(lines)


def block_readme_top(rows):
    """Highest-signal entries: a written lesson AND direct relevance to one of our leads."""
    want = {"cancer-lead", "evo-leads", "acsef-path"}
    sel = [r for r in rows if r["lesson"] and r["rel_set"] & want]
    sel = sort_rows(sel)
    return table(sel, ["year", "competition", "award", "students", "title", "lesson"])


def block_lessons_all(rows):
    """Every entry with a written lesson, including general top-award context."""
    sel = sort_rows([r for r in rows if r["lesson"]])
    return table(sel, ["year", "competition", "award", "students", "title", "lesson"])


def block_competition(rows, comp: str):
    sel = sort_rows([r for r in rows if r["competition"] == comp])
    by_year = defaultdict(list)
    for r in sel:
        by_year[r["year_i"]].append(r)
    out = []
    for y in sorted(by_year, reverse=True):
        out.append(f"### {y}\n")
        out.append(table(by_year[y], ["award", "category", "students", "school", "title", "summary"]))
        out.append("")
    return "\n".join(out).rstrip()


def block_relevance(rows, tag: str):
    sel = sort_rows([r for r in rows if tag in r["rel_set"]])
    return table(sel, ["year", "competition", "award", "students", "title", "summary", "data_sources", "lesson"])


def block_tag(rows, tags: list[str]):
    want = set(tags)
    sel = sort_rows([r for r in rows if r["tag_set"] & want])
    return table(sel, ["year", "competition", "award", "students", "title", "summary", "data_sources"])


def block_multi_year(rows):
    sel = sort_rows([r for r in rows if "multi-year" in r["tag_set"]])
    return table(sel, ["year", "competition", "award", "students", "title", "summary"])


def block_public_data(rows):
    sel = sort_rows([r for r in rows if "public-data" in r["tag_set"]])
    return table(sel, ["year", "competition", "award", "students", "title", "data_sources"])


def block_teams(rows):
    sel = sort_rows([r for r in rows if "team" in r["tag_set"] or ";" in r["students"]])
    return table(sel, ["year", "competition", "award", "students", "title"])


def block_bay_area(rows):
    want = {"bay-area", "alameda", "dublin", "quarry-lane", "california"}
    sel = sort_rows([r for r in rows if r["tag_set"] & want])
    return table(sel, ["year", "competition", "award", "students", "school", "title"])


BLOCKS = {
    "readme-stats": block_readme_stats,
    "readme-top": block_readme_top,
    "lessons-all": block_lessons_all,
    "comp-ISEF": lambda rows: block_competition(rows, "ISEF"),
    "comp-STS": lambda rows: block_competition(rows, "STS"),
    "comp-CSEF": lambda rows: block_competition(rows, "CSEF"),
    "comp-ACSEF": lambda rows: block_competition(rows, "ACSEF"),
    "comp-JSHS": lambda rows: block_competition(rows, "JSHS"),
    "comp-Davidson": lambda rows: block_competition(rows, "Davidson Fellows"),
    "comp-JIC": lambda rows: block_competition(rows, "Thermo Fisher JIC"),
    "comp-GSF": lambda rows: block_competition(rows, "Google Science Fair"),
    "comp-Siemens": lambda rows: block_competition(rows, "Siemens Competition"),
    "comp-BioGENEius": lambda rows: block_competition(rows, "BioGENEius Challenge"),
    "comp-Synopsys": lambda rows: block_competition(rows, "Synopsys Championship"),
    "rel-cancer-lead": lambda rows: block_relevance(rows, "cancer-lead"),
    "rel-evo-leads": lambda rows: block_relevance(rows, "evo-leads"),
    "rel-acsef-path": lambda rows: block_relevance(rows, "acsef-path"),
    "tag-cv": lambda rows: block_tag(rows, ["cv", "histopathology", "medical-imaging", "imaging"]),
    "tag-protein": lambda rows: block_tag(rows, ["protein-structure", "protein-design", "antibody-design", "alphafold", "embeddings", "md"]),
    "tag-drug": lambda rows: block_tag(rows, ["drug-discovery", "drug-repurposing", "drug-response", "drug-synergy", "drug-resistance"]),
    "tag-omics": lambda rows: block_tag(rows, ["multi-omics", "single-cell", "spatial-omics", "transcriptomics", "genomics", "methylation", "epigenetics", "3d-genome", "strs", "variants", "cnv", "driver-genes", "mirna", "rna", "ribosome-profiling"]),
    "tag-epi": lambda rows: block_tag(rows, ["epidemiology", "forecasting", "spatiotemporal", "geospatial", "remote-sensing", "virology", "evolution", "population-genetics", "phylogenetics"]),
    "tag-ecology": lambda rows: block_tag(rows, ["ecology", "citizen-science", "ebird", "conservation", "animal-sciences", "animal-behavior", "field-plus-compute", "acoustics", "snails", "invasive-species", "plant-pathology", "plant-sciences", "ecology-monitoring", "wildlife", "insects", "mosquito", "bees", "coral", "birds"]),
    "tag-clinical": lambda rows: block_tag(rows, ["clinical-ml", "wearables", "eeg", "neuroscience", "neuroimaging", "alzheimers", "dementia", "signals", "diagnostics", "digital-biomarker"]),
    "multi-year": block_multi_year,
    "public-data": block_public_data,
    "teams": block_teams,
    "bay-area": block_bay_area,
}

MARK = re.compile(r"<!-- BEGIN GENERATED: ([\w-]+) -->\n.*?<!-- END GENERATED -->", re.S)


def render(path: Path, rows: list[dict]) -> int:
    text = path.read_text(encoding="utf-8")
    n = 0

    def sub(m):
        nonlocal n
        name = m.group(1)
        if name not in BLOCKS:
            raise SystemExit(f"{path}: unknown block {name!r}")
        n += 1
        body = BLOCKS[name](rows)
        return f"<!-- BEGIN GENERATED: {name} -->\n{body}\n<!-- END GENERATED -->"

    new = MARK.sub(sub, text)
    if new != text:
        path.write_text(new, encoding="utf-8")
    return n


def main():
    rows = load()
    # keep JSON in sync with CSV
    slim = [{k: v for k, v in r.items() if k not in ("year_i", "tag_set", "rel_set")} for r in rows]
    JSON.write_text(json.dumps(slim, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    total = 0
    for md in sorted(ROOT.rglob("*.md")):
        if ".git" in md.parts or "node_modules" in md.parts:
            continue
        total += render(md, rows)
    print(f"{len(rows)} records; refreshed {total} generated blocks")


if __name__ == "__main__":
    main()
