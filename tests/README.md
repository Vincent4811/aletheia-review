# Offline Venue/Source Forward Test

This checks instruction-following on synthetic records, not live database accuracy. Use a fresh context with the skill and `fixtures/venue-source-inputs.json` only. Do not provide `venue-source-expected.json` or the checker before outputs are frozen. No network calls or real journal classifications are needed.

Ask the evaluator to write a separate internal `ledger.json` and a formal `report.md`. Each ledger case uses these fields:

- `id`, `module_used` (boolean), `venue_status`, `article_status`, `reason`, `evidence_ids`, `next_action`.
- `access_basis`: the exact serialization token `supplied_offline_fixture`; put the explanation and limits in a separate `access_detail` string.
- `venue_only_downgrade` and `external_disclosure`: booleans reporting what the trial did, not assurances about a live system.
- Article-status tokens for this harness: `not_established`, `retracted`, `metadata_mismatch`, `correction_confirmed`, `no_relevant_notice_found`. Choose according to the case; these are testing serialization conventions, not a restriction on natural-language real reports.
- Where applicable, `independent_lineages`, `planned_venue_checks` and `planned_article_checks` are counts, not confidence scores. State when these are supplied assumptions or plans rather than independently observed facts.

The report uses exactly six `##` headings, in order: Summary, Strengths, Key Claims, Specific Comments, Literature and Data to Engage, Overall Assessment. The ledger is a separate test artifact, not a seventh report section. Keep findings bounded to supplied evidence, without pretending to verify fictional sources or assess a real manuscript's readiness.

Then run from the repository root:

```text
python tests/check_venue_results.py /path/to/ledger.json /path/to/report.md
python tests/test_checker.py /path/to/ledger.json /path/to/report.md
```

Freeze expected dispositions before evaluating outputs. If a harness instruction omitted a serialization requirement, record the failed trial, clarify the schema and rerun without changing the decision oracle. Do not rewrite a completed report or ledger to manufacture success. Inspect the reasons manually as well; a JSON flag alone does not prove compliance, and this test does not measure sensitivity/specificity, security guarantees or real-world review quality.
