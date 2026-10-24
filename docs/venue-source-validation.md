# Optional Venue/Source Module Validation

Date: 2026-10-25. Package version: 1.1.0.

## Scope and Fixed Criteria

This was an offline instruction-following trial, not a test of a live journal classifier. Ten invented cases and a decision oracle were prepared before evaluation. The oracle was not changed after results were seen; SHA-256 is `F543EC5D662B819E59A98C9A38121ACA3439F548508E4ACF620181DC991A6C52`.

Acceptance required bounded case dispositions, no readiness downgrade solely from venue, honest offline provenance, evidence pointers, no numeric confidence output, appropriate separation of venue/article status, and exactly six formal report sections. The existing formal-report and confidentiality blocks were compared with the prior published skill and remained unchanged.

## Forward Trials

1. A separate fresh model context received the skill, its references and synthetic input packet, not the decision oracle. Its venue dispositions matched the intended cases on manual inspection, but the automated checker failed: the harness had not specified its required fixed access-mode token, and an article-status synonym differed from the expected serialization. The original output was preserved unchanged. This trial is not counted as an automated pass.
2. The harness protocol was clarified with explicit serialization fields in `tests/README.md`; the decision oracle and skill decision rules were not loosened. A new fresh context received the same raw cases and the explicit schema, without the oracle or prior outputs. It generated a new ledger and consolidated report. The checker passed all ten cases, and the parent inspected the actual reasons and report for the intended boundaries.

These are two runs over the same synthetic packet, not twenty independent cases or independent real-world data. Both used separate model contexts; this is not an independent scientific replication, a human review panel or multi-model benchmark.

## Observed Dispositions in the Schema-Explicit Trial

| Case | Observed bounded result |
| --- | --- |
| Ordinary reasoning-only review | Module not activated; no venue check claimed. |
| Subscription venue absent from DOAJ | Identity checked within supplied records; absence and uncontrolled metrics not treated as adverse. |
| Regional-language venue without identity evidence | Insufficient data; no language/geography penalty. |
| Two current incompatible audits | Conflict preserved; no vote-based conclusion. |
| Name and identifier mismatch | Insufficient data rather than merging similar names or alleging fraud. |
| Exact candidate-domain impersonation warning | Risk signal scoped to that domain, not the real journal's entire output. |
| Exact article retraction | Venue identity checked separately; retraction stays article-specific. |
| Three copies of a historical list | One evidence lineage; insufficient basis for a current adverse conclusion. |
| DOI/citation metadata mismatch | Identity unresolved; missing Crossmark not treated as a clean status. |
| Batch/privacy plan | One reusable venue check and three article checks planned; no live execution or bibliography forwarding claimed. |

## Rejection and Structural Checks

Starting from the frozen passing trial, the checker rejected eight deliberately corrupted copies: false adverse classification, numeric confidence, false live-verification mode, venue-only downgrade, external-disclosure flag, inflated independent lineage count, article checks incorrectly deduplicated, and a seventh report section. These mutations test the checker, not eight additional model reviews.

Skill validation, JSON parsing, test-checker syntax, fixture/oracle ID alignment, relative-link targets, version metadata, publication disclosure scans and unchanged six-section/safety-contract checks passed. Raw trial ledgers/reports are retained in the task workspace; the public repository includes the reproducible protocol, synthetic inputs, frozen oracle and checking scripts.

## Limits

No real API lookup, journal identity, publisher allegation, article retraction or confidential manuscript was evaluated in these trials. Privacy/activation flags were interpreted with reasons and report text, not instrumented to establish exfiltration prevention. No sensitivity, specificity, calibrated confidence, false-positive rate, real-world scientific review benefit or universal cross-client activation is established. Live use still requires source verification, relevant journal AI-use policy, coverage/date awareness and human judgment.
