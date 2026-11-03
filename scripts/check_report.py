#!/usr/bin/env python3
"""Lightweight completeness checker for Agent SEO Markdown reports.

This checks for required report sections; it does not validate SEO quality or scores.
Usage:
  python scripts/check_report.py templates/initial-audit-report.md --type initial
  python scripts/check_report.py templates/final-comparison-report.md --type final
"""
import argparse
from pathlib import Path

REQUIRED = {
    "initial": [
        "Executive summary", "Business and product understanding",
        "Competitor landscape", "Top-five SERP research",
        "SEO findings and strategy", "GEO findings and strategy",
        "AEO findings and strategy", "Baseline scores", "Approval request",
    ],
    "final": [
        "Executive summary", "Before-and-after scores",
        "Criterion-level score comparison", "Completed changes",
        "UI preservation and consent audit", "Tests and validation",
        "Deployment", "Deferred, rejected, failed or incomplete items",
        "Monitoring plan",
    ],
}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("report", type=Path)
    parser.add_argument("--type", choices=REQUIRED, required=True)
    args = parser.parse_args()
    if not args.report.is_file():
        raise SystemExit(f"Report not found: {args.report}")
    content = args.report.read_text(encoding="utf-8").lower()
    missing = [heading for heading in REQUIRED[args.type] if heading.lower() not in content]
    if missing:
        print("INCOMPLETE — missing expected sections:")
        for item in missing:
            print(f"- {item}")
        raise SystemExit(1)
    print(f"PASS — required {args.type} report sections are present.")
    print("Note: this is a structural check only, not a factual or quality audit.")

if __name__ == "__main__":
    main()
