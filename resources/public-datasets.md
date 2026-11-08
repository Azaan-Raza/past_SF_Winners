# Public datasets the winners used (and the ones our leads need)

| Dataset | What it is | Used by (catalog IDs) | Notes for us |
|---|---|---|---|
| **DepMap portal** (depmap.org/portal) | Broad Cancer Dependency Map: CRISPR gene-effect scores, expression, mutations, drug sensitivity for 1,000+ 2D lines and, since Aug 2026, ~150 3D organoid/spheroid models (Cas12a screens) | Yan (STS-2026-F-yan, 479 cell lines, scale), CANDraGAT (cell-line drug response) | Primary source for PD1-CAN-01. Download the 3D release files and the 36 Cas12a-screened 2D lines; record release version and file hashes. |
| **Cell Model Passports / Sanger** (cellmodelpassports.sanger.ac.uk) | Sanger cancer model annotations and screens, including the 2026 organoid biobank (162 organoid cultures screened) | none in catalog yet | Second biobank for PD1-CAN-01. Availability of screen-level files was unconfirmed at V2.4; this is documentary step one. |
| **GDSC** (cancerrxgene.org) | Sanger drug sensitivity in cancer cell lines | CANDraGAT (ISEF-2022-CBIO-1-candragat, likely), Dharani (STS-2026-F-dharani, likely) | Links dependencies to drug response if we extend to pharmacology. |
| **CCLE** | Broad cell-line omics (expression, mutations, metabolomics) | Cong (STS-2024-02-cong, likely), Yan | Now folded into DepMap releases. |
| **TCGA / GDC** (portal.gdc.cancer.gov) | Patient tumor genomics, expression, methylation, clinical | Mandera (ISEF-2020-F-mandera), Xu (ISEF-2020-F-xu), Anisetti (ISEF-2021-F-anisetti), Gammell (STS-2025-F-gammell), Zhu (likely), Sahota (likely), Revanur (likely) | The patient-side anchor if we ask whether organoid-specific dependencies track patient subtypes. |
| **GEO** (ncbi.nlm.nih.gov/geo) | Expression datasets | Anisetti, DeMeo (ISEF-2021-CBIO-4-demeo), Lakkis (ISEF-2021-CBIO-3-lakkis) | |
| **ENCODE / Hi-C** | Chromatin features, 3D genome | Naidu (ISEF-2017-TOP-siyss-naidu), Chiang (ISEF-2018-CBIO-3-chiang) | |
| **LINCS / CMap** | Perturbation expression signatures | Roh (ISEF-2024-CBIO-1-roh, likely), Jain and Abul-Hassan (ISEF-2021-CBIO-4-jain-abulhassan, likely) | |
| **PDB / AlphaFold DB** | Protein structures and predictions | Xu (STS-2026-05-xu), Liang (STS-2026-F-liang), Xiao (STS-2025-F-xiao), Venkatraman (ISEF-2022-CBIO-4-venkatraman) | |
| **GBIF** (gbif.org) | Occurrence records with images aggregated from iNaturalist and others | none in catalog yet | ~164,600 Cepaea and ~383,400 Columba livia image records for PD1-EVO-01/02. Use the GBIF API with a DOI-citable download; keep the download DOI. |
| **iNaturalist** (inaturalist.org) | Research-grade photo observations | Narayan (crowd-sourced images incl. citizen science, ISEF-2020-F-narayan) | Source of most GBIF images; export licenses vary (CC BY, CC BY-NC); check per image. |
| **eBird** (ebird.org) | Bird observations | Sivakumar (ISEF-2019-EAEV-4-sivakumar, 146,457 records) | Observer-effort covariates if we model pigeon sampling bias. |
| **Landsat-8 / Sentinel-2 via Google Earth Engine** | Land surface temperature, vegetation, impervious surface | Sivakumar (1.7 TB processed in GEE), Petersen (satellite yield indices) | Urban heat (LST) and urban intensity (impervious surface, NDVI, night lights) layers for both EVO leads, computed per city. |
| **PRISM / ERA5** | Climate | Sivakumar (PRISM) | Background climate heat vs urban heat-island excess. |
| **BirdNET (Cornell)** | Open-source bird sound classifier | McGill (STS-2026-F-mcgill) | Example of building on an open model and citing it. |
| **Kaggle: All International Science Fair Projects** (kaggle.com/datasets/wkaisertexas/all-international-science-fair-projects) | ~13,543 ISEF abstracts 2014-2023 scraped from the Society database | Kaiser's analysis (see links.md) | Load it to find every CBIO abstract mentioning our keywords in one pass. |

Rules of thumb from the record: name the dataset and its size in the abstract; record versions and download dates; where a dataset is biased (citizen photos, sightings), model the bias rather than mention it.
