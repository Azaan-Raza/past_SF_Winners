# Adding a project

1. Find the primary source: the competition's own award list, the ISEF abstract page, the STS Finalist Book or finalist page, or the fair's official results document. News articles are acceptable only when no official page exists; say so in `summary`.
2. Add one row to `data/projects.csv`. Columns are defined in `data/schema.md`. Minimum: `id`, `year`, `competition`, `level`, `award`, `category`, `students`, `title`, `title_status`, `relevance`, `source_url`.
3. If the title in the source is cut off, keep the verbatim part, end it with ` [...]`, and set `title_status = abbreviated`. If the source gives no formal title, write a short description ending in ` [paraphrased]` and set `title_status = paraphrased`.
4. Put datasets in `data_sources` exactly as the source names them. If you are inferring (for example "TCGA" from a title), add "(likely)".
5. Write `lesson` only if the project tells us something specific about our own leads. Rows with a lesson appear in the README short list, so keep it to one sentence.
6. Run `python3 scripts/validate.py` then `python3 scripts/build_readme.py`. Commit the CSV, the JSON and the regenerated Markdown together.

## Row template

```
id:            ISEF-2027-CBIO-1-surname
year:          2027
competition:   ISEF
level:         international
award:         1st Award ($6,000)
category:      Computational Biology and Bioinformatics
students:      First Last; First Last
school:        School Name
location:      City, ST, Country
title:         Exact Title From Source
title_status:  verbatim
summary:       One or two sentences on what they did, from the source.
methods:       method1; method2
data_sources:  Dataset A; Dataset B (likely)
tags:          cancer;public-data;team
relevance:     cancer-lead;compbio
lesson:        One sentence, only if it changes what we do.
source_url:    https://...
```
