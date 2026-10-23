# Method-specific checks

Use only branches relevant to the actual manuscript and its claims. These are reviewer checks, not mandatory new analyses or a reporting-checklist score. A checklist item is not evidence of misconduct or an automatically fatal omission. Verify current reporting guidelines at their original source before calling them a requirement.

## Quantitative, clinical and observational research

- Align target population, sampling, comparator, timing, outcome and estimand. Distinguish descriptive, predictive and causal claims; evaluate identification assumptions and plausible rival explanations.
- Check experimental/inferential unit, repeated observations, clustering, paired designs, confounding, selection, missingness, attrition and multiplicity. Distinguish biological from technical replicates and planned from exploratory analyses.
- Interpret effect size and uncertainty, not only significance. Nonsignificance is not equivalence or absence of effect; statistical significance is not clinical importance. Do not infer a between-group difference from one significant and one nonsignificant within-group result.
- For mixed-effects models, assess grouping structure, within/between-person interpretation, random-effects justification, convergence and uncertainty when reported. Do not require a complex model without enough independent units or claim diagnostic checks passed without outputs.
- Match a proposed sensitivity analysis to a specific threat; avoid post hoc observed power as a substitute for effect-size uncertainty. State what existing data could and could not resolve.

## Qualitative research

- Establish the stated epistemology and analytic approach before evaluating it: reflexive thematic analysis, codebook analysis, coding-reliability analysis, grounded theory or another approach.
- Assess fit among question, sampling, recruitment, context, data generation, analytic steps, reflexivity, negative cases and interpretation. Trace claims to actual source spans or quotations where supplied.
- Do not impose intercoder agreement on reflexive thematic analysis, a universal saturation threshold, or theme frequency as a measure of significance. For grounded theory, assess the actually claimed theoretical sampling, constant comparison and theory-building process without forcing another tradition's conventions.
- Treat participant coverage, coded references and word frequency as different counting units. No access to raw transcripts means no claim of independently verified coding completeness.

## Mixed-methods research

- Identify why integration is needed, the design, sequencing, strand priority and integration points. Check whether qualitative and quantitative populations, constructs and timepoints are comparable.
- Assess linkage via appropriate ParticipantID/CaseID without exposing identities. Examine triangulation, complementarity, disagreement and joint displays where relevant.
- A positive qualitative account does not erase a null quantitative outcome. Assess whether the meta-inference respects both strands and alternative explanations. Do not require convergence or convert themes into numeric measures without justification.

## Bioinformatics and multi-omics

- Identify the biological question, assay, independent biological unit, sample provenance, QC, batches, covariates and reference versions. Distinguish cells, spots, reads and technical replicates from independent donors or organisms.
- Examine donor-aware inference, pseudoreplication, batch correction versus removal of biology, multiple testing, annotation uncertainty and missing modalities. Pathway enrichment depends on the tested background and method; network association does not establish a causal mechanism.
- For integration, check cross-modal sample alignment, feature selection and preprocessing leakage, fair baselines, held-out validation at the claimed generalization level and robustness to integration choices.
- In spatial/single-cell work, consider patient/site splits, spatial dependence, doublets, ambient contamination and composition versus state effects where relevant. Do not mandate every pipeline step irrespective of assay or hypothesis.
- Protein structure, docking, multi-epitope and prediction outputs support computational hypotheses within model limits, not experimental binding, immunogenicity, safety or clinical efficacy. Inspect uncertainty/confidence, template or training overlap, baselines and orthogonal validation only as required by the claim.

## Computational methods and benchmarks

- Trace implementation, data/version provenance, split independence, preprocessing, tuning budget, checkpoint selection, fair comparators, seeds, uncertainty and reproducibility. Distinguish a wrapper demo from an independent reproduction.
- Reconcile metrics with their definitions, denominators, bounds and micro/macro aggregation. A disagreement caused by an undefined aggregation level is an ambiguity until resolved, not a proven impossible result.
- For mathematical claims, inspect assumptions, definitions, scope, proof steps and counterexamples. Do not demand a benchmark or wet-lab experiment for a purely theoretical contribution unless necessary for an empirical claim.

## Review articles and evidence synthesis

- Distinguish narrative review, scoping review, systematic review and meta-analysis. Assess the transparency and completeness appropriate to the declared design rather than applying a systematic-review checklist to every narrative article.
- For systematic synthesis, assess search coverage/dates, selection, risk of bias, duplicate populations, heterogeneity and certainty. For narrative reviews, assess a distinctive defensible argument, critical synthesis and balanced treatment of contradictory evidence.

## Readiness calibration

Prefer a small number of grounded, high-impact concerns. A repair being laborious does not by itself make a flaw central; a repair being easy does not make a central validity flaw minor. Distinguish proven contradiction, plausible threat, reporting gap and inaccessible evidence. Suggest new experiments only when indispensable to the retained claim, with a narrower existing-evidence alternative where possible.
