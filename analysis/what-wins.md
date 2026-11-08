# What wins

Patterns across the 500 catalogued entries (ISEF 2014-2026, STS 2013-2026, ACSEF, CSEF, JSHS, Davidson, JIC and others). Each claim below points at rows in `data/projects.csv`; the IDs are in parentheses.

## 1. A biological question, answered, beats a model, built

The clearest split in twelve years of CBIO results. Projects whose title is a method ("A Novel Deep Learning Pipeline for X") cluster in 3rd and 4th. Projects whose title is a claim or a question cluster at 1st and 2nd and in the top awards.

- "Immune-related cancers show pronounced differences in metabolism and gene expression" beat the field's assumption: STS 2024 2nd, $175,000 (STS-2024-02-cong).
- "Micro-Changing Short Tandem Repeats: a novel genomic factor of polymorphism in 10 human cancers": CBIO 1st twice (ISEF-2022-CBIO-1-zhu, ISEF-2023-TOP-siyss-zhu).
- "A Markov Chain Model for Predicting ETI Resistance Breakdown in Tomato–Pseudomonas syringae": CBIO 1st 2026 (ISEF-2026-CBIO-1-alasmari).
- "Algae's Photoinhibition Sheds Light on Why Land Plants Evolved To Be Green, Not Black": Plant Sciences 1st 2014 (ISEF-2014-PS-1-wan).
- Counter-examples: five well-built public-data pipelines with no biological claim in the title (ISEF-2021-F-anisetti, ISEF-2026-CBIO-4-dixit, ISEF-2021-CBIO-4-holzer, ISEF-2023-CBIO-3-rahman, ISEF-2024-F-mcgill year 1) placed 4th or not at all.

For us: the title should state the replication result, not the pipeline. "3D-specific cancer dependencies replicate across two independent organoid biobanks (or do not)" is a claim. "A multi-omic framework for organoid dependency analysis" is a pipeline.

## 2. Two independent lines of evidence

The top-3 STS and top-award ISEF projects in comp bio almost always pair the computational result with something independent: a wet-lab test, a second dataset, a field trial, or an out-of-sample region.

- Public retinal images plus a second cell model: STS 2026 2nd (STS-2026-02-kang).
- 479 cell lines plus a knockdown that stopped spreading: STS 2026 finalist (STS-2026-F-yan).
- Public patient genetics plus AlphaFold plus CRISPR plus docking: ISEF BCHM 1st, STS finalist, Davidson $50k (ISEF-2024-BCHM-1-xiao).
- Public cell data plus two approved drugs tested in a dish: STS 2026 8th (STS-2026-08-wang).
- Satellite indices fit on US yields, tested on African yields: STS 2020 1st (STS-2020-01-petersen).
- Bioinformatic gene identification plus consortia engineering: ISEF Moore Award 2016 (ISEF-2016-TOP-moore).

For a dry-lab team the second line of evidence is the second dataset. The cancer lead has it built in (Broad and Sanger). The snail and pigeon leads have it in the geography (fit in one country, test in others).

## 3. Public data wins when the method finds something new in it

Public data is the norm in CBIO and no barrier at the top: Kaitlyn Wang found the smallest known ultra-short-period planet in public Kepler data and won the $75,000 Yancopoulos Award (ISEF-2023-TOP-yancopoulos); Andrew Jin found 100+ adaptive mutations in public genomes and won $150,000 (STS-2015-GG1-jin); Melody Hong's Bayesian trans-mQTL model placed 6th at STS (STS-2025-06-hong); Franklin Wang's deep learning on public survey images discovered new asteroids (ISEF-2021-TOP-scripps). What these share: a named discovery or a quantified result that did not exist before, and a validation step a judge can inspect.

## 4. Year two wins

The strongest single predictor of a top placement in this catalog is having competed with the same program the year before.

- Kevin Zhu: CBIO 1st 2022, CBIO 1st and SIYSS 2023.
- Swetha Revanur: CBIO 1st 2015 and 2016.
- William Wakefield: CBIO 3rd 2024, 2nd 2025.
- Joshua Wu (Dublin HS): BMED 2nd 2025, 3rd 2026, from ACSEF both years.
- Vrishank Chandrasekhar (Lynbrook): CSEF 2nd 2024, ISEF TMED 1st plus SIYSS 2025.
- Yookta Pandit (Quarry Lane): CSEF 2nd and JIC finalist 2025 (8th grade), ISEF CBIO 3rd 2026 (9th grade).
- Estrada siblings (Clovis North): Moore Award 2021, PLNT 1st 2022, PLNT 1st 2024, one imaging pipeline on new plants each year.
- Varun Madan: ANIM 1st 2021 (Year 4) and 2022 (Year 5). Titles literally start with "Year 4:" and "Year 5:".
- Finnegan McGill: ISEF 2024 no award, Davidson 2025, STS 2026 top 40.
- Lillian Petersen: ISEF EAEV 1st 2018, STS 1st 2020.

For us: the 2027 ACSEF entry is year one. Design it so that a year-two extension is obvious (second organism, second biobank, second continent) and say so in the "future work" section.

## 5. Teams are not penalized; they are judged twice

CBIO 1st went to teams in 2015 (Retchin twins), 2021 (EGFRNet), 2022 (CANDraGAT) and 2025 (Sharma, Das, Dunakhe), and a team took CBIO 2nd in 2026 (Song and Sharma). Top awards went to teams in 2022 (Moore, BiDEx), 2023 (RYSA, lacewing team), 2024 (Moore, Huang and Ou) and 2025 (Moore, NeuroFlex). Four of ACSEF's seven 2026 ISEF projects were teams; Dublin High's 2025 CBIO 2nd was a two-person team. The judging criteria say each member is assessed on contribution and understanding, so both of us must be able to defend every figure.

## 6. Field-plus-compute beats compute-only in the biology categories

In Animal Sciences, Plant Sciences and Earth and Environmental Sciences, the computational winners all generated or collected their own data and used computation as the instrument: Manaswi's multi-CNN histology plus field trials (ANIM 1st and Scripps 2026), Lo's bee training with AI analysis (ANIM 1st 2025), Estrada's imaging rigs, Orth's hive acoustics (STS 9th 2022), McQuilkin's glacier survey plus 3D model (EAEV 1st 2021), Springer's spatial disease-rate comparison (ANIM 1st and Scripps 2024). A GBIF-image project does not collect its own data, which is why it belongs in CBIO EVO rather than Animal Sciences unless we add a field component (a Bay Area transect of our own snail or pigeon photos would be a cheap second line of evidence).

## 7. Simple statistics, done right, are enough

Several top placements used regression or Bayesian models and no deep learning: Madan's multiple linear regression (ANIM 1st twice), Hong's Bayesian mQTL mapping (STS 6th), Luo's wavelet-based cutoff (STS 3rd), Petersen's index regression (STS 1st), Lipkovitz's panel model (STS 5th), Orth's acoustic model (STS 9th). Judges reward the match between method and question and the care in validation. Reserve deep learning for where it is needed (the image classifier) and use prespecified statistics for the inference.

## 8. Reframing a known problem with a method from another field counts as creativity

Noah Getz reframed virtual screening as information retrieval: STS 2021 2nd, $175,000 (STS-2021-02-getz). Hikaru Kuribayashi sampled origami configuration spaces with MCMC: ISEF 2026 top award. Caroline Huang used chaos theory on tumor vasculature: CBIO 3rd. Creativity and Potential Impact is 20 of 100 points at ISEF; this is the cheapest way to earn it.

## 9. Category choice is strategic

Computational projects have won in Biochemistry (Punjabi 2015), Biomedical Engineering (Jain's RNN codon optimizer, RYSA 2022), Translational Medical Science (BiDEx CNN, Moore 2022; Chandrasekhar's OncoNote, TMED 1st 2025), Robotics (Hua's CNN, top award 2021), Earth and Environmental Sciences (Sivakumar's eBird work, Puri's poacher detection), Plant Sciences (Estrada). CBIO is the most crowded computational category (92 projects in 2026). ACSEF and CSEF categories do not map one-to-one onto ISEF's; confirm with the SRC before Feb 1.

## 10. Cancer is crowded; the subject is not the edge

Kaiser's analysis of 13,543 ISEF projects (2014-2023) found projects mentioning cancer or tumors won 10-20% fewer awards in recent years, while projects mentioning AI or ML won more (an advantage that shrank over time), and titles with a colon-separated two-part structure won about 33% more awards in 2023 ([source](https://wkaisertexas.github.io/blog/international-science-and-engineering-fair-analysis)). Those are correlations, but they match what the catalog shows: in CBIO 2026 the two firsts were not cancer projects, and the ten cancer projects spread across 2nd to 4th.

## 11. Non-placement is not a verdict

McGill's A-BiRD placed nowhere at ISEF 2024, then earned a Davidson Fellowship and an STS finalist spot. The Beesam twins placed 4th in CBIO and won the Siemens team grand prize the same year. Matteo Paz won STS and got a Davidson honorable mention. Enter several competitions with the same work (ACSEF, CSEF, ISEF, JSHS in spring; Davidson in February of the following year; STS senior year).

## 12. The abstract database is the real competitor list

Every ISEF finalist abstract since 2014 is searchable. Before we commit to a title, we should read every CBIO abstract 2021-2026 that mentions DepMap, CCLE, organoid, GBIF, iNaturalist, urban, melanism or colour, and state in our research plan what is new relative to each. See `resources/abstract-database-howto.md`.
