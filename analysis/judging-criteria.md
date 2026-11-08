# Judging criteria and how winners score on them

## ISEF Grand Award rubric (science projects)

Source: [Society for Science, Grand Award Judging Criteria](https://www.societyforscience.org/isef/grand-award/criteria/). 100 points.

| Criterion | Points | What judges look for | What the winners in this catalog did |
|---|---|---|---|
| Research Question | 10 | Clear, focused purpose; identifies its contribution to the field; testable | Titles that are claims or questions (Zhu, Alasmari, Cong). A one-sentence gap statement relative to named prior work. |
| Design and Methodology | 15 | Well-designed plan and data-collection methods; appropriate, complete variables and controls | Prespecified statistics; a control for the obvious artifact (our Cas12a-library control; Shea's observer-bias model; Petersen's out-of-sample test). |
| Execution: Data Collection, Analysis and Interpretation | 20 | Systematic collection and analysis; reproducibility; appropriate math and statistics; enough data to support conclusions | Multiple testing correction over 18,000 genes; held-out test sets for classifiers; effect sizes with uncertainty, not just p-values; code released (Zou, Kiker released open-source software). |
| Creativity and Potential Impact | 20 | Significant creativity in question, design or analysis; actual or potential impact on the field, technology, economy, environment or society | Cross-field method transfer (Getz, Kuribayashi); a neglected signal (Zhu's STRs); a resource others can use (Paz's catalog, Hong's method). |
| Presentation: Poster | 10 | Logical organization; clear graphics and legends; supporting documentation displayed | Colon-structured titles; one main figure that carries the result; the rubric's own words ("reproducible", "controls") visible on the board. |
| Presentation: Interview | 25 | Clear, concise, thoughtful answers; understanding of the basic science; understanding of limitations; independence; recognition of impact; ideas for further research; for teams, each member's contribution and understanding | The interview is a quarter of the score. Both team members must be able to defend every figure, name the limitations unprompted, and describe year two. |

Engineering projects use a parallel rubric (Research Problem 10, Design and Methodology 15, Execution: Construction and Testing 20, Creativity 20, Presentation 35). Teams and individuals are judged together on quality alone.

## Where comp-bio projects lose points

- **Execution (20).** A classifier accuracy with no confusion matrix, no held-out set and no error analysis. No multiple-testing correction. No effect sizes. Reproducibility unaddressed (no code, no seeds, no data versions).
- **Design (15).** No control for the obvious confound: library (Cas9 vs Cas12a), lineage mix, culture medium for us; photographer, lighting, observer density for the image leads.
- **Research Question (10).** A method-shaped title with no stated gap. See `title-and-abstract-anatomy.md`.
- **Interview (25).** One team member who did the coding and one who cannot explain it. The rubric names this explicitly.

## STS

STS judges a written research report (reviewed like a paper) plus, for finalists, interviews that probe general scientific knowledge and reasoning across fields, not just the project. It weights statistical depth, independence and the quality of the written report more than ISEF's poster interview does. Evidence: Amber Luo's RiboBayes was 3rd in ISEF CBIO and 3rd overall at STS ($150,000); Melody Hong's Bayesian mQTL mapping, with no deep learning and no wet lab, placed 6th.

## ACSEF

ACSEF publishes category and special-award results but not a rubric in the documents we fetched; it follows ISEF categories and SRC rules. Projects using only publicly available datasets are "Regular" (no early approval). The 2027 timeline is in `competitions/acsef.md`. Confirm category mapping for a CBIO EVO project with the ACSEF SRC before the Nov 30 interest form.

## AI and authorship rules (2026-27)

From the ISEF rules as summarized in our prior planning: AI tools may be used and must be cited as a resource, but may not write the research plan, abstract or poster, or generate citations. Form 2A (Student Support Disclosure) is required for every project and must disclose any AI-assisted preparation, including the dossier that produced our leads. Check the live [Rules for All Projects](https://www.societyforscience.org/isef/international-rules/rules-for-all-projects/) before submitting.
