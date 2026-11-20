# Harness engineering practice repo

Use this small Python program to practice giving an assistant clear instructions, checking its work, and comparing two runs. Its CSV files contain fictional transactions.

Use Python 3.10 or newer. The standard library is enough. Git and an AI service are optional. See the [course setup guide](https://harness.rojamahorse.com/en/workshop/local-setup/) for Windows, macOS, and Linux steps. The course has its own access rules.

Run these commands from the folder containing this README. Use python3 on macOS or Linux, or py -3 on Windows, if that is how your computer starts Python.

```text
python -m unittest discover -s tests -v
python ledger.py fixtures/transactions.csv
```

The tests should pass. The sample should print {"meals": 450, "travel": 1000}. Try fixtures/blank_amounts.csv to reproduce the exercise's intentionally unfixed error. The task is to skip empty amounts and preserve the existing behavior for other rows.

Use Code > Download ZIP on GitHub to get another clean copy.