# Using the ISEF abstract database

Every ISEF finalist abstract since 2014 is at https://abstracts.societyforscience.org/. This is the real competitor list for a CBIO project.

## The search form

Filters: keyword or phrase, finalist last name, category (about 40), country, US state, year (2014 to the current fair), and a display toggle between "All Abstracts Matching Criteria" and "Only Winning Abstracts". The form posts; search results do not have a shareable URL, so run searches by hand in a browser.

## Stable URLs

- Full abstract: `https://abstracts.societyforscience.org/Home/FullAbstract?ProjectId=<id>`
- Print version: `https://abstracts.societyforscience.org/Home/PrintPdf/<id>`

Project IDs run roughly 5000 (2014) to 26000 (2026). Google indexes the FullAbstract pages, so `site:abstracts.societyforscience.org <keyword>` works as a second search path and is how several rows in this catalog were found.

## Searches to run before we fix our title

Category = Computational Biology and Bioinformatics, years 2021-2026, all abstracts:

- `DepMap`, `dependency`, `CRISPR screen`, `organoid`, `cell line`, `CCLE`, `GDSC`, `Achilles`
- `GBIF`, `iNaturalist`, `citizen science`, `urban`, `heat island`, `melanism`, `pigmentation`, `colour` / `color`, `snail`, `pigeon`, `Cepaea`, `Columba`
- `replication`, `reproducib`, `model fidelity`, `xenograft`, `PDX`

Also run the same keywords in Animal Sciences and Earth and Environmental Sciences, and the Only Winning toggle for each.

Record each hit in `data/projects.csv` (even non-winners; use award = "Finalist (no grand award)") with a one-line summary and what is different about ours. The research plan's "prior work" section should cite the closest two or three by name.

## Faster: the Kaggle dump

William Kaiser scraped 13,543 abstracts (2014-2023) into a Kaggle dataset: https://www.kaggle.com/datasets/wkaisertexas/all-international-science-fair-projects. Load it with pandas and grep the keyword list above in one pass; then check 2024-2026 by hand on the site.
