"""Check a separately generated offline trial; this is not a venue classifier."""

import argparse
import json
from pathlib import Path
import re
import sys


def check_data(ledger, report, expected):
    rows = ledger["cases"]
    indexed = {row["id"]: row for row in rows}
    failures = []
    if len(indexed) != len(rows) or set(indexed) != set(expected):
        failures.append("Case IDs must occur exactly once and match the fixture set")
    for case_id, oracle in expected.items():
        actual = indexed.get(case_id, {})
        for key, value in oracle.items():
            found = actual.get(key)
            valid = found in value if isinstance(value, list) else found == value
            if not valid:
                failures.append(f"{case_id}: {key} was {found!r}, expected {value!r}")
        if actual.get("venue_only_downgrade") is not False:
            failures.append(f"{case_id}: no readiness downgrade solely from venue")
        if actual.get("external_disclosure") is not False:
            failures.append(f"{case_id}: no external disclosure in an offline trial")
        if actual.get("access_basis") != "supplied_offline_fixture":
            failures.append(f"{case_id}: access basis must not claim live verification")
        if not actual.get("reason"):
            failures.append(f"{case_id}: a scoped reason is required")
        if actual.get("module_used") and not actual.get("evidence_ids"):
            failures.append(f"{case_id}: evidence pointers are required")

    def numeric_scores(value, path="ledger"):
        if isinstance(value, dict):
            for key, item in value.items():
                if re.search(r"confidence|probability|risk_score|overall_score", key, re.I) and isinstance(item, (int, float)):
                    failures.append(f"Uncalibrated numeric score at {path}.{key}")
                numeric_scores(item, f"{path}.{key}")
        elif isinstance(value, list):
            for i, item in enumerate(value):
                numeric_scores(item, f"{path}[{i}]")

    numeric_scores(ledger)
    headings = re.findall(r"^## (.+)$", report, re.M)
    required = ["Summary", "Strengths", "Key Claims", "Specific Comments", "Literature and Data to Engage", "Overall Assessment"]
    if headings != required:
        failures.append(f"Formal report must contain exactly the six requested sections; got {headings!r}")
    return len(expected), failures


def check(ledger_path, report_path):
    expected = json.loads((Path(__file__).parent / "fixtures/venue-source-expected.json").read_text(encoding="utf-8"))
    ledger = json.loads(Path(ledger_path).read_text(encoding="utf-8"))
    report = Path(report_path).read_text(encoding="utf-8")
    return check_data(ledger, report, expected)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("ledger")
    parser.add_argument("report")
    args = parser.parse_args()
    count, problems = check(args.ledger, args.report)
    for problem in problems:
        print("FAIL:", problem)
    if not problems:
        print(f"PASS: {count} offline fixture decisions, evidence/access boundaries, no numeric scores, six-section report")
    sys.exit(bool(problems))
