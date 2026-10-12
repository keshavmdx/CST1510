"""
RECORD CHECK  -  my version
===========================

Name  : keshav
Lane  :  AI    
Date  : 10/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

over_limit_count = 0

while True:

    # ================================================================ INPUT
    dataset = input("Dataset name (or 'quit') : ")
    if dataset == "quit":
        break

    rows_missing = float(input("Rows missing              : "))
    missing_allowed = float(input("Missing rows allowed      : "))

    # ============================================================== PROCESS
    difference = rows_missing - missing_allowed
    percent = (rows_missing / missing_allowed) * 100

    if percent >= 100:
        status = "OVER LIMIT"
        over_limit_count += 1
    elif percent >= 90:
        status = "WARNING"
    else:
        status = "OK"

    # =============================================================== OUTPUT
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {dataset}")
    print("=" * 34)
    print(f"  Missing     : {rows_missing:>10.2f}")
    print(f"  Allowed     : {missing_allowed:>10.2f}")
    print(f"  Difference  : {difference:>+10.2f}")
    print(f"  Of allowed  : {percent:>9.1f} %")
    print(f"  Status      : {status:>10}")
    print("=" * 34)
    print()

print(f"Records over limit: {over_limit_count}")