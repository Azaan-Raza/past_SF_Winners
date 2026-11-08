# Title and abstract anatomy

What the winning titles and abstracts in `data/projects.csv` have in common, with examples. Use this when drafting ours. (Rule: the abstract is written by us, not by an AI tool; see ISEF rules.)

## Titles

**Shape A: Name: Claim.** A short memorable name, a colon, then the scientific content. Kaiser's analysis of 13,543 ISEF projects found colon-structured titles won about 33% more awards in 2023.

- "RiboBayes: Assessing the Transcriptome-Wide Expression of Ribosome Pause Sites in Ribosome Profiling Data With Bayesian ..." (STS 3rd)
- "DNALoopR: A Novel High-Performance Machine Learning Predictor to Identify Genome-Wide 3D DNA Interactions in Cancer" (CBIO Best of Category, STS 7th)
- "CANDraGAT: A Hybrid Fragment-Based Graph Attention Network To Improve Cancer Drug Response Prediction" (CBIO 1st)
- "ElSa: A Novel Real-Time Wildlife Poacher Detection Solution Leveraging Machine Learning-Driven Spatio-Temporal Analysis ..." (EAEV 1st, Scripps)

**Shape B: The claim itself.** No name, just the finding or the precise question.

- "Micro-Changing Short Tandem Repeats: Investigating a Novel Genomic Factor of Polymorphism in 10 Human Cancers" (CBIO 1st)
- "Biophysical and Genomic Drivers of Targeted Therapy Resistance: Analysis of Growth Dynamics in Non-Small Cell Lung Cancer" (CBIO 2nd)
- "Evolutionary Insights Into the Stemness Paradox of Human Germ Cells and Cancer Cells" (BMED 1st)
- "Snail shell colour evolution in urban heat islands detected via citizen science" (the Kerstes et al. 2019 paper our snail lead extends; not a student project, but the shape to aim for)

**Shape C: Year N.** Multi-year programs say so in the title: "Year 5: Developing a Novel Multiple Linear Regression Model To Optimize Honey Bee Gut Immunity ..." (ANIM 1st), "Advancing Early Detection of Kidney Cancer (Year 3): ..." (TMED 1st), "Experimental Characterization of Inhibitors of the MSUT-2 Protein ... (Year 2)" (CBIO 2nd).

**What loses.** Titles that are only a method ("A Deep Learning Approach to X", "A Novel Pipeline for Y") cluster in 3rd-4th. "Novel" appears in a large share of titles and, per Kaiser, correlated with 20-70% more awards, but it is now so common in CBIO that it carries no information; the specific noun after it does.

**Drafts for us (to be rewritten by us, not adopted verbatim):**

- Cancer: "Do 3D-Specific Cancer Dependencies Replicate? A Library-Controlled Comparison of Two Patient-Derived Organoid Biobanks"
- Snails: "City Snails Across Two Continents: Testing Urban-Heat Selection on Cepaea Shell Colour With a Validated Citizen-Science Image Classifier"
- Pigeons: "Heat or City? Separating Thermal and Urbanization Effects on Pigeon Plumage Melanism Across 25 Countries"

## Abstracts

ISEF abstracts are 250 words. The winning ones in the abstract database follow one order:

1. **Gap in one or two sentences, with the prior finding named.** Mandera (ISEF 2020) explicitly stated prior accuracy (67%) before giving his (74.1%). Shen (2022) named the known inconsistency (consensus molecular subtype) that motivated the PDX question. Kerstes et al. is our named prior finding for snails.
2. **Question as a testable statement.** Not "to explore" but "we tested whether".
3. **Data, with sizes.** "146,457 eBird observations", "1.7 TB of Landsat-8 and Sentinel-2", "479 human cancer cell lines", "21,131 birdsong events from 98 species". Numbers signal execution.
4. **Method, one sentence per step, with the control.** Sivakumar: derive indices, correlate in R, supervised classification. Shen: negative-binomial DGE, GSEA on Hallmark sets, PCA. Say what the null is.
5. **Result with a number and a direction.** "76% accuracy across 12 tumor classes, 15% above the no-embedding baseline" (Xu 2020). "Dabbling ducks showed no correlation" (Sivakumar: a negative result stated plainly).
6. **Interpretation plus one limitation plus the next step.** Sivakumar: species behavior within a category changes response; method is reusable because the tools are free.

Things the strong abstracts avoid: adjectives about the work ("innovative", "groundbreaking"), methods lists without a question, results without numbers, and claims about clinical impact beyond what was shown.

## Poster

The 10-point poster criterion rewards organization and legends. The pattern among top projects: one headline figure that shows the result (a replication scatter with the null band; a map of cities colored by effect size), the rubric vocabulary visible ("control", "held-out", "replicates", "limitations"), and a short "what is new relative to [named prior work]" box.
