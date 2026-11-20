import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def run_ledger(fixture: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, str(ROOT / "ledger.py"), str(ROOT / "fixtures" / fixture)],
        capture_output=True,
        text=True,
        timeout=10,
    )


class LedgerTest(unittest.TestCase):
    def test_totals_include_negative_transactions(self):
        result = run_ledger("transactions.csv")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout), {"meals": 450, "travel": 1000})

    def test_non_integer_amount_fails(self):
        result = run_ledger("invalid_amount.csv")
        self.assertNotEqual(result.returncode, 0)


if __name__ == "__main__":
    unittest.main()
