"""Summarize integer-cent transactions by category."""
import argparse
import csv
import json
from collections import defaultdict
from pathlib import Path


def summarize(path: Path) -> dict[str, int]:
    totals = defaultdict(int)
    with path.open(encoding="utf-8", newline="") as csv_file:
        for row in csv.DictReader(csv_file):
            totals[row["category"]] += int(row["cents"])
    return dict(totals)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file", type=Path, help="CSV with category and cents columns")
    args = parser.parse_args()
    try:
        totals = summarize(args.file)
    except (OSError, KeyError, ValueError) as error:
        parser.error(str(error))
    print(json.dumps(totals, sort_keys=True))


if __name__ == "__main__":
    main()
