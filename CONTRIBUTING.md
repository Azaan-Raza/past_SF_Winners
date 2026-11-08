# Contributing

This is a two-person research notebook that happens to be a repo. Keep it that way: every row traceable to a source, every claim in `analysis/` pointing at row IDs.

- Add entries with `templates/project-entry.md`.
- Never add a row from memory. If you cannot find the source, open an issue with what you remember and we will look it up.
- Run `python3 scripts/validate.py` before committing. CI runs it too.
- Regenerate tables with `python3 scripts/build_readme.py` and commit the output. Do not hand-edit anything between `<!-- BEGIN GENERATED -->` and `<!-- END GENERATED -->`.
- Hand-written text goes above or below the generated blocks.
- Project titles and abstracts belong to their authors. Quote titles; paraphrase abstracts; always link.
- Plain language. No em dashes.
