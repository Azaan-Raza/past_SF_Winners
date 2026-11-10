# ISEF/STS reference index

This proposed reference edition contains 17,667 source-identified competition appearances. It is a link index with attributed analysis, not a republished collection of student abstracts or documents. All files are privately staged pending final review and separate integration authorization.

The historical ISEF collection and Azaan's curated ISEF/STS selection remain distinct in `collection_memberships`. The 329 matching ISEF rows are aliases to existing appearances. The 104 STS entries remain separate competition appearances. Azaan's original 500-row catalogue and generated pages are not replaced.

`project_records` are source-scoped mentions. They do not prove that two appearances are different scientific projects. `scientific_projects` and `project_identity_links` are intentionally empty until project-family identities are adjudicated. Never report the appearance count as a unique-project count.

The candidate retains source and assertion identifiers, stable links, preferred correction provenance, missing-value states, separate award-assertion records, eligible original Azaan annotations, and asset fingerprints. It reproduces no third-party titles, abstracts, award descriptions, student roster, schools/locations or bulk assets. Withheld values are distinct from values missing in the source. Blank award fields do not establish nonwinner status. Award rows are source-specific assertions, not deduplicated prizes.

Eleven unresolved identity entries and their 77 affected asset occurrences are excluded. Sixty-seven other-competition catalogue entries remain in the original repository outside this edition. Unresolved category and weaker alias evidence is visible in the public issue table. Structured person/project relationship hypotheses are not exported. Annotations may discuss cross-event connections without establishing them.

Azaan annotations are credited analysis and may contain unverified or explicitly qualified claims. They do not establish official scientific findings, project identity or causal conclusions. Summary narratives, relevance-to-personal-research fields and personalized advice are omitted; original values remain preserved outside this candidate.

See `schema.json`, `PUBLIC_EXPORT_POLICY.json`, `SOURCE_RIGHTS.md`, `ATTRIBUTION.md`, and `RELEASE_METADATA.json`. Dataset files are UTF-8 JSON Lines with explicit keys and nullable values. The root `PUBLIC_CANDIDATE_SHA256SUMS.txt` covers the proposed addition files. Run `python scripts/validate_isef_sts_reference.py --integrated` after a separately authorized integration.

These are same-run producer checks, not an independent external audit or legal permission to publish. Universal historical completeness and a unique scientific-project count remain unestablished.

This corrected candidate applies an explicit source and post visibility rule. It retains all 17,667 competition appearances and all 433 curated links, with 31,950 supported asset references and 31,785 distinct fingerprints. Restricted and unverified references, dependent source-only claims and unused fingerprints are withheld. The complete original histories remain privately preserved. Public source visibility supports this limited reference use; it does not grant a licence to copy linked materials. A focused independent re-review and separate integration authorization remain required.

Coverage documentation for candidate 1.0-rc3

This revision changes the coverage explanation and aggregate reporting. It preserves all 17,667 competition appearances, all 433 Azaan relationships, all 31,950 retained asset references and all 31,785 retained fingerprints. The 22,756 withheld references remain excluded. Focused independent verification of this exact documentation correction is required before separate integration authorization.

The private evidence archive and this public reference collection have different scopes. The private archive preserves original files, historical versions, withheld associations and quarantined evidence. This public collection contains only selected links, reference metadata and fingerprints; it contains no original asset payloads. Its 54,706-reference baseline is the earlier privately staged proposal AFTER identity quarantine but BEFORE visibility filtering. It is not a count of the full private archive, and does not mean all baseline references were ever approved for publication. The 11 quarantined records and their 77 asset occurrences were already outside that baseline and must not be subtracted again.

Each count below is an asset-reference occurrence, not a unique project, document, presentation or fingerprint. A project may have many slide/image references, and the same bytes may have more than one occurrence. The retained occurrence count of 31,950 corresponds to 31,785 distinct fingerprints. Historical ISEF records and the curated Azaan selection remain distinct.

For every row, withheld = baseline - retained; retention percent = 100 × retained / baseline; withheld percent = 100 × withheld / baseline. Both rates use that row's baseline, and are rounded to six decimal places using decimal half-up rounding. For a zero baseline the percentage is undefined: N/A here, an empty field in CSV, and null in JSON. Zero-baseline rows are not 0% or 100% retention claims. These overlapping summary tables must not be added to each other.

The complete [COVERAGE.csv](COVERAGE.csv) has 84 mutually exclusive competition × year × asset-type cells: both competitions, every year represented by the appearance collection (2013–2026), and all three asset types, including zero-baseline combinations. Summing this atomic table once gives the overall totals. RELEASE_METADATA.json supplies the same denominator definitions, yearly/type summaries and the table's SHA-256 identity.

Overall, 54,706 baseline references become 31,950 retained and 22,756 withheld: 58.403100% retained and 41.596900% withheld.

Coverage by year (ISEF and STS combined; every nonzero asset count originates from ISEF ProjectBoard):

| Year | Baseline references | Retained | Withheld | Retention % | Withheld % |
| --- | ---: | ---: | ---: | ---: | ---: |
| 2013 | 0 | 0 | 0 | N/A | N/A |
| 2014 | 0 | 0 | 0 | N/A | N/A |
| 2015 | 0 | 0 | 0 | N/A | N/A |
| 2016 | 0 | 0 | 0 | N/A | N/A |
| 2017 | 0 | 0 | 0 | N/A | N/A |
| 2018 | 0 | 0 | 0 | N/A | N/A |
| 2019 | 0 | 0 | 0 | N/A | N/A |
| 2020 | 0 | 0 | 0 | N/A | N/A |
| 2021 | 17,653 | 17,653 | 0 | 100.000000 | 0.000000 |
| 2022 | 1,601 | 1,601 | 0 | 100.000000 | 0.000000 |
| 2023 | 1,354 | 1,353 | 1 | 99.926145 | 0.073855 |
| 2024 | 1,376 | 1,376 | 0 | 100.000000 | 0.000000 |
| 2025 | 16,190 | 502 | 15,688 | 3.100679 | 96.899321 |
| 2026 | 16,532 | 9,465 | 7,067 | 57.252601 | 42.747399 |

Coverage by asset type:

| Asset type | Baseline references | Retained | Withheld | Retention % | Withheld % |
| --- | ---: | ---: | ---: | ---: | ---: |
| presentations | 46,293 | 25,277 | 21,016 | 54.602208 | 45.397792 |
| quad_charts | 8,410 | 6,670 | 1,740 | 79.310345 | 20.689655 |
| supplementary_presentations | 3 | 3 | 0 | 100.000000 | 0.000000 |

Year-by-type breakdown for nonzero baselines (all zero combinations and the competition split are also included in COVERAGE.csv):

| Year / asset type | Baseline references | Retained | Withheld | Retention % | Withheld % |
| --- | ---: | ---: | ---: | ---: | ---: |
| 2021 / presentations | 16,258 | 16,258 | 0 | 100.000000 | 0.000000 |
| 2021 / quad_charts | 1,395 | 1,395 | 0 | 100.000000 | 0.000000 |
| 2022 / presentations | 11 | 11 | 0 | 100.000000 | 0.000000 |
| 2022 / quad_charts | 1,587 | 1,587 | 0 | 100.000000 | 0.000000 |
| 2022 / supplementary_presentations | 3 | 3 | 0 | 100.000000 | 0.000000 |
| 2023 / quad_charts | 1,354 | 1,353 | 1 | 99.926145 | 0.073855 |
| 2024 / quad_charts | 1,376 | 1,376 | 0 | 100.000000 | 0.000000 |
| 2025 / presentations | 14,847 | 450 | 14,397 | 3.030915 | 96.969085 |
| 2025 / quad_charts | 1,343 | 52 | 1,291 | 3.871929 | 96.128071 |
| 2026 / presentations | 15,177 | 8,558 | 6,619 | 56.387955 | 43.612045 |
| 2026 / quad_charts | 1,355 | 907 | 448 | 66.937269 | 33.062731 |

Why the 2025 reduction is disproportionately large

2025 asset references declined from 16,190 to 502 following public-release visibility filtering: 15,688 withheld, a 96.899321% reduction (approximately 96.9%), and 3.100679% retained. The exclusion evidence accounts for that loss exactly:

| 2025 exclusion evidence | Presentations | Quad charts | Total references |
| --- | ---: | ---: | ---: |
| Affirmative private/restricted flags | 1,965 | 87 | 2,052 |
| Unverified public visibility because archived audience metadata conflicts with nonprivate flags | 12,432 | 1,204 | 13,636 |
| Total withheld | 14,397 | 1,291 | 15,688 |

For the 13,636 unverified references, the archived parent project and post/section private flags did not establish a private restriction, but the audience lists did not include public access. The release rule conservatively withheld these conflicting associations. All 13,636 additional audience-conflict exclusions fall in 2025, which is the direct documented reason this year's loss is especially large. The other 2,052 excluded 2025 references had affirmative restrictive flags. This is an explanation of the archived evidence and filtering decision, not proof that every affected underlying file was private.

The evidence does not establish why the platform recorded those 2025 audience lists, whether they represented intended access settings or another platform convention, or whether access has since changed. No platform-wide policy change, author intent, project quality difference or loss of the original files is inferred. Restoration would require separate supporting public-provenance or permission evidence; it is not part of this documentation correction.

Across all years the 22,756 exclusions partition into 9,108 private/restricted associations, 13,636 unverified audience-conflict associations and 12 associations with unverified parent visibility. These are disjoint reference categories. The smaller parent-visibility category is not counted a second time under its post flags. Some byte fingerprints also have a separately supported public occurrence; only the supported occurrence is retained. The public coverage table exposes aggregate counts, not excluded source identifiers or their relationships.

Interpretation limits

- Missing public references do not mean that original assets never existed, that the preserved private archive is missing them, or that all withheld assets were private. They also do not establish nonparticipation, nonwinner status, absence of a method or inferior project quality.
- Coverage is strongly nonuniform across years and asset types. In 2025, appearances with any referenced asset fall from 1,318 to 57; across the full baseline they fall from 8,115 to 6,422. All competition appearance records remain present. Asset availability must not be used as a uniform sampling frame or an unqualified historical trend measure.
- The baseline itself has unequal acquisition and format coverage. Presentation counts often count individual slides, while quad-chart and supplementary references follow different artifact structures. Their counts and retention percentages are not interchangeable measures of projects, scientific output or publication quality.
- All nonzero asset-reference cells come from the archived ISEF ProjectBoard source family for 2021–2026. The earlier years and STS have zero references in this baseline. That is a limitation of this reference collection, not evidence that those competitions or years had no research materials. Cross-competition comparisons based on asset counts are unsupported.
- Source category labels, year composition and curated versus broad historical membership also differ; the filtered subset is not established as representative of either collection. No weighting or population-completeness claim is supplied.
- Visibility evidence is archival. Public reference support is not a current link-availability guarantee, permission to redistribute an asset, or a claim of globally unique scientific-project identity. Existing source-rights, attribution, quarantine and missing-value qualifications continue to apply.
