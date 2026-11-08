# `projects.csv` schema

One row per project-at-a-competition. The same project can appear twice if it was recognized at two competitions (for example an ISEF row and an STS row); the `summary` cross-references the other row.

| Column | Required | Values |
|---|---|---|
| `id` | yes | `COMP-YEAR-tag-surname`, unique. Examples: `ISEF-2026-CBIO-1-vipuil`, `STS-2025-06-hong`, `ACSEF-2026-ISEF-pandit`. |
| `year` | yes | Competition year (4 digits). |
| `competition` | yes | One of: `ISEF`, `STS`, `CSEF`, `ACSEF`, `JSHS`, `Davidson Fellows`, `Thermo Fisher JIC`, `Google Science Fair`, `Siemens Competition`, `BioGENEius Challenge`, `Synopsys Championship`. |
| `level` | yes | `international`, `national`, `state`, `regional`. |
| `award` | yes | As written in the source, including money when given. |
| `category` | yes | Competition category as written in the source. |
| `students` | yes | `; `-separated for teams. |
| `school` | no | School as written. |
| `location` | no | City, State/Province, Country. |
| `title` | yes | Project title. See `title_status`. |
| `title_status` | yes | `verbatim` (exact), `abbreviated` (press release cut it; ends with `[...]`), `paraphrased` (no formal title in source). |
| `summary` | no | What the project did, in our words, from the source. |
| `methods` | no | Short list of methods. |
| `data_sources` | no | Datasets used. "(likely)" marks our inference. |
| `tags` | no | `;`-separated lowercase kebab-case topic tags. Free vocabulary; see the list below for the ones the topic pages key on. |
| `relevance` | yes | `;`-separated from: `cancer-lead`, `evo-leads`, `compbio`, `acsef-path`, `general`. |
| `lesson` | no | One sentence: what this project tells us about our own work. Rows with a lesson appear in the README short list. |
| `source_url` | yes | Primary source the row was taken from. |

## Relevance tags

- `cancer-lead`: informs PD1-CAN-01 (do 3D-specific cancer dependencies and biomarker links replicate across biobanks; cell line vs organoid fidelity; cancer genomics on public data).
- `evo-leads`: informs PD1-EVO-01/02 (urban heat and snail shell colour; urban intensity and pigeon plumage; citizen-science images; CV on organisms; spatial ecology; computational evolution).
- `compbio`: computational biology generally.
- `acsef-path`: Alameda County, Quarry Lane, Dublin and nearby precedents for the ACSEF to CSEF to ISEF ladder.
- `general`: context for what wins top awards outside comp bio.

## Topic tags the pages key on

`cv`, `histopathology`, `medical-imaging`, `imaging`, `protein-structure`, `protein-design`, `antibody-design`, `alphafold`, `embeddings`, `md`, `drug-discovery`, `drug-repurposing`, `drug-response`, `drug-synergy`, `drug-resistance`, `multi-omics`, `single-cell`, `spatial-omics`, `transcriptomics`, `genomics`, `methylation`, `epigenetics`, `3d-genome`, `strs`, `variants`, `cnv`, `driver-genes`, `mirna`, `rna`, `ribosome-profiling`, `epidemiology`, `forecasting`, `spatiotemporal`, `geospatial`, `remote-sensing`, `virology`, `evolution`, `population-genetics`, `phylogenetics`, `ecology`, `citizen-science`, `ebird`, `conservation`, `animal-sciences`, `animal-behavior`, `field-plus-compute`, `acoustics`, `snails`, `invasive-species`, `plant-pathology`, `plant-sciences`, `clinical-ml`, `wearables`, `eeg`, `neuroscience`, `neuroimaging`, `alzheimers`, `diagnostics`, `multi-year`, `public-data`, `team`, `hybrid-wet-dry`, `bay-area`, `alameda`, `dublin`, `quarry-lane`, `california`, `model-fidelity`, `cell-lines`, `organoids`, `pdx`.

`hybrid-wet-dry` marks projects that paired computation with an independent experimental test. `model-fidelity` marks projects asking whether one experimental model represents another.
