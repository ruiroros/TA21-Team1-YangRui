from pathlib import Path
# cwd now is np one drive/"IGP PFB"/"project_group"/"cash_on_hand.py"
fp = Path.cwd()
cash_fp = fp/"csv_reports"/"cash-on-hand-usd.csv"
print(fp)
print(cash_fp)

with cash_fp.open(mode='r', encoding='UTF-8') as file:
    cash_read = file.read()

print(cash_read)
