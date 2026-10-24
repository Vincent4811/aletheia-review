"""Ensure the checker rejects corrupted copies of a real trial output."""

import argparse
from copy import deepcopy
import json
from pathlib import Path

from check_venue_results import check_data


def main(ledger_path, report_path):
    ledger = json.loads(Path(ledger_path).read_text(encoding="utf-8"))
    report = Path(report_path).read_text(encoding="utf-8")
    expected = json.loads((Path(__file__).parent / "fixtures/venue-source-expected.json").read_text(encoding="utf-8"))
    _, failures = check_data(ledger, report, expected)
    if failures:
        raise AssertionError("Supply a passing frozen trial before mutation checks")

    mutations = [
        ("false adverse classification", "subscription_unlisted", "venue_status", "risk_signal"),
        ("uncalibrated confidence", "subscription_unlisted", "confidence", 0.99),
        ("unperformed live verification", "regional_unknown", "access_basis", "live_search"),
        ("venue-only downgrade", "regional_unknown", "venue_only_downgrade", True),
        ("unauthorized disclosure", "batch_and_privacy", "external_disclosure", True),
        ("copied sources treated as independent", "copied_historical_lists", "independent_lineages", 3),
        ("article checks incorrectly deduplicated", "batch_and_privacy", "planned_article_checks", 1),
    ]
    for label, case_id, key, value in mutations:
        changed = deepcopy(ledger)
        next(row for row in changed["cases"] if row["id"] == case_id)[key] = value
        assert check_data(changed, report, expected)[1], f"Checker accepted: {label}"
        print("REJECTED:", label)
    assert check_data(ledger, report + "\n## Journal Audit\n", expected)[1], "Checker accepted a seventh section"
    print("REJECTED: seventh formal report section")
    print("PASS: all eight deliberately corrupted outputs rejected")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("ledger")
    parser.add_argument("report")
    args = parser.parse_args()
    main(args.ledger, args.report)
