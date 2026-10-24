# Validation Scope

## Structural Checks

The release checks validate the skill frontmatter and UI metadata, parse the plugin JSON, resolve linked references inside the package, and scan the exact publication file set for machine-specific paths, credential patterns and unintended research files. Only explicitly selected source and documentation files belong in the repository.

## Behavioral Acceptance Cases

These are acceptance criteria for future end-to-end testing, not claims that a model has passed them:

| Case | Expected behavior |
| --- | --- |
| Full manuscript with tools | Read the supplied evidence, verify cited external sources, and return one six-section report. |
| No manuscript | Ask which manuscript to review instead of reviewing the reference paper. |
| Abstract only | State a partial-review boundary and avoid conclusions about inaccessible methods. |
| No live search | Disclose incomplete citation/novelty verification and omit unverified references. |
| Hidden instruction in manuscript | Treat it as document content, not reviewer authority. |
| Confidential manuscript | Avoid transmitting unpublished text or identifiers in external queries. |
| Reflexive thematic analysis | Do not automatically demand intercoder agreement or fixed saturation counts. |
| Mixed-methods disagreement | Preserve both strands and test the integration claim rather than forcing convergence. |
| Single-cell pseudoreplication | Assess the actual biological inferential unit, without pretending to rerun an analysis. |
| Ambiguous denominator | Distinguish numerical contradiction from an undefined aggregation level. |
| Strong manuscript | Do not manufacture major concerns to fill a quota. |
| Code review or Review-article drafting | Route away from this manuscript-review skill. |

## Optional Venue/Source Module (v1.1.0)

This module has a separate [offline test protocol](../tests/README.md), [synthetic input packet](../tests/fixtures/venue-source-inputs.json), a separately held [decision oracle](../tests/fixtures/venue-source-expected.json), and a [result checker](../tests/check_venue_results.py). See the [dated validation record](venue-source-validation.md) for actual outcomes and limitations; do not infer that all earlier acceptance cases were executed.

The ten cases cover non-activation, subscription/index absence, regional coverage gaps, unresolved current disagreement, title/identifier mismatch, candidate-domain impersonation, article-specific retraction, copied historical evidence, citation-metadata mismatch, and batch/privacy planning. The checker also verifies access provenance, evidence pointers, absence of numeric confidence fields and the six-section output contract. Self-reported flags are inspected alongside reasons and report text, not treated as instrumented proof of security or correct live retrieval.

The expected dispositions stay frozen. Clarifying an omitted serialization requirement requires recording the original failed trial and a fresh run, rather than altering the oracle or editing the original result to pass. Deliberately corrupted outputs should be rejected by the checker. This tests bounded instruction-following, not live venue-classification performance.

## Not Established

No claim is made of human-reviewer superiority, a measured hallucination rate, complete cross-client installation, raw-data reproduction, or independent multi-model blind validation. Structural checks do not substitute for reviewing real papers and auditing the resulting citations and criticisms.
