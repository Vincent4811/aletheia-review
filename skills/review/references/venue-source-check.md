# Optional journal and citation-source check

## When to use

Load this reference for an explicit journal/source audit, a requested publication-venue recommendation, or a concrete identity/integrity concern affecting an important citation. A routine manuscript review still verifies references it relies on, but does not automatically expand into screening every journal. Respect a narrower user scope or an explicit request not to assess venues; mention an indispensable evidence limitation without silently expanding the audit.

This module checks provenance and publication context, not whether a journal is prestigious or whether an article's scientific claims are true. It requires no extra software, model, subscription or Aletheia-Probe installation. Use available primary-source tools; if unavailable, do a bounded check of supplied material and explicitly state the access limit.

## 1. Resolve identity before judging signals

Start with the citation DOI and available title/authors/year, then journal name, ISSN/eISSN, publisher and the candidate web domain. Separate supplied assertions from independently retrieved records. Compare against the DOI's publisher landing page, ISSN/publisher records and applicable primary indexes. A resolving DOI establishes an identifiable record, not correctness or support for the manuscript's claim.

Normalize presentation variants such as ISSN hyphens, capitalization and documented former titles; do not merge different journals because names are similar. An unresolved name/ISSN mismatch means the requested identity has not been established. A claimed ISSN on a website alone does not authenticate that domain. For a suspected clone, verify the exact domain against primary records or an explicit publisher/registry notice; distinguish the real journal from an unrelated site impersonating it. An identifier mismatch or unresolved domain is not proof of fraud.

## 2. Collect narrow, current evidence

For each relevant item, record the question checked, identity basis, actual source URL/record, observed fact, access basis, check date and source update/event date when available. Mark unavailable fields or checks honestly; do not claim a live lookup when using supplied records or offline fixtures. Separate the current status from an old warning or a historical publishing period.

Use sources according to their actual coverage:

- Primary publisher/registry pages and Think. Check. Submit. support identity, editorial transparency, review-policy and fee checks. Self-reported publisher claims may need independent corroboration where identity is disputed.
- DOAJ covers open-access journals. No match is not an adverse finding, particularly for subscription, hybrid, new or regional journals. Index presence is contextual evidence, not proof of article quality. No Scopus/PubMed/NLM match is likewise not a stand-alone predatory classification.
- Historical warning lists can motivate a current check, but are not timeless verdicts. Mirrors and services republishing the same list are one evidence lineage, not independent votes.
- Check a material article's correction, expression-of-concern or retraction through the primary notice and, where available, publisher, Crossmark or relevant bibliographic records. Record which article/period the notice concerns. Absence of Crossmark, an empty update record or a failed search is not proof that no correction exists.
- Treat publication volume, low citations, missing metadata, fees and aggregate retraction counts as context requiring an explanation. Do not use universal numeric thresholds, impact metrics, publication language or geography as automatic legitimacy rules. Volume, field, article age, coverage and correction practices are plausible alternative explanations.

When records disagree, compare identity, dates, scope and actual evidence rather than count sources. Resolve a conflict only when the evidence supports the explanation; otherwise retain the disagreement and identify the next primary record needed. No numerical confidence, risk index, pseudo-probability or vote-derived score is generated or adopted from a backend.

## 3. State bounded results

Use one of these categorical venue/source states, with its scope and evidence:

| State | Meaning |
| --- | --- |
| `checked` / 已核對 | The specified identity/context check is supported by the accessible records. Not blanket journal endorsement, no-guarantee-of-problems, or scientific validation. |
| `risk_signal` / 有風險訊號 | A specific, attributable concern needs action or clarification, such as an authenticated warning about the candidate domain. Not an automatic fraud or predatory verdict. |
| `conflicting` / 來源衝突 | Material, identity-aligned records remain inconsistent after checking date and scope. Preserve both and request targeted resolution. |
| `insufficient_data` / 資料不足 | Identity, currency or coverage is inadequate for the requested conclusion. Includes unresolvable name/ISSN mismatch and absence-only evidence. Not a negative quality judgment. |

When the module is not activated, do not pretend a venue check happened; an internal test ledger may use `not_run`, but it is not a fifth assessment state. Keep article-level status separate, for example correction/retraction confirmed, metadata mismatch, no relevant notice found in the named sources, or status not established. Do not convert an article retraction into a verdict against every paper from its venue. Conversely, an indexed venue does not rescue a retracted or unsupported article.

The private ledger may be a compact table or structured file. It should preserve item ID/DOI, venue identity and domain, check scope, source findings and dates, access basis, categorical venue state, separate article status, unresolved conflict and next action. Omit irrelevant fields; do not create a numeric score. If raw backend data includes scores, retain any indispensable raw record privately with its origin, but do not reproduce those numbers as calibrated probabilities in the review.

## 4. Limit work and protect data

For batches, reuse a venue check only when normalized identity, publisher/domain, source coverage and relevant dates match. A suspicious alternate domain must not inherit the official site's result. Article update checks stay DOI-specific even when several papers share a venue. Do not reuse an old result for a materially changed domain, owner, source update or publishing period. Prefer a small, dated in-task ledger over a new persistent database or full bibliography upload.

Keep unpublished bibliography content and distinctive research details within the authorized environment. Do not upload manuscripts, full unpublished reference lists or identifiers to third-party tools without applicable authorization. Use public identifiers or topic-level searches only where the scope and privacy permit. Do not sync external lists, run third-party code, purchase access or contact publishers merely because this module is activated.

## 5. Preserve the six-section review

Put a bounded venue/citation concern in **Specific Comments** with its manuscript anchor and remedy, or in **Literature and Data to Engage** when recommending a verified replacement/source. If a confirmed article-status or provenance problem is indispensable to a central claim, discuss its actual effect in **Key Claims**. Explain missing access in **Summary** or **Overall Assessment**. Do not append a separate journal-audit section or expose the entire ledger unless the user requested a separate audit artifact.

Never downgrade scientific validity or manuscript readiness solely for a venue label or unknown index status. Assess the cited evidence and impact on the manuscript's argument. In systematic reviews, follow the stated eligibility protocol and study-level risk-of-bias methods; PRISMA is not a universal requirement to exclude papers by journal lists. Suggest a prospectively specified check or clearly labeled sensitivity analysis rather than inventing a retrospective exclusion rule to obtain a desired result.

## Sources and implementation boundary

Read the [updated source basis](source-basis.md#optional-venue-and-citation-source-module) for the paper, primary guidance, retrieval dates and the ideas adopted versus rejected. Tool architecture, synthetic examples and instruction tests do not establish a false-positive rate or scientific effectiveness.
