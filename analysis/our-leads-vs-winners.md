# Our three leads against the winners

All three leads carry the disposition ADVANCE FOR LATER REVIEW under the SFPP-T instrument (V2.4). This page does not re-qualify them. It maps each to its closest catalogued precedents and lists what those precedents imply for design, category and risk. Row IDs refer to `data/projects.csv`.

## PD1-CAN-01: Do 3D-specific cancer dependencies replicate across the Broad and Sanger organoid biobanks?

**Design recap.** Compare 3D-vs-2D differential dependencies and biomarker-dependency links from the Broad 3D DepMap release (147 Cas12a screens, 10 cancer types; Neiswender et al., Nature, Aug 2026) with the Sanger organoid biobank screens (162 organoid cultures; Herranz-Ors et al., Nature, Aug 2026), within shared lineages, against a random-gene null; separate real 3D biology from CRISPR-library artifact using the 36 Broad 2D lines screened with the same Cas12a library. Unit = patient-derived model.

**Closest precedents.**

| Precedent | What they did | What it implies for us |
|---|---|---|
| Leo Shen, ISEF 2022 CBIO 4th (ISEF-2022-CBIO-4-shen) | PDX vs patient fidelity by DGE, GSEA, PCA on open RNA-seq | Same question shape, placed 4th because the analysis was descriptive. We need a prespecified replication statistic (sign concordance and effect-size threshold vs a null), not a list of enriched pathways. |
| Mythreya Dharani, STS 2026 finalist (STS-2026-F-dharani) | Trained on cell-line cisplatin response, predicted in patient tumors, interpretable | The cell-line-to-patient transfer problem is live at STS. Position ours as the complementary question: how much of what 2D screens say survives in 3D models. |
| Thomas Cong, STS 2024 2nd (STS-2024-02-cong) | Public cell-line multi-omics tested a field assumption | Frame the result as a test of a belief ("3D models reveal new dependencies"). If replication is low, that is a finding; if high, that is a finding. Prespecify both readings. |
| Jonathan Yan, STS 2026 finalist (STS-2026-F-yan) | 479-cell-line computational screen plus one knockdown | We cannot do a knockdown. Our second line of evidence is the second biobank and the library-controlled 2D comparison. Say so explicitly. |
| Virginia Ma, ISEF 2019 CBIO 2nd (ISEF-2019-CBIO-2-ma) | Benchmarked deconvolution methods on public data | Methods evaluation is a legitimate 2nd-place project. If the biology is thin, the replication framework itself is a contribution. |
| CANDraGAT, ISEF 2022 CBIO 1st (ISEF-2022-CBIO-1-candragat) | GNN on GDSC/CCLE cell-line pharmacogenomics | Our data family (DepMap/CCLE/Cell Model Passports) has produced a CBIO 1st. |
| Kevin Zhu, CBIO 1st 2022 and 2023 | One neglected variant class, pan-cancer, two years | Pick the narrow, defensible claim (named links such as ENO1/ENO2, KRAS/SCD) and plan the year-two extension (more lineages, a third biobank, drug-response links). |

**Risks the record flags.** Cancer is the most crowded CBIO subject and public-data cancer analyses without a validation layer land 3rd-4th. The 2026 CBIO firsts were a physics-informed imaging pipeline and a plant-pathogen evolution model. Our differentiators must be visible in the title: two independent 2026 biobanks, library control, replication statistic.

**Category.** ISEF CBIO, subcategory Genomics (GEN) or Other. At CSEF: Computational Systems: Medical or Computational Science. JSHS: Biomedical Sciences or Math and Computer Science.

**Feasibility flag from the dossier.** Sanger screen files were not confirmed downloadable at V2.4; that is the first documentary step, and Dharani's and Yan's abstracts show judges accept "published data from X" only when X is named.

## PD1-EVO-01: Does urban heat favor lighter snail shells outside the Netherlands and in introduced North American snails?

**Design recap.** ~164,600 GBIF image records of Cepaea; student-built, validated colour classifier; unit = site within city, cities as replicates; multi-country, two-continent test of Kerstes et al. 2019 (Communications Biology).

**Closest precedents.**

| Precedent | What they did | What it implies for us |
|---|---|---|
| Rithika Narayan, ISEF 2020 finalist (ISEF-2020-F-narayan) | Hand-labeled hundreds of crowd-sourced coral photos, fine-tuned Mask R-CNN, >85% | Our labeling budget (2,000-3,000 images) is in range. Report a held-out confusion matrix and photographer/lighting robustness; then spend most of the poster on the biology, not the model. |
| Ashwin Sivakumar, ISEF 2019 EAEV 4th (ISEF-2019-EAEV-4-sivakumar) | 146,457 eBird records vs Landsat/Sentinel/PRISM in Earth Engine, one site | Citizen-science occurrences crossed with public environmental layers is an accepted design. One site placed 4th; our many-cities replication is the step up. Use the same public heat layers (Landsat LST, ERA5, local UHI products). |
| Lillian Petersen, STS 2020 1st (STS-2020-01-petersen) | Fit in the US, tested in Africa | Fit the shell-colour vs urban-heat relationship in the Netherlands (where it is known), then test out of sample in other European countries and in introduced North American populations. State the prediction before testing. |
| Jessica Young, ISEF 2017 ANIM Best of Category (ISEF-2017-ANIM-1-young) | Invasive snail control | Snails win Animal Sciences when there is an applied angle. Introduced North American Cepaea gives us one. |
| Isabella Bowland, ISEF 2017 PLNT 1st (ISEF-2017-PLNT-1-bowland) | Alpine gradient, plant-fungus symbiosis | Environmental-gradient designs win. Urban heat is a gradient; treat each city as a gradient from core to edge. |
| Mohammed Alasmari, ISEF 2026 CBIO 1st (ISEF-2026-CBIO-1-alasmari) | Host-pathogen evolution model | CBIO EVO produced a 2026 first. The evolutionary framing (selection on thermal melanism) is where the category credit is. |

**Risks the record flags.** Photographer and lighting bias in colour scoring (no winner has solved this with citizen photos; Narayan sidestepped it with coarse classes). Classifier-only projects do not place. Needs no approvals, which the dossier noted as its advantage.

**Category.** ISEF CBIO, subcategory Computational Evolutionary Biology (EVO), which names ecology explicitly; or Animal Sciences (Ecology) if we add a Bay Area field transect. Confirm ACSEF category mapping before Nov 30.

## PD1-EVO-02: Across the world's cities, do pigeons get lighter with climate heat but darker with urban intensity?

**Design recap.** ~383,400 GBIF image records of Columba livia in 25+ countries; unit = city; built-in contest between two hypotheses (thermal selection vs urbanization-linked melanism); noisiest biology (escaped fancy pigeons, vertebrate-rule check).

**Closest precedents.**

| Precedent | What they did | What it implies for us |
|---|---|---|
| Benjy Firester, STS 2018 1st (STS-2018-01-firester) | Spatiotemporal model from public weather and disease data | A computational-ecology model with cities/regions as units can win the top prize when it predicts something checkable. |
| Noah Nager, ISEF 2023 CBIO 4th (ISEF-2023-CBIO-4-nager) | Public land-cover layers vs West Nile virus across US regions | The EPD/EVO "regions as units, public layers as predictors" shape. Placed 4th: correlational designs need the two-hypothesis contest to stand out. Ours has it. |
| Addison Shea, STS 2025 finalist (STS-2025-F-shea) | Spatial statistics on 30 years of biased, observational sightings | Judges accept observational records if sampling bias is modeled, not ignored. Budget a bias analysis (observer density, platform effects). |
| Anika Puri, ISEF 2022 EAEV 1st and Scripps (ISEF-2022-TOP-scripps) | Spatiotemporal ML on wildlife video | Conservation plus CV plus spatiotemporal modeling earns top special awards; communication quality (Scripps) matters. |
| Kevin Xuan Lei, ISEF 2024 BMED 1st (ISEF-2024-BMED-1-lei) | Evolutionary lens on a biology question | Evolutionary framing is a category-level differentiator. |
| Dylan Bagnall and Richard Beattie, ISEF 2019 ANIM 1st (ISEF-2019-ANIM-1-bagnall-beattie) | Methods for citizen scientists | A reusable, validated pipeline for scoring plumage from citizen photos is itself a methods contribution if we release it. |

**Risks the record flags.** No high-school winner has worked on urban pigeon colouration; the niche is open but the biology is noisy and vertebrate rules apply even to photo-only work (confirm with the SRC). The dossier's two-species option (snails and pigeons on one pipeline) matches the multi-year pattern in `topics/multi-year-projects.md`: species one in 2027, species two in 2028.

**Category.** ISEF CBIO (EVO) or Animal Sciences (Ecology). Judges in Animal Sciences will press on pigeon biology, genetics and escaped domestics; judges in CBIO will press on model accuracy, validation and statistics.

## Cross-cutting implications

1. Put the result in the title; put the pipeline in the methods. (what-wins #1)
2. Name the second line of evidence in the abstract: second biobank, out-of-sample countries, library control. (what-wins #2)
3. Prespecify the statistic and the two readings of the outcome before the data are downloaded; the SFPP-T stage cards already require this. (what-wins #7)
4. Write the year-two extension into the research plan now. (what-wins #4)
5. Read every CBIO abstract 2021-2026 that touches our keywords and cite the gap. (what-wins #12)
6. Enter JSHS and plan Davidson; STS is the Class of 2029's autumn 2028 problem. (what-wins #11)
